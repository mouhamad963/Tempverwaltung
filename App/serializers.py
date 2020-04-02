from rest_framework import serializers
from .models import Benutzer,Logs,Sensors,Temperaturen,Hersteller
from django.db import transaction

class BenutzerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Benutzer
        fields = ('__all__')


class LogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logs
        fields = ('__all__')
        depth = 2


class SensorsSerializer(serializers.ModelSerializer):
    adresse = serializers.CharField()
    
    class Meta:
        model = Sensors
        fields = ('__all__')

class TemperaturenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Temperaturen
        fields = ('__all__')
    
#     @transaction.atomic
#     def create(self, validated_data):
#         temperatur = self.validated_data["temperatur"]
#         sensor = self.validated_data['sensor']
#         if sensor.max_temp < temperatur:
#             msg = f"Warning Sensor {sensor.sensor_id} it above max Temperature"
#         else:
#             msg = f"Sensor {sensor.sensor_id} it works fine"
# 
#         logs = Logs.objects.create(sensor_id=sensor.sensor_id, nachricht=msg,benutzer_id=1)
#         logs.save()
#         
#         temp = Temperaturen.objects.create(sensor_id=sensor.sensor_id, temperatur=temperatur)
# 
#         return logs
#     
#         


class HerstellerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hersteller
        fields = ('__all__')
    
class RequestLogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Logs
        fields = ('__all__')
