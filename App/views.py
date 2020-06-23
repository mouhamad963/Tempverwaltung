from rest_framework import viewsets,permissions
from .serializers import BenutzerSerializer,SensorsSerializer,TemperaturenSerializer,LogsSerializer,HerstellerSerializer,RequestLogsSerializer
from .models import Benutzer,Temperaturen,Logs,Sensors,Hersteller
from rest_framework_filters.filterset import FilterSet
from django_filters.rest_framework.backends import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password

# Create your views here.



class AuthView(APIView):
    """
    A viewset for Authitication a user.
    """
    queryset = User.objects.all()
    def get(self,request):
        user = self.request.user
        
        if user.is_authenticated:
            return Response({"Authentication":"Success"})
        else:
            return Response({"Authentication":"Failed"})

    



class BenutzerView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset = Benutzer.objects.all()
    serializer_class = BenutzerSerializer
   

    filter_backends = (DjangoFilterBackend,
                       SearchFilter,
                       OrderingFilter,
                       )


    search_fields = ("name","anmeldename","telefonnr")

    ordering_fields = ("name","anmeldename","telefonnr")
    
    def create(self,request):
            
        name = self.request.data["name"]
        anmeldename = self.request.data['anmeldename']
        telefonnr = self.request.data['telefonnr']
        password = self.request.data['password']
        
        user = self.queryset.create(name=name,anmeldename=anmeldename,telefonnr=telefonnr)
        user.password = make_password(password)
        user.save()
        
        u = User(username=anmeldename)
        u.set_password(password)
        u.is_superuser = False
        u.is_staff = False
        try:
            u.save()
        except Exception:
            pass
        
        
        return Response(BenutzerSerializer(user).data)

        
class TemperaturenView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset =  Temperaturen.objects.all()
    serializer_class =  TemperaturenSerializer
    
    
    filter_backends = (DjangoFilterBackend,
                       SearchFilter,
                       OrderingFilter,
                       )

    search_fields = ("temperatur_id", "datum", "temperatur", "sensor__adresse")
    ordering_fields =  ("temperatur_id", "datum", "temperatur", "sensor_id")
    
    
    def create(self,request):
        temperatur = self.request.data["temperatur"]
        sensor_id = self.request.data['sensor']
        sensor = Sensors.objects.get(sensor_id=sensor_id)
        if sensor.max_temp < int(temperatur):
            msg = f"Warning Sensor {sensor.sensor_id} it above max Temperature"
        else:
            msg = f"Sensor {sensor.sensor_id} it works fine"

        logs = Logs.objects.create(sensor_id=sensor.sensor_id, nachricht=msg,benutzer_id=self.request.user.id)
        logs.save()
        
        temp = Temperaturen.objects.create(sensor_id=sensor.sensor_id, temperatur= int(temperatur))

        return Response(TemperaturenSerializer(temp).data)
    
        
    
class LogsView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset =  Logs.objects.all().order_by('-datum')
    serializer_class =  LogsSerializer
    def get_serializer_class(self):        
        method = self.request.method
        if method =="GET":
            return LogsSerializer
        else:
            return RequestLogsSerializer
    filter_backends = (DjangoFilterBackend,
                       SearchFilter,
                       OrderingFilter,
                       )

    search_fields = ("log_id", "datum", "nachricht","benutzer__anmeldename","benutzer__name","sensor__adresse","sensor__adresse","sensor__hersteller__name")
    ordering_fields =  ("log_id", "datum", "nachricht","benutzer_id", "sensor_id")
    

class SensorsView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset =  Sensors.objects.all()
    serializer_class =  SensorsSerializer
    filter_backends = (DjangoFilterBackend,
                       SearchFilter,
                       OrderingFilter,
                       )

    search_fields = ("sensor_id", "adresse", "serverschrank","max_temp", "hersteller__name")
    ordering_fields = ("sensor_id", "adresse", "serverschrank","max_temp", "hersteller_id")
    

    def perform_update(self, request, *args, **kwargs):
        max_temp = self.request.data.pop("max_temp","")
        sensor = self.queryset.get(sensor_id=self.kwargs["pk"])
        sensor.max_temp = max_temp
        sensor.save()
        
        msg = f"Sensor Max Temperatur Changed to {max_temp}"
        logs = Logs.objects.create(sensor_id=sensor.sensor_id, nachricht=msg,benutzer_id=self.request.user.id)
        logs.save()
        
        
        return Response(SensorsSerializer(sensor).data)

        
    
class HerstellerView(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    queryset =  Hersteller.objects.all()
    serializer_class =  HerstellerSerializer
    
    filter_backends = (DjangoFilterBackend,
                       SearchFilter,
                       OrderingFilter,
                       )

    search_fields = ("hersteller_id", "name")
    ordering_fields = ("hersteller_id", "name")
    

    
    
    
    
    
    
    
    
    
    
    
    