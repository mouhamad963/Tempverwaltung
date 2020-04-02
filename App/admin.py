from django.contrib import admin

from .models import Benutzer ,Logs ,Sensors, Temperaturen
# Register your models here.

admin.site.register(Benutzer)
admin.site.register(Sensors)
admin.site.register(Temperaturen)

admin.site.register(Logs)