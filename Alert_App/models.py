from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser, User


class Users(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	is_supervisor_user = models.BooleanField(default=False)
	
	def get_supervisor_status(self):
		"""Returns status of whether a user is a supervisor or not."""
		return self.is_supervisor_user
	
	def get_is_authenticated(self):
		"""Returns authentication value."""
		return self.user.is_authenticated
		

def create_users(sender,instance,created,**kwargs):
	if created:
		Users.objects.create(user=instance)

post_save.connect(create_users,sender=User)