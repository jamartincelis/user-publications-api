from django.contrib import admin

from notification.models import Notification


class NotificationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'metadata']

admin.site.register(Notification, NotificationAdmin)
