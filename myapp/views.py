import django.utils.timezone
from django.http import HttpResponse
from django.utils import timezone
from datetime import datetime, timedelta
from myapp.models import Task, Subtask


def create_sample_tasks():
    now = timezone.now()

    # создание задачи
    task, created = Task.objects.get_or_create(
        title="Prepare presentation",
        defaults={
            "description": "Prepare materials and slides for the presentation",
            "status": "new",
            "deadline": now + timedelta(days=3)}
    )

    # создаём Subtask
    subtasks_data = [
            {"title": "Gather information",
             "description": "Find necessary information for the presentation",
             "status": "new",
             "deadline": now + timedelta(days=2)},

    {
        "title" : "Create slides",
    "description" : "Create presentation slides",
    "status ": "new",
    "deadline" : now + timedelta(days=1)}
    ]

    for title, desc, days in subtasks_data:
        Subtask.objects.get_or_create(
            title=title,
            task_id=task.id,
            defaults={
                "description": desc,
                "status": "new",
                "deadline": now + timedelta(days=days)
            }
        )
    return task


# Create your views here.
def hello(request):
    return HttpResponse("Hello Raisa!")

