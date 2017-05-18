from django import forms
from .models import PointOfInterest



class UploadFileForm(forms.Form):
	file = forms.FileField()
