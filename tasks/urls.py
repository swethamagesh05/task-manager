from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('create/', views.create_task, name='create_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('login/', auth_views.LoginView.as_view(
    redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]