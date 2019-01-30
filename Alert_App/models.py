
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser, User
from django.dispatch import receiver


class Marker(models.Model):
	"""Defines a model for storing map markers that correspond to a location."""
	name = models.CharField(max_length=200,default="")
	x_position = models.FloatField(default=-1)
	y_position = models.FloatField(default=-1)
	activated = models.BooleanField(default=False)
	isAlerting = models.BooleanField(default=False)

	
class DeviceId(models.Model):
	"""Defines a model for storing device ids, which correspond with a Marker object."""
	marker = models.OneToOneField(Marker,on_delete=models.CASCADE)
	id_number = models.IntegerField(default=-1)
	
	
class Users(models.Model):
	"""Defines a model with custom attributes, which will be added to the base User class."""
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	id = models.AutoField(primary_key=True)
	is_supervisor_user = models.BooleanField(default=False)
	using_device_number = models.IntegerField(default=-1)  #default is -1 to indicate that it hasn't been changed
	
	def get_supervisor_status(self):
		"""Returns status of whether a user is a supervisor or not."""
		return self.is_supervisor_user
	
	def get_is_authenticated(self):
		"""Returns authentication value."""
		return self.user.is_authenticated
		

def create_users(sender,instance,created,**kwargs):
	""" """
	if created:
		Users.objects.create(user=instance)

post_save.connect(create_users,sender=User,dispatch_uid="AlertApp.models")
#the post_save signal sends the model instance that needs to be saved