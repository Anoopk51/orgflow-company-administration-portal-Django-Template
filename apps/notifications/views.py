from django.contrib.auth.decorators import login_required
from django.shortcuts import render ,redirect, get_object_or_404

from .models import Notification , NotificationType

# Create your views here.

@login_required
def notification_list(request):

    notifications = Notification.objects.filter(recipient = request.user)

    unread_count = notifications.filter(is_read = False).count()

    return render(request,"notifications/notification_list.html",{"notifications":notifications,"unread_count":unread_count,},)

@login_required
def mark_notification_read(request,notification_id):

    notification = get_object_or_404(Notification,id=notification_id,recipient = request.user,)

    if request.method == "POST":
        notification.is_read = True
        notification.save(update_fields=["is_read"])
    return redirect("notification_list")
