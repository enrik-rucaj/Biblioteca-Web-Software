from django.shortcuts import render, redirect,get_object_or_404,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Libri, Autori, Editori, Prestiti, Utenti
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from django.core.paginator import Paginator

from .forms import LibriForm, PrestitiForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class PrestitiCreateView(LoginRequiredMixin, CreateView):
    model = Prestiti
    form_class = PrestitiForm
    template_name = 'prenotazioni.html'

    def get_initial(self):
        initial = super().get_initial()
        initial['idlibro'] = get_object_or_404(Libri, idlibro = self.kwargs['idlibro'])
        return initial

    def get_success_url(self):
        return reverse_lazy('libro', kwargs={'idlibro': self.object.idlibro.idlibro})

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
    form_class = LibriForm
    #fields = ['dewey','titolo','isbn','idedi','nedizione','annopubblicazione','prezzo','dataacquisto','descrizione','pagine','idcollocazione','idsede','inprestito','idstato']
    
def detail_view(request, idlibro):
    data = Libri.objects.get(idlibro = idlibro)
    context = {
        'data' : data
    }
    return render(request, "detail_view.html", context)

@login_required
def update_view(request, idlibro):
    
    context = {}
    obj = get_object_or_404(Libri, idlibro = idlibro)
    form = LibriForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+str(idlibro))

    context["form"] = form   

    return render(request, "update_view.html", context)
@login_required
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
