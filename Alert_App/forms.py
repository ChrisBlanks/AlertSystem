from django import forms 
from Alert_App.models import Marker, DeviceId

class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
        fields = ('phone','age','gender','address','bio')