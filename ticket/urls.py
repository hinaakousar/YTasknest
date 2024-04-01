
from django.urls import path 
from ticket.views import *

urlpatterns = [
    path('project/', start_p.as_view())
]