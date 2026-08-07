from django.db import models

# Create your models here.
class Department(models.Model):

    name = models.CharField(
            max_length=100,
            unique=True,
            db_index=True,
        )
    
    code = models.CharField(
            max_length=10,
            unique=True,
            db_index=True,
        )

    description = models.TextField(
        blank = True,
        )

    head= models.OneToOneField(
        "employees.Employee",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='headed_department',
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
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return self.name
