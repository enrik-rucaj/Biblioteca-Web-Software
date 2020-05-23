"""Biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls.static import static
from Biblioteca import settings
from libri.models import Editori
from libri.views import (LibriListView, LibriCreateView, LibriUpdateView, LibriDeleteView, LibriDetailView, 
                        HomeView, ApriPrestitiCreateView, ChiudiPrestitiCreateView, AutoriLibriCreateView,
                        LibriNonConsegnatiView,
                        InfoListView, FiloListView, ReligioneListView, ScieSocListView, LinguisticaListView, 
                        ScienzePureListView, TecnologiaListView, ArtiListView, LetteraturaListView, 
                        GeoStoListView)

urlpatterns = [
    path('', HomeView.as_view(), name = 'home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('select2/', include('django_select2.urls')),
    path('secret/', LibriListView.as_view(), name = 'libri'),
    path('admin/', admin.site.urls),
    path('aggiungi/', LibriCreateView.as_view(),name = 'aggiungi' ),
    path('<int:idlibro>/', LibriDetailView.as_view(), name = 'libro'),
    path('<int:idlibro>/update', LibriUpdateView.as_view(), name = 'aggiorna'),
    path('<int:idlibro>/delete', LibriDeleteView.as_view(), name ='cancella'),
    path('<int:idlibro>/prenota', ApriPrestitiCreateView.as_view(), name = 'prenota'),
    path('<int:idlibro>/disprenota', ChiudiPrestitiCreateView.as_view(), name = 'disprenota'),
    path('aggiungi/<int:idlibro>/autorelibro/', AutoriLibriCreateView.as_view(), name = 'autoriLibri'),
    path('da_consegnare/', LibriNonConsegnatiView.as_view(), name = 'daConsegnare'),
    
    path('informatica',InfoListView.as_view(), name = 'info'),
    path('filosofia', FiloListView.as_view(), name = 'filo'),
    path('religione', ReligioneListView.as_view(), name = 'rel'),
    path('ScienzeSociali', ScieSocListView.as_view(), name = 'ss'),
    path('linguistica', LinguisticaListView.as_view(), name = 'ling'),
    path('ScienzePure', ScienzePureListView.as_view(), name = 'sp'),
    path('tecnologia', TecnologiaListView.as_view(), name = 'tech'),
    path('arti', ArtiListView.as_view(), name = 'art'),
    path('letteratura', LetteraturaListView.as_view(), name = 'lett'),
    path('geografiastoria', GeoStoListView.as_view(), name = 'geosto'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
