from django.shortcuts import render, redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Libri, Autori, Editori
from django.views.generic import ListView, CreateView
from django.core.paginator import Paginator

from .forms import LibriForm
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def home(request):
    count = User.objects.count()
    return render(request,'home.html',{
        'count' : count
    })

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

class LibriListView(LoginRequiredMixin, ListView):
    queryset = Libri.objects.all()
    paginate_by=25

class LibriCreateView(LoginRequiredMixin, CreateView):
    model = Libri
    fields = ['dewey','titolo','isbn','idedi','nedizione','annopubblicazione','prezzo','dataacquisto','descrizione','pagine','idcollocazione','idsede','inprestito','idstato']
    success_url = "/"

def detail_view(request, idlibro):
    context = {}

    context["data"] = Libri.objects.get(idlibro = idlibro)
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

def search_view(request):
    query = request.GET.get("search_box", None)
    qs = Libri.objects.all()
    if query is not None:
        
        qs = qs.filter(titolo__icontains=query)
    context = {
        "libri_list": qs,
    }
    template= 'libri/search.html'   
    return render(request, template, context)

    
