from django.contrib import admin
from libri.models import Libri, Autori, Autorilibri, Codicedewey, Collocazione, Editori, Scarichi, Sede, Stato, Utenti, Prestiti
# Register your models here.
admin.site.register(Libri)
admin.site.register(Autori)
admin.site.register(Autorilibri)
admin.site.register(Codicedewey)
admin.site.register(Collocazione)
admin.site.register(Editori)
admin.site.register(Prestiti)
admin.site.register(Scarichi)
admin.site.register(Sede)
admin.site.register(Stato)
admin.site.register(Utenti)
