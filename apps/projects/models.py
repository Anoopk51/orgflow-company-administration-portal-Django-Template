from django.db import models

# Create your models here.

class ProjectStatus(models.TextChoices):
    PLANNED = "PLANNED","Planned"
    IN_PROGRESS = "IN_PROGRESS","In Progress"
    ON_HOLD = "ON_HOLD","On Hold"
    COMPLETED = "COMPLETED" ,"Completed"
    CANCELLED = "CANCELLED","Cancelled"

class Project(models.Model):

    name = models.CharField(
        max_length=150,
        unique=True,
        db_index = True,
    )

    code = models.CharField(
        max_length=20,
        unique=True,
        db_index= True
    )

    description = models.TextField(
                blank= True,
    )

    project_manager  = models.ForeignKey(
        "employees.Employee",
        on_delete = models.SET_NULL,
        null = True,
        blank= True,
        related_name="managed_projects",
    )

    teams = models.ManyToManyField(
        "teams.Team",
        related_name= "projects",
        blank=True,
    )

    start_date = models.DateField()

    end_date = models.DateField(
        null = True,
        blank= True,
    )

    status = models.CharField(
        max_length=20,
        choices= ProjectStatus.choices,
        default=ProjectStatus.PLANNED,
        db_index=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self):
        return f"{self.code} - {self.name}"