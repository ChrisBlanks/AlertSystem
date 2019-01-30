from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from Alert_App.models import Users, Marker, DeviceId


admin.site.unregister(User) 

class DeviceIdInline(admin.TabularInline):
	"""Allows device id to be edited within admin page."""
	model = DeviceId
	

class MarkerAdmin(admin.ModelAdmin):
	fieldsets = [
		( 'Name' , { 'fields': ['name'] } ),
		( 'X-position in Image' , { 'fields': ['x_position'] } ),
		( 'Y-position in Image' , { 'fields': ['y_position'] } ),
		( 'Activation status' , { 'fields': ['activated'] } ),
		( 'Is it currently on alert?' , { 'fields': ['isAlerting'] } ),
	]
	inlines=[DeviceIdInline]
	list_display = ('name','activated','isAlerting')
	

class UsersInline(admin.StackedInline):
	"""Allows admin interface to edit the given model on the same page as the parent model."""
	model = Users
	extra = 0
	can_delete = True
	
	verbose_name_plural = "user"

	
class UserAdmin(UserAdmin):
	"""Adds the Inline to the admin user """
	inlines = (UsersInline,)

 
admin.site.register(Users)   #registers my custom model
admin.site.register(User,UserAdmin) #reloads default models w/ my changes
admin.site.register(Marker,MarkerAdmin)
