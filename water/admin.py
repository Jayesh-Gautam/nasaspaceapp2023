from django.contrib import admin
from .models import *
# Register your models here.

class WaterAdmin(admin.ModelAdmin):
    list_display = ["name","location","published"]
    empty_value_display = "--"
    exclude = ["published"]
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ["name"]
    empty_value_display = "--"
class ActivitiesAdmin(admin.ModelAdmin):
    list_display = ["name"]
    empty_value_display = "--"

admin.site.register(Water,WaterAdmin)
admin.site.register(Species,SpeciesAdmin)
admin.site.register(Activities,ActivitiesAdmin)