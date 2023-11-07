from django.contrib import admin

# Register your models here.
from app_blog.models import Perro, Gato, Caballo

admin.site.register(Perro)
admin.site.register(Gato)
admin.site.register(Caballo)