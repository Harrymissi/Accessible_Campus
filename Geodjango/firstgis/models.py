from django.db.models import Manager as GeaoManager
from django.contrib.gis.db import models

# Create your models here.
class Incidences(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects = GeaoManager()

    def __int__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Incidences"  # 显示在admin中的



class Countie(models.Model):
    counties = models.CharField(max_length=25)
    codes = models.IntegerField()
    cty_code = models.CharField(max_length=24)
    dis = models.IntegerField()
    geom = models.MultiPolygonField(srid=4326)

    def __int__(self):
        return self.counties


class Accessble_Entr(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects = GeaoManager()

    def __int__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Accessble Entrance"  # 显示在admin中的

class Handi_Transit(models.Model):
    name = models.CharField(max_length=20)
    location = models.PointField(srid=4326)
    objects = GeaoManager()

    def __int__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Handi Transit Stop"  # 显示在admin中的