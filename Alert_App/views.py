from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import authenticate

from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404

def index(request):
	device_id = None
	user_type = None
	isNotValidUser = False
	msg = ""
	
	if request.method == "POST":
		username = request.POST.get('username',None)
		print(username)
		password = request.POST.get('password',None)
		print(password)
		
		if request.user.is_authenticated:
			pass #if user is already authenticated, skip 
		else:
			user = authenticate(username=username,password=password) #checks credentials against authentication backend
			if user:
				login(request,user) #if authenticated, login using database credentials
				device_id = request.POST.get('id_number',None)
				user_type = user.users.is_supervisor_user #get user type for later use in forms
			else:
				isNotValidUser = True #not a valid user
				msg = msg + "Not a valid user. "
    
	if device_id == None or device_id == "":
		msg = msg + "Not using a registered device."
	else:
		msg = msg + "Logged in with device: " + str(device_id)
		
	context = {'message': msg,'user_type':user_type,'isNotValidUser':isNotValidUser}
	return render(request,'Alert_App/index.html', context)
	

def report(request):
	"""Sets up view for reporting emergencies."""
	user_type = None 
	print("Before POST check")
	if request.method == "POST":
		print("Post received.")
		user_type = request.POST.get('user_type',None)
		print("After POST")
		print(user_type)
	context = {'user_type':user_type}
	return render(request,'Alert_App/report.html',context)
	

def map(request):
	"""Sets up view for map and markers."""
	return render(request,'Alert_App/map.html')
	


