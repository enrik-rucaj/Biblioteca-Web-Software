from django.utils import timezone
from django.urls import reverse_lazy
from django.db.models import  IntegerField, Q 
from django.db.models.functions import Cast, Substr
from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from .models import Libri, Autori, Editori, Prestiti, Utenti, Autorilibri
from .forms import LibriForm, ApriPrestitiForm, ChiudiPrestitiForm, LibroInPrestitoForm, AutoriLibriForm

# Create your views here.
class ApriPrestitiCreateView(LoginRequiredMixin, CreateView):
    def get(self, request, *args, **kwargs):
        obj = Libri.objects.get(idlibro = self.kwargs['idlibro'])
        form1 = LibroInPrestitoForm(instance = obj, initial = {'inprestito': True})
        form2 = ApriPrestitiForm(initial = {'idlibro': obj})

        context = {'form1': form1, 'form2': form2}
        return render(request, 'prenotazioni.html', context)

    def post(self, request, *args, **kwargs):
        obj = Libri.objects.get(idlibro = self.kwargs['idlibro'])
        form1 = LibroInPrestitoForm(request.POST, instance = obj, initial = {'inprestito': True})
        form2 = ApriPrestitiForm(request.POST, initial = {'idlibro': obj})
        if form1.is_valid() and form2.is_valid():
            book1 = form1.save()
            book2 = form2.save()
            book1.save()
            book2.save()
            return HttpResponseRedirect(reverse_lazy('libro', kwargs={'idlibro': self.kwargs['idlibro']}))
        return render(request, 'prenotazioni.html', {'form1': form1, 'form2': form2})

class ChiudiPrestitiCreateView(LoginRequiredMixin, UpdateView):
    def get(self, request, *args, **kwargs):
        obj = Libri.objects.get(idlibro = self.kwargs['idlibro'])
        obj2 = Prestiti.objects.get(idlibro = obj, datarestituzione = None)
        form1 = LibroInPrestitoForm(instance = obj, initial = {'inprestito': False})
        form2 = ChiudiPrestitiForm(instance = obj2, initial = {'datarestituzione': timezone.now()})

        context = {'form1': form1, 'form2': form2}
        return render(request, 'disprenotazioni.html', context)

    def post(self, request, *args, **kwargs):
        obj = Libri.objects.get(idlibro = self.kwargs['idlibro'])
        obj2 = Prestiti.objects.get(idlibro = obj, datarestituzione = None)
        form1 = LibroInPrestitoForm(request.POST, instance = obj, initial = {'inprestito': False})
        form2 = ChiudiPrestitiForm(request.POST, instance = obj2)
        if form1.is_valid() and form2.is_valid():
            book1 = form1.save()
            book2 = form2.save()
            book1.save()
            book2.save()
            return HttpResponseRedirect(reverse_lazy('libro', kwargs={'idlibro': self.kwargs['idlibro']}))
        return render(request, 'disprenotazioni.html', {'form1': form1, 'form2': form2})

class LibriListView(LoginRequiredMixin, ListView):
    #queryset = Libri.objects.all()
    paginate_by=25
    def get_queryset(self):
        # idAutori=Autori.objects.filter(cognomenome = self.request.GET.get("search_box", "")).values_list('idautore', flat=True)
        # idlibro=Autorilibri.objects.filter(idautore = idAutori).values_list('idlibro', flat = True)
        return Libri.objects.filter(Q(titolo__icontains=self.request.GET.get("search_box", ""))|Q(isbn__icontains = self.request.GET.get("search_box", "")))

class LibriCreateView(LoginRequiredMixin, CreateView):
    model = Libri
    form_class = LibriForm
    template_name = 'libri/libri_create_form.html'

    def get_success_url(self):
        return reverse_lazy('autoriLibri', kwargs={'idlibro': Libri.objects.latest('idlibro').idlibro})
        #return reverse_lazy('libro', kwargs={'idlibro': Libri.objects.latest('idlibro').idlibro})

class AutoriLibriCreateView(LoginRequiredMixin, CreateView):
#    model = Autorilibri
#    form_class = AutoriLibriForm
#    template_name = 'libri/autoriLibri_create_form.html'

    def get(self, request, *args, **kwargs):
        obj = Libri.objects.get(idlibro = self.kwargs['idlibro'])
        form1 = AutoriLibriForm(initial = {'idlibro': obj})
        context = {'form': form1}
        return render(request, 'libri/autoriLibri_create_form.html', context)

    def post(self, request, *args, **kwargs):
        obj = Libri.objects.get(idlibro = self.kwargs['idlibro'])
        form1 = AutoriLibriForm(request.POST, initial = {'idlibro': obj})
        if form1.is_valid():
            book1 = form1.save()
            book1.save()
            return HttpResponseRedirect(reverse_lazy('autoriLibri', kwargs={'idlibro': self.kwargs['idlibro']}))
        return render(request, 'libri/autoriLibri_create_form.html', {'form': form1})
        #return HttpResponseRedirect(reverse_lazy('libro', kwargs={'idlibro': self.kwargs['idlibro']}))

