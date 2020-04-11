from django.contrib import admin
from hello_world.models import Libro
from hello_world.models import Autori

# Register your models here.


admin.site.register(Libro)
admin.site.register(Autori)