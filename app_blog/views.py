from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
#Importo para las clases
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.
from .models import Perro
from .models import Gato
from .models import Caballo
from app_blog.forms import PerroFormulario, GatoFormulario, CaballoFormulario

def mostrar_perritos(request):
    # Traemos todos los datos guardados en la base de datos
    perritos = Perro.objects.all()
    # Enviamos esos datos al archivo html por el contexto
    return render(request, 'listar_perritos.html', {"perritos": perritos})

#No usaremos crear_perritos
def crear_perritos(request):
    if request.method == "POST":
        formulario = PerroFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            raza = data["raza"]
            fecha_nacimiento = data["fecha_nacimiento"]
            descripcion = data["descripcion"]
            perro = Perro(nombre=nombre, raza=raza, fecha_nacimiento=fecha_nacimiento, descripcion=descripcion)  # lo crean solo en RAM
            perro.save()  # Lo guardan en la Base de datos

        # Redirecciono al usuario a la lista de perritos
            url_exitosa = reverse('crear_perritos')  
            return redirect(url_exitosa)
    else:  # GET
        formulario = PerroFormulario()
    http_response = render(
        request=request,
        template_name='formulario_perro.html',
        context={'formulario': formulario}
    )
    return http_response

def mostrar_gatitos(request):
    # Traemos todos los datos guardados en la base de datos
    gatitos = Gato.objects.all()
    # Enviamos esos datos al archivo html por el contexto
    return render(request, 'listar_gatitos.html', {"gatitos": gatitos})

def crear_gatitos(request):
    if request.method == "POST":
        formulario = GatoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            color = data["color"]
            fecha_nacimiento = data["fecha_nacimiento"]
            descripcion = data["descripcion"]
            gato = Gato(nombre=nombre, color=color, fecha_nacimiento=fecha_nacimiento, descripcion=descripcion)  # lo crean solo en RAM
            gato.save()  # Lo guardan en la Base de datos

        # Redirecciono al usuario a la lista de gatitos
            url_exitosa = reverse('crear_gatitos')  
            return redirect(url_exitosa)
    else:  # GET
        formulario = GatoFormulario()
    http_response = render(
        request=request,
        template_name='formulario_gato.html',
        context={'formulario': formulario}
    )
    return http_response

def mostrar_caballos(request):
    # Traemos todos los datos guardados en la base de datos
    caballos = Caballo.objects.all()
    # Enviamos esos datos al archivo html por el contexto
    return render(request, 'listar_caballos.html', {"caballos": caballos})

def crear_caballos(request):
    if request.method == "POST":
        formulario = CaballoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            color = data["color"]
            fecha_nacimiento = data["fecha_nacimiento"]
            caballo = Caballo(nombre=nombre, color=color, fecha_nacimiento=fecha_nacimiento)  # lo crean solo en RAM
            caballo.save()  # Lo guardan en la Base de datos

        # Redirecciono al usuario a la lista de caballos
            url_exitosa = reverse('crear_caballos') 
            return redirect(url_exitosa)
    else:  # GET
        formulario = CaballoFormulario()
    http_response = render(
        request=request,
        template_name='formulario_caballo.html',
        context={'formulario': formulario}
    )
    return http_response 

def buscar_perrito(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        #perritos = Perro.objects.filter(nombre__icontains=busqueda)
        # Ejemplo filtro avanzado
        perritos = Perro.objects.filter(
            Q(nombre__icontains=busqueda) | Q(raza__contains=busqueda)
        )

        contexto = {
            "perritos": perritos,
        }
        http_response = render(
            request=request,
            template_name='listar_perritos.html',
            context=contexto,
        )
        return http_response
    
def buscar_gatito(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        gatitos = Gato.objects.filter(nombre__icontains=busqueda)

        contexto = {
            "gatitos": gatitos,
        }
        http_response = render(
            request=request,
            template_name='listar_gatitos.html',
            context=contexto,
        )
        return http_response

def buscar_caballo(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        caballos = Caballo.objects.filter(nombre__icontains=busqueda)


        contexto = {
            "caballos": caballos,
        }
        http_response = render(
            request=request,
            template_name='listar_caballos.html',
            context=contexto,
        )
        return http_response          


# Vistas de Perritos(basadas en clases)
class PerroListView(ListView):
    model = Perro
    template_name = 'listar_perritos.html'

class PerroCreateView(CreateView):
    model = Perro
    fields = ('nombre', 'raza', 'fecha_nacimiento', 'descripción')
    success_url = reverse_lazy('listar_perritos')


class PerroDetailView(DetailView):
    model = Perro
    success_url = reverse_lazy('listar_perritos')


class PerroUpdateView(UpdateView):
    model = Perro
    fields = ('nombre', 'raza', 'fecha_nacimiento', 'descripción')
    success_url = reverse_lazy('listar_perritos')


class PerroDeleteView(DeleteView):
    model = Perro
    success_url = reverse_lazy('listar_perritos')    