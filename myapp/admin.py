from django.contrib import admin
from .models import Task, Subtask, Category


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)


class SubtaskInLine(admin.TabularInline):
    model = Subtask
    extra = 1
    fk_name = "task"


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    def short_title(self, obj):
        return obj.title if len(obj.title) <= 10 else obj.title[:10] + "..."
    short_title.short_description = "Name (short)"


    list_display = ("id", "short_title", "status", "deadline", "created_at")
    list_display_links = ("id", "short_title")
    search_fields = ("title",)
    ordering = ('-created_at',)
    filter_horizontal = ("categories",)
    inlines = [SubtaskInLine]

def mark_done(modeladmin, request, queryset):
    """ Change selected tasks status to 'Done'"""
    queryset.update(status="Done")
mark_done.short_description = "Change to Done"

@admin.register(Subtask)
class SubtaskAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "status", "deadline", "created_at")
    list_filter = ("status", "created_at", "deadline")
    search_fields = ("title",)
    ordering = ('-created_at',)
    actions = [mark_done]
