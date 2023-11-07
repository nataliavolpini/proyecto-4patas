from django.contrib import admin
from django.urls import path

from app_blog.views import mostrar_perritos
from app_blog.views import mostrar_gatitos
from app_blog.views import mostrar_caballos
from app_blog.views import crear_perritos
from app_blog.views import crear_gatitos
from app_blog.views import crear_caballos
from app_blog.views import buscar_perrito
from app_blog.views import buscar_gatito
from app_blog.views import buscar_caballo


urlpatterns = [
    
    path("perritos/", mostrar_perritos, name="mostrar_perritos"),
    path("gatitos/", mostrar_gatitos, name="mostrar_gatitos"),
    path("caballos/", mostrar_caballos, name="mostrar_caballos"),
    path("crear-perritos/", crear_perritos, name="crear_perritos"),
    path("crear-gatitos/", crear_gatitos, name="crear_gatitos"),
    path("crear-caballos/", crear_caballos, name="crear_caballos"),
    path("buscar-perritos/", buscar_perrito, name="buscar_perrito"),
    path("buscar-caballos/", buscar_caballo, name="buscar_caballo"),
    path("buscar-gatitos/", buscar_gatito, name="buscar_gatito"),
]
