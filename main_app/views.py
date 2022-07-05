from django.shortcuts import render

# Add the following import 
from django.http import HttpResponse

# Create your views here.
# Home view
def home(request):
    return render(request, 'home.html')

# About view
def about(request):
    return render(request, 'about.html')