from django.shortcuts import render, redirect 
from django.views.generic import TemplateView
from user.views import *

class makepro (TemplateView):
    template_name = "board.html"