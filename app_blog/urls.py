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
from app_blog.views import PerroListView
from app_blog.views import PerroCreateView
from app_blog.views import PerroDetailView
from app_blog.views import PerroUpdateView
from app_blog.views import PerroDeleteView



urlpatterns = [
    
    #path("perritos/", mostrar_perritos, name="mostrar_perritos"),
    path("gatitos/", mostrar_gatitos, name="mostrar_gatitos"),
    path("caballos/", mostrar_caballos, name="mostrar_caballos"),
    #path("crear-perritos/", crear_perritos, name="crear_perritos"),
    path("crear-gatitos/", crear_gatitos, name="crear_gatitos"),
    path("crear-caballos/", crear_caballos, name="crear_caballos"),
    path("buscar-perritos/", buscar_perrito, name="buscar_perrito"),
    path("buscar-caballos/", buscar_caballo, name="buscar_caballo"),
    path("buscar-gatitos/", buscar_gatito, name="buscar_gatito"),
    #url con listas basadas en clases
    path("perritos/", PerroListView.as_view(), name="mostrar_perritos"),
    path("perritos/<int:pk>/", PerroDetailView.as_view(), name="ver_perritos"),
    path("crear-perritos/", PerroCreateView.as_view(), name="crear_perritos"),
    path("editar-perritos/<int:pk>/", PerroUpdateView.as_view(), name="editar_perritos"),
    path("eliminar-perritos/<int:pk>/", PerroDeleteView.as_view(), name="eliminar_perritos"),
]
