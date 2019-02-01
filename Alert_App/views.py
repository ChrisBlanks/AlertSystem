from django.contrib.auth import views as auth_views
from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth import authenticate


from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404

from Alert_App.sendSms import sendAlertToPolice
from Alert_App.models import Marker, DeviceId
from AlertSystem import settings
import random 


def login_page(request):
	ids = []
	list_of_available_markers = Marker.objects.all()
	print(list_of_available_markers)
	for marker in list_of_available_markers:
		ids.append(marker.deviceid.id_number)
	context = {'device_ids':ids}
	return render(request,"registration\login.html",context)

	
def index(request):
	device_id = None
	user_type = None
	isNotValidUser = False
	users_obj = None
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
				if device_id is not None:
					users_objs = request.user.users_set.filter(using_device_number__gt=-1)
					
					if len(users_objs) > 1:
						users_obj = users_objs[0] #only one users object should be attached to a user object
					elif len(users_objs) < 1:
						raise Exception("No users objects attached to user ")
					else:
						users_obj = users_objs[0]   # list -> single object
					
					users_obj.using_device_number = device_id
					print("stored device number as:"+users_obj.using_device_number)
					
				print(user)
				user_type = users_obj.is_supervisor_user #get user type for later use in forms
				print(user_type)
				users_obj.save()
				user.save()
			else:
				isNotValidUser = True #not a valid user
				msg = msg + "Not a valid user. "
	else:
		print("No post received")
		print(request.user)
		print(request.user.users_set.all())
		print(dir(request.user.users_set))
		users_objs = request.user.users_set.filter(using_device_number__gt=0)
		
		if len(users_objs) > 1:
			users_obj = users_objs[0] #only one users object should be attached to a user object
		elif len(users_objs) < 1:
			raise Exception("No users objects attached to user ")
		else:
			users_obj = users_objs[0]   # list -> single object
		
		device_id = users_obj.using_device_number
    
	list_of_available_markers = Marker.objects.all()
	
	isRegistered = False
	
	for marker in list_of_available_markers:
		if str(device_id) in str(marker.deviceid.id_number):
			isRegistered = True
			break 
	
	if (device_id == None) or (device_id == "" ) or (isRegistered is False):
		msg = msg + "Not using a registered device."
	else:
		msg = msg + "Logged in with device: " + str(device_id)
		
	context = {'message': msg,'user_type':user_type,'isNotValidUser':isNotValidUser,'users':users_obj}
	return render(request,'Alert_App/index.html', context)
	

def report(request):
	"""Sets up view for reporting emergencies."""
	user_type = None 
	if request.method == "POST":
		user_type = request.POST.get('user_type',None)
	context = {'user_type':user_type}
	return render(request,'Alert_App/report.html',context)
	

def map(request):
	"""Sets up view for map and markers."""
	Markers_list = Marker.objects.all() #stores all of the markers in a list
	marker_str = ""
	for marker in Markers_list:
		id = marker.deviceid.id_number
		x_pos = marker.x_position
		y_pos = marker.y_position
		isAlerting = marker.isAlerting
		
		marker_str = marker_str + f"{id} {x_pos} {y_pos} {isAlerting}|"
		print(marker_str)

	users_objs = request.user.users_set.filter(using_device_number__gt=-1)
					
	if len(users_objs) > 1:
		users_obj = users_objs[0] #only one users object should be attached to a user object
	elif len(users_objs) < 1:
		raise Exception("No users objects attached to user ")
	else:
		users_obj = users_objs[0]   # list -> single object
					
	isAllowed = users_obj.is_supervisor_user
	print(isAllowed)
	context = {'marker_str': marker_str,'isAllowed':isAllowed}
	return render(request,'Alert_App/map.html',context)
	
def response(request):
	"""Loads the response view to the report view submission."""
	report_type = None 
	if request.method == "POST":
		isShooter = request.POST.get('isSchoolShooting',None)
		isFire = request.POST.get('isFire',None)
		isInjury = request.POST.get('isInjury',None)
		
		if isShooter is not None:
			report_type = isShooter
		elif isFire is not None: 
			report_type = isFire
		elif isInjury is not None:
			report_type = isInjury
		else:
			report_type = None
	
	if report_type == None:
		return render(request,'Alert_App/response.html')
	elif report_type == "shooter":
		users_objs = request.user.users_set.filter(using_device_number__gt=0)
		
		if len(users_objs) > 1:
			users_obj = users_objs[0] #only one users object should be attached to a user object
		elif len(users_objs) < 1:
			raise Exception("No users objects attached to user ")
		else:
			users_obj = users_objs[0]   # list -> single object

		id_to_set = users_obj.using_device_number
		
		list_of_available_markers = Marker.objects.all()
		for marker in list_of_available_markers:
			if str(id_to_set) == str(marker.deviceid.id_number):
				marker.isAlerting = True
				marker.save()
		
		sendAlertToPolice(id_to_set)
		
	context = {'report_type':report_type}
	return render(request,'Alert_App/response.html',context)
	
	
def sendReport(request):
	"""Sends questionnaire results to officer too."""
	
	if request.method == "POST":
		shooter_proximity = request.POST.get('shooter_proximity',None)
		alone_or_group = request.POST.get('alone_or_group',None)
		any_injuries = request.POST.get('any_injuries',None)
		location_str = request.POST.get('location',None)
		
		if (shooter_proximity is None) and (alone_or_group is None) and (any_injuries is None) :
			print("No feedback.")
		else:
			msg_combination = f"Questionnaire for previous report: \n{shooter_proximity}\n{alone_or_group}\n{any_injuries}\n\n"
			if location_str is not None:
				print("Location is:"+location_str)
				msg_combination = msg_combination + location_str
		
			users_objs = request.user.users_set.filter(using_device_number__gte=0)
			
			if len(users_objs) > 1:
				users_obj = users_objs[0] #only one users object should be attached to a user object
			elif len(users_objs) < 1:
				raise Exception("No users objects attached to user ")
			else:
				users_obj = users_objs[0]   # list -> single object

			device_num = users_obj.using_device_number
			sendAlertToPolice(device_num,default_msg=msg_combination,addLocation=True )
		
	
	return render(request, 'home.html')
			


