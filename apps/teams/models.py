from django.db import models

# Create your models here.

class Team(models.Model):

    name = models.CharField(
        max_length=100,
        db_index=True,
        )

    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.CASCADE,
        related_name='teams',
    )

    leader = models.OneToOneField(
        "employees.Employee",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="leading_team",
    )

    members = models.ManyToManyField("employees.Employee",related_name="teams",blank=True,)
    description = models.TextField(
        blank=True,
    )

    is_active = models.BooleanField(
        default=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        )

    update_at  = models.DateTimeField(
        auto_now=True,
        )


    class Meta:
        ordering = ['name']
        verbose_name = 'Team'
        verbose_name_plural = 'Teams'

        constraints = [
            models.UniqueConstraint(
                fields=['department','name'],
                name='unique_team_name_per_department',
            )
        ]

    def __str__(self):
        return f"{self.department.name} - {self.name}"