from django.shortcuts import render, redirect 
from django.views.generic import TemplateView
from user.views import *

def home (request):
    return render(request, 'home.html')

class makepro (TemplateView):
    template_name = "board.html"