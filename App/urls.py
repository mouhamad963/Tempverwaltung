from django.urls import  include,path
from .views  import BenutzerView,HerstellerView,LogsView,SensorsView,TemperaturenView,AuthView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'benutzer',BenutzerView)
router.register(r'hersteller',HerstellerView)
router.register(r'logs',LogsView)
router.register(r'sensors',SensorsView)
router.register(r'temperaturen',TemperaturenView)

urlpatterns = [
    path(r'', include(router.urls)),
    path('auth/', AuthView.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

]