#    def get_success_url(self):
#       return reverse_lazy('home')

class LibriUpdateView(LoginRequiredMixin, UpdateView):
    model = Libri
    form_class = LibriForm
    template_name = 'libri/libri_update_form.html'

    def get_success_url(self):
        return reverse_lazy('libro', kwargs={'idlibro': self.kwargs['idlibro']})

    def get_object(self):
        idlibro = self.kwargs.get("idlibro")
        return get_object_or_404(Libri, idlibro = idlibro)

class LibriDeleteView(LoginRequiredMixin, DeleteView):
    model = Libri
    template_name = 'libri/libri_delete_form.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        idlibro = self.kwargs.get("idlibro")
        return get_object_or_404(Libri, idlibro = idlibro)

class LibriDetailView(DetailView):
    model = Libri
    template_name = 'libri/libri_detail_form.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['data'] = Libri.objects.get(idlibro = self.kwargs.get("idlibro"))
        return context

    def get_object(self):
        idlibro = self.kwargs.get("idlibro")
        return get_object_or_404(Libri, idlibro = idlibro)

class HomeView(ListView):
    paginate_by = 25
    model = Libri
    template_name = 'home.html'
    def get_queryset(self):
        return Libri.objects.filter(titolo__icontains=self.request.GET.get("Search", ""))
    def get_context_data(self, **kwargs):
         context = super(HomeView, self).get_context_data(**kwargs)
         context['nuovi_arrivi'] = Libri.objects.order_by('-idlibro')[:9][::-1]
         return context
class InfoListView(ListView):
    paginate_by = 25
    model = Libri
    template_name = 'secret.html'
    
    def get_queryset(self):
        return Libri.objects.annotate(
            part=Cast(Substr("dewey", 1,3), IntegerField())
        ).filter(part__lte = 99)

class FiloListView(ListView):
    paginate_by = 25 
    model = Libri
    template_name = 'secret.html'
    def get_queryset(self):
        return Libri.objects.annotate(
            part=Cast(Substr("dewey",1,3), IntegerField())
        ).filter(Q(part__lte = 199 )& Q(part__gte= 100))
class ReligioneListView(ListView):
    paginate_by = 25
    model = Libri
    template_name = 'secret.html'
    def get_queryset(self):
        return Libri.objects.annotate(
            part=Cast(Substr("dewey",1,3), IntegerField())
        ).filter(Q(part__lte = 299 )& Q(part__gte= 200))
class ScieSocListView(ListView):
    paginate_by = 25 
    model = Libri
    template_name = 'secret.html'
    def get_queryset(self):
        return Libri.objects.annotate(
            part=Cast(Substr("dewey",1,3), IntegerField())
        ).filter(Q(part__lte = 399 )& Q(part__gte= 300))
class LinguisticaListView(ListView):
    paginate_by = 25
    model = Libri 
    template_name = 'secret.html'
    def get_queryset(self):
        return Libri.objects.annotate(
            part=Cast(Substr("dewey",1,3), IntegerField())
        ).filter(Q(part__lte = 499 )& Q(part__gte= 400))
class ScienzePureListView(ListView):
    paginate_by = 25
    model = Libri 
    template_name = 'secret.html'
    def get_queryset(self):
        return Libri.objects.annotate(
            part=Cast(Substr("dewey",1,3), IntegerField())
        ).filter(Q(part__lte = 599 )& Q(part__gte= 500))
class TecnologiaListView(ListView):
    paginate_by = 25
    model = Libri 
    template_name = 'secret.html'
    def get_queryset(self):
        return Libri.objects.annotate(
            part=Cast(Substr("dewey",1,3), IntegerField())
        ).filter(Q(part__lte = 699 )& Q(part__gte= 600))
class ArtiListView(ListView):
    paginate_by = 25
    model = Libri 
    template_name = 'secret.html'
    def get_queryset(self):
        return Libri.objects.annotate(
            part=Cast(Substr("dewey",1,3), IntegerField())
        ).filter(Q(part__lte = 799 )& Q(part__gte= 700))
class LetteraturaListView(ListView):
    paginate_by = 25
    model = Libri 
    template_name = 'secret.html'
    def get_queryset(self):
        return Libri.objects.annotate(
            part=Cast(Substr("dewey",1,3), IntegerField())
        ).filter(Q(part__lte = 899 )& Q(part__gte= 800))
class GeoStoListView(ListView):
    paginate_by = 25
    model = Libri 
    template_name = 'secret.html'
    def get_queryset(self):
        return Libri.objects.annotate(
            part=Cast(Substr("dewey",1,3), IntegerField())
        ).filter(Q(part__lte = 999 )& Q(part__gte= 900))