from django.db import models
from django.utils import timezone
# Create your models here.


class Species(models.Model):
    name = models.CharField(max_length=50,null=False,unique=True)
    def __str__(self):
        return self.name
class Activities(models.Model):
    name = models.CharField(max_length=50,null=False,unique=True)
    def __str__(self):
        return self.name
class Water(models.Model):
    name = models.CharField(max_length=50, null=False)
    location = models.CharField(max_length=500,null=False,)
    location_url = models.URLField(unique=True)

    warning = models.CharField(max_length=50,blank=True,null=True)
    dissolved_oxygen = models.FloatField(blank=True,null=True)
    # faceal_content = models.FloatField(blank=True,null=True)
    # metal_content = models.FloatField(blank=True,null=True)

    tds = models.FloatField(blank=True,null=True)
    ph = models.FloatField(blank=True,null=True)

    hightide = models.FloatField(blank=True,null=True)
    lowtide = models.FloatField(blank=True, null=True)

    published = models.DateTimeField("published date", auto_now_add=True)

    species = models.ManyToManyField(to=Species,blank=True, null=True)
    activities = models.ManyToManyField(to=Activities,blank=True, null=True)


    line1 = models.TextField(blank=True, null=True)
    line2 = models.TextField(blank=True, null=True)
    line3 = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
