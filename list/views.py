from django.shortcuts import render, redirect 
from django.views.generic import TemplateView
from user.views import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from list.models import Board
from.models import List, Item


def board_view(request):
    boards = Board.objects.all()
    return render(request, 'board.html', {'boards' : boards})


@csrf_exempt
def update_item_position(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data['new_list_id']

        item = Item.objects.get(pk=item_id)
        item.list_id = new_list_id
        item.save()

        return JsonResponse({'success' : True})
    return JsonResponse({'success' : False})
