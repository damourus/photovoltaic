from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Location, InverterCategory, PvCategory, Photovoltaic, Inverter, Radiation)

class ViewAdmin(ImportExportModelAdmin):
    pass
