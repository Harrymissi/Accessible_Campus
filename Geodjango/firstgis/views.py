from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Countie,Incidences,Accessble_Entr,Handi_Transit
import json
# Create your views here.

class HomePageView(TemplateView):
    template_name = 'index.html'


class Campus_MapView(TemplateView):
    template_name = 'camples_map.html'

def county_dataset(request):
    counties = serialize('geojson',Countie.objects.all())
    return HttpResponse(counties,content_type="json")

def point_dataset(request):
    points = serialize('geojson',Incidences.objects.all())
    return HttpResponse(points,content_type="json")

def access_entr_dataset(request):
    points = serialize('geojson',Accessble_Entr.objects.all())
    return HttpResponse(points,content_type="json")

def handi_dataset(request):
    points = serialize('geojson',Handi_Transit.objects.all())
    return HttpResponse(points,content_type="json")


def Accessible_Entr(request):
    if request.method == 'POST':
        loc = request.POST['location']
        location = Incidences.objects.filter(name=loc)
        loc_json = serialize('geojson', location)
        loc_dict = json.loads(loc_json)
        loc_lat = loc_dict['features'][0]['geometry']['coordinates'][1]  # 纬度
        loc_lo = loc_dict['features'][0]['geometry']['coordinates'][0]  # 经度
        return render(request, 'camples_map.html', {
            'loc_lat': loc_lat,
            'loc_lo': loc_lo,
        })
    else:
        return render(request,'camples_map.html',{})
