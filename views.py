from django.shortcuts import render, redirect

# Create your views here.
# django.shortcuts
from django.contrib.auth.forms import UserCreationForm
from .models import Userprofile

def signup(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            # userprofile = Userprofile.objects.create(user=user)
            Userprofile.objects.create(user=user)

            return redirect('/log-in/')
    form = UserCreationForm()

    return render(request, 'userprofile/signup.html', {
        'form': form
    })

def login(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            # userprofile = Userprofile.objects.create(user=user)
            Userprofile.objects.create(user=user)

            return redirect('/log-in/')
    form = UserCreationForm()

    return render(request, 'userprofile/signup.html', {
        'form': form
    })