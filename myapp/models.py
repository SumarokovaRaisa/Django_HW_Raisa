from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    STATUS_CHOICE = [
        ("new", "New"),
        ("in_progress", "In_progress"),
        ("blocked", "Blocked"),
        ("done", "Done"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    categories = models.ManyToManyField(Category, related_name="tasks", blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default="new")
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("title", "created_at")  # уникально для даты

    def __str__(self):
        return self.title


class Subtask(models.Model):
    STATUS_CHOICE = [
        ("new", "New"),
        ("in_progress", "In_progress"),
        ("blocked", "Blocked"),
        ("done", "Done"),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="subtask")
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, default="new")
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.task.title} -> {self.title}"
