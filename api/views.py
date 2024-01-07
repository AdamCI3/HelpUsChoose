from django.http import HttpResponse
from django.shortcuts import render
import uuid

from api.models import User, Game
from mainpage.models import Category

# Create your views here.

def init(request):
    if 'id' not in request.session:
        new_user = User.objects.create()
        request.session['id'] = new_user.id
        return HttpResponse("OK")
    else:
        return HttpResponse("ERR")

def session_check(request):
    id = request.session.get('id', 'Guest')
    return HttpResponse(f"id is, {id}.")

def new_game(request, category_id):
    if 'id' not in request.session:
        return HttpResponse("ERR")
    
    print(category_id)
    
    current_user = User.objects.get(id=request.session['id'])
    category = Category.objects.get(id=category_id)
    
    new_game = Game.objects.create(
        url="", 
        owner_id=current_user ,
        category_id=category)
    new_game.url = f"game/{new_game.id}"
    new_game.save()
    
    return HttpResponse(new_game.id)