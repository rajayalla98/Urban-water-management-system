from __future__ import unicode_literals
from .models import sensor
from django.shortcuts import render
from django.http import HttpResponse
def index(request):
	received_data=sensor.objects.all()[len(sensor.objects.all())-1]
	all_obj=sensor.objects.all()
	#temp_data=str(received_data.tem_value)
	#hum_data=str(received_data.hum_value)	
	soil_data=str(received_data.soil_value)
	level_data=str(received_data.water_level)
	flow_data=str(received_data.water_flow)
	turb_data=str(received_data.turbidity)
	ph_data=str(received_data.ph)
	result=str(received_data.result)
	context={'flow':flow_data,'result':result,'soil':soil_data,'level':level_data,'all_obj':all_obj,'turb':turb_data,'ph':ph_data}
	return render(request,'sensor/index.html',context)

def getdata(request):
	if request.method=='GET' :
		#tem_value=request.GET['temperature']
		#hum_value=request.GET['humidity']
		soil_value=request.GET['soilmoisture']
		water_level=request.GET['waterlevel']
		water_flow=request.GET['waterflow']
		turbidity=request.GET['turbidity']
		ph=request.GET['ph']
		result=request.GET['request']
		t_obj=sensor()
		#t_obj.tem_value=tem_value
		#t_obj.hum_value=hum_value
		t_obj.soil_value=soil_value
		t_obj.water_level=water_level
		t_obj.water_flow=water_flow
		t_obj.turbidity=turbidity
		t_obj.ph=ph
		t_obj.request=request
		t_obj.save()
		return HttpResponse("data saved in db")
	else:
		return HttpResponse("error")