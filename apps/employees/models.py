from django.db import models

# Create your models here.

class EmployeeStatus(models.TextChoices):
    PROBATION = "PROBATION", "Probation"
    ACTIVE = "ACTIVE" , "Active"
    ON_LEAVE = "ON_LEAVE" , "On Leave"
    RESIGNED = "RESIGNED" , "Resigned"
    TERMINATED = "TERMINATED","Terminated"


class Employee(models.Model):

    # Authentication
    user = models.OneToOneField(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="employee_profile",
    )


    # Compnay Identity
    employee_id = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
        db_index=True,
    )

    # Organization
    ''' <-----------x-------------x-----------------> '''
    department = models.ForeignKey(
        "departments.Department",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="employees",
    )

    manager = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="subordinates",
    )

    # Employment
    joining_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=EmployeeStatus.choices,
        default=EmployeeStatus.PROBATION,
        db_index=True,
    )


    # Personal
    phone_number = models.CharField(
        max_length = 15,
        unique = True,
        db_index=True,
    )

    profile_photo = models.ImageField(
        upload_to="employees/profile/",
        blank=True,
        null = True,
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    # Audit
    created_at = models.DateTimeField(
        auto_now_add = True,
        )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    team= models.ForeignKey(
        'teams.Team',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employees',

        )
    
    class Meta:
        ordering = ["employee_id"]
        verbose_name = "Employee"
        verbose_name_plural = "Employee"

    def __str__(self):
        return f"{self.employee_id} - {self.user.email}"