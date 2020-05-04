from django.shortcuts import render, redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Libri, Autori, Editori, Prestiti
from django.views.generic import ListView, CreateView
from django.core.paginator import Paginator

from .forms import LibriForm, PrenotaLibroForm, PrestitoLibroForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserCreationForm()
    return render(request, 'registration/signup.html', {   
        'form' : form
    })

def book_view(request, idlibro):
    context = {}
    obj = get_object_or_404(Libri, idlibro = idlibro)
    #form1 = PrenotaLibroForm(request.POST or None, instance = obj, initial={ "inprestito" : "true" })
    form2 = PrestitoLibroForm(request.POST or None, instance = obj)

    if form2.is_valid():
        #form1.save()
        form2.save()
        #form1 = PrenotaLibroForm()
        form2 = PrestitoLibroForm()
        return HttpResponseRedirect("/"+str(idlibro))

    #context["form1"] = form1
    context["form2"] = form2
    return render(request, "prenotazioni.html", context)

class LibriListView(LoginRequiredMixin, ListView):
    queryset = Libri.objects.all()
    paginate_by=25

class LibriCreateView(LoginRequiredMixin, CreateView):
    model = Libri
    fields = ['dewey','titolo','isbn','idedi','nedizione','annopubblicazione','prezzo','dataacquisto','descrizione','pagine','idcollocazione','idsede','inprestito','idstato']
    success_url = "/"

def detail_view(request, idlibro):
    data = Libri.objects.get(idlibro = idlibro)
    context = {
        'data' : data
    }
    return render(request, "detail_view.html", context)

def update_view(request, idlibro):
    
    context = {}
    obj = get_object_or_404(Libri, idlibro = idlibro)
    form = LibriForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+idlibro)

    context["form"] = form   

    return render(request, "update_view.html", context)

def delete_view(request, idlibro):

    context = {}

    obj = get_object_or_404(Libri, idlibro = idlibro)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, "delete_view.html", context)
class SearchListView(ListView):
    paginate_by = 25
    model = Libri
    template_name = 'home.html'

    def get_queryset(self):
        return Libri.objects.filter(titolo__icontains=self.request.GET.get("search_box", ""))
