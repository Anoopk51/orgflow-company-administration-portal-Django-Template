from django.urls import path
from .views import notification_list , mark_notification_read

urlpatterns = [
    path("notifications/",notification_list,name="notification_list",),
    path("notifications/<int:notification_id>/read/",mark_notification_read,name = "mark_notification_read",),
]