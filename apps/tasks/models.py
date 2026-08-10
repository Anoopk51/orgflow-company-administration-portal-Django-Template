from django.db import models

# Create your models here.

class TaskStatus(models.TextChoices):
    TODO = "TODO","To Do"
    IN_PROGRESS = "IN_PROGRESS","In Progress"
    IN_REVIEW = "IN_REVIEW" ,"In Review"
    COMPLETED = "COMPLETED","Completed"
    CANCELLED = "CANCELLED","Cancelled"

class TaskPriority(models.TextChoices):
    LOW = "LOW", "Low"
    MEDIUM = "MEDIUM" ,"Medium"
    HIGH = "HIGH","High"
    URGENT = "URGENT","Urgent"

class Task(models.Model):

    title = models.CharField(
        max_length= 200,
        db_index=True,
    )

    description = models.TextField(
        blank=True,
    )

    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name='tasks',
    )

    assigned_to = models.ForeignKey(
        "employees.Employee",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_tasks",
    )

    status = models.CharField(
        max_length=20,
        choices=TaskStatus.choices,
        default=TaskStatus.TODO,
        db_index=True,
    )

    priority = models.CharField(
        max_length=10,
        choices=TaskPriority.choices,
        default=TaskPriority.MEDIUM,
        db_index=True,
    )

    due_date = models.DateField(
        null = True,
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add = True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

    def __str__(self):
        return self.title