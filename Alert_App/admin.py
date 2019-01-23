from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from Alert_App.models import Users


class UsersInline(admin.StackedInline):
    model = Users
    can_delete = False
    verbose_name_plural = "users"

class UserAdmin(UserAdmin):
    inlines = (UsersInline,)

admin.site.unregister(User)
admin.site.register(User,UserAdmin)
