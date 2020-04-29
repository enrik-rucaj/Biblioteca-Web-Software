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
from libri.models import Editori
from libri import views
from libri.views import LibriListView, LibriCreateView
from libri.views import update_view, detail_view, delete_view
urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('secret/', views.LibriListView.as_view(), name='libri'),
    path('admin/', admin.site.urls),
    path('aggiungi/', LibriCreateView.as_view(),name='aggiungi' ),
    path('<idlibro>/', detail_view , name= 'libro'),
    path('<idlibro>/update', update_view, name= 'aggiorna'),
    path('<idlibro>/delete', delete_view, name='cancella')
]
