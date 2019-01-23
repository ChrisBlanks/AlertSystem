from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.http import Http404

def index(request):
	device_id = None
	user_type = None
	if request.method == "POST":
		device_id = request.POST.get('id_number',None)
		user_type = request.POST.get('user_type',None)
		print (user_type)
		print(user_type)
		print(user_type)
		#print(request.user.is_authenticated)
		#print(request.user.is_supervisor_user)
    
	if device_id == None or device_id == "":
		msg = "Logged in, but not using a registered device."
	else:
		msg = "Logged in with device: " + str(device_id)
		
	context = {'message': msg,'user_type':user_type}
	return render(request,'Alert_App/index.html', context)
	

def report(request):
	"""Sets up view for reporting emergencies."""
	user_type = None 
	if request.method == "POST":
		user_type = request.POST.get('user_type',None)
	context = {'user_type':user_type}
	return render(request,'Alert_App/report.html',context)
	


