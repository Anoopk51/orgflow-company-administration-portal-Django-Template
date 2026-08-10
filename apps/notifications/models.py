from django.db import models

# Create your models here.

class NotificationType(models.TextChoices):
    TASK_ASSIGNED = "TASK_ASSIGNED" ,"Task Assigned"
    TASK_UPDATED = "TASK_UPDATED","Task Updated"
    PROJECT_UPDATED = "PROJECT_UPDATED" ,"Project Updated"
    TEAM_ADDED = "TEAM_ADDED" ,"Team Added"
    APPROVAL_REQUIRED = "APPROVAL_REQUIRED" ,"Approval Required"
    APPROVAL_COMPLETED = "APPROVAL_COMPLETED" , "Approval Completed"
    GENERAL = "GENERAL" , "General"

class Notification(models.Model):

    recipient = models.ForeignKey(
        "accounts.User",
        on_delete=models.CASCADE,
        related_name="notifications",
    )

    notification_type = models.CharField(
        max_length=30,
        choices=NotificationType.choices,
        db_index=True,
    )

    title = models.CharField(
        max_length= 150,
    )

    message = models.TextField()

    is_read = models.BooleanField(
        default=False,
        db_index=True,
    )

    created_at = models.DateTimeField(
        auto_now_add = True,
    )

    class Meta:
        ordering =["-created_at"]
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        return f"{self.recipient.email} - {self.title}"