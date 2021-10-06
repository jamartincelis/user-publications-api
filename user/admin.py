from django.contrib import admin

from user.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'optional_id', 'email']


admin.site.register(User, UserAdmin)
