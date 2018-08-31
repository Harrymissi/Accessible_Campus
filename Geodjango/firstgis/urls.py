_auther_ = 'Harry'
_date_ = '7/26/2018 9:42 PM'

from .views import HomePageView, county_dataset, point_dataset,Accessible_Entr,handi_dataset,access_entr_dataset
from django.urls import path

app_name = 'firstgis'

urlpatterns = [
    path('',HomePageView.as_view(),name='home'),
    path('county_data/',county_dataset,name="county"),
    path('incidence_data/',point_dataset,name="incidence"),
    path('campus_map/',Accessible_Entr,name="campus_map"),
    path('handi_data/',handi_dataset,name="handi_data"),
    path('access_entr_data/',access_entr_dataset,name="access_entr_data"),
]
