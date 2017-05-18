from django.shortcuts import render
from django.shortcuts import render
from .models import PointOfInterest
import csv
import xlwt
import calendar
import django_excel as excel
from .forms import UploadFileForm
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.http import StreamingHttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
from django import template
import pyexcel.ext.xls
# Create your views here.



def import_sheet(request):
	if request.method == "POST":
		form = UploadFileForm(request.POST,
							  request.FILES)
		if form.is_valid():
			request.FILES['file'].save_to_database(
				name_columns_by_row=2,
				model=PointOfInterest,
				mapdict=['Accident_Index', 'Location_Easting_OSGR', 'Location_Northing_OSGR','Longitude','Latitude','Police_Force','Accident_Severity','Number_of_Vehicles','Number_of_Casualties','Date','Day_of_Week','Time','Local_Authority_District','Local_Authority_Highway','first_Road_Class','first_Road_Number','Road_Type','Speed_limit','Junction_Detail','Junction_Control','second_Road_Class','second_Road_Number','Pedestrian_Crossing_Human_Control','Pedestrian_Crossing_Physical_Facilities','Light_Conditions','Weather_Conditions','Road_Surface_Conditions','Special_Conditions_at_Site','Carriageway_Hazards','Urban_or_Rural_Area','Did_Police_Officer_Attend_Scene_of_Accident','LSOA_of_Accident_Location'])
			return HttpResponse("OK")
		else:
			return HttpResponseBadRequest()
	else:
		form = UploadFileForm()
	return render(
		request,
		'upload_form.html',
		{'form': form})



def poi_list(request):
	pois = PointOfInterest.objects.all()
	context = {
	'pois' : pois
	}
	return render(request, 'maps1.html', context)

