from django.contrib import admin
from hello_world.models import Libri
from hello_world.models import Autori

# Register your models here.


admin.site.register(Libri)
admin.site.register(Autori)
