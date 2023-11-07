"""
URL configuration for nuestros_4patas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from app_blog.views import mostrar_perritos 
from nuestros_4patas.views import saludar_usuario
from app_blog.views import mostrar_gatitos
from app_blog.views import mostrar_caballos 

urlpatterns = [
    path('admin/', admin.site.urls),
    path("mostrar-animales/", include ("app_blog.urls")),
    path("inicio/", saludar_usuario, name="inicio"),
    
]
