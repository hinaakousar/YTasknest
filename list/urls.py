from django.urls import path 
from list.views import *

urlpatterns = [
    path('land/', home, name='login' ),
    path('make', makepro.as_view())
    
]