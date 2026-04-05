from django.apps import AppConfig
from django.apps import AppConfig

class YourAppConfig(AppConfig):
    name = 'tasks'

    def ready(self):
        from django.contrib.auth.models import User
        if not User.objects.filter(username='swetha').exists():
            User.objects.create_superuser('swetha', 'swetha@gmail.com', '1234')

class TasksConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tasks'
