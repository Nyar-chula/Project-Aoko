
from django.shortcuts import render

def home_view(request):
    return render(request, 'amyres_webapp/home.html')

def background_view(request):
    return render(request, 'amyres_webapp/background.html')

def about_view(request):
    return render(request, 'amyres_webapp/about.html')

def team_view(request):
    return render(request, 'amyres_webapp/team.html')

def news_view(request):
    return render(request, 'amyres_webapp/news.html')

def products_view(request):
    return render(request, 'amyres_webapp/products.html')

# products page login views #

from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import CustomLoginForm  # Import CustomLoginForm

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('products')
    else:
        form = CustomLoginForm()
    return render(request, 'amyres_webapp/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'amyres_webapp/signup.html', {'form': form})

@login_required
def products_view(request):
    return render(request, 'amyres_webapp/products.html')

# products_download views #

from django.http import FileResponse
import os

@login_required
def download_file(request):
    file_path = os.path.join('amyres_webapp/files', 'file1.zip')
    return FileResponse(open(file_path, 'rb'), as_attachment=True)

