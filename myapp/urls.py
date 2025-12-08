from django.urls import path
from .views import hello
from myapp.views import create_sample_tasks
from django.http import HttpResponse

def sample_task_view(request):
    task = create_sample_tasks()
    return HttpResponse(f"Task {task.title} and subtasks created ")


urlpatterns = [
    path('hello/', hello),
    path('create-task/', sample_task_view),
]