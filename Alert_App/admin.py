from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from Alert_App.models import Users


class UsersInline(admin.StackedInline):
	"""Allows admin interface to edit the given model on the same page as the parent model."""
	model = Users
	can_delete = False
	verbose_name_plural = "users"

class UserAdmin(UserAdmin):
	"""Adds the Inline to the admin user """
	inlines = (UsersInline,)

admin.site.unregister(User)  
admin.site.register(Users)   #registers my custom model
admin.site.register(User,UserAdmin) #reloads default models w/ my changes
