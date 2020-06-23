
from django.urls import  include,path

from django.contrib import admin
from django.urls import path, reverse_lazy


  
urlpatterns = [
   # path('login/', admin.site.urls),

    path('', include('App.urls')),
    path('admin/', admin.site.urls),


]
