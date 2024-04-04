from django.urls import path 
from list.views import *
from .views import board_view, update_item_position
from django.urls import path
urlpatterns = [
    path('', board_view, name='board'),
    path('update-item-position/', update_item_position, name='update_item_position'),
]
    
