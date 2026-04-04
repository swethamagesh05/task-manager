from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now


@login_required
def dashboard(request):
    tasks = Task.objects.filter(user=request.user)

    pending = tasks.filter(status='PENDING')
    in_progress = tasks.filter(status='IN_PROGRESS')
    completed = tasks.filter(status='COMPLETED')

    return render(request, 'dashboard.html', {
        'pending': pending,
        'in_progress': in_progress,
        'completed': completed,
        'now': now()
    })


@login_required
def create_task(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        status = request.POST['status']
        deadline = request.POST['deadline']

        Task.objects.create(
            user=request.user,
            title=title,
            description=description,
            status=status,
            deadline=deadline
        )

        return redirect('dashboard') 

    return render(request, 'create_task.html') 


@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect('dashboard')