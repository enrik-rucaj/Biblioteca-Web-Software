from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Libri,Autori,Editori
from django.views.generic import ListView


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

class LibriListView(LoginRequiredMixin,ListView):
    queryset=Libri.objects.all()


