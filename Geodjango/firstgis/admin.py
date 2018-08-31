from django.contrib import admin
from .models import Incidences,Countie,Accessble_Entr,Handi_Transit
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class IncidencesAdmin(LeafletGeoAdmin):
    list_display = ('name','location')
admin.site.register(Incidences,IncidencesAdmin)


class CountieAdmin(LeafletGeoAdmin):
    list_display = ('counties','codes')
admin.site.register(Countie, CountieAdmin)


class Accessble_EntrAdmin(LeafletGeoAdmin):
    list_display = ('name','location')
admin.site.register(Accessble_Entr,Accessble_EntrAdmin)


class Handi_Admin(LeafletGeoAdmin):
    list_display = ('name','location')
admin.site.register(Handi_Transit,Handi_Admin)