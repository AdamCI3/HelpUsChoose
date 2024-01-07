from django.http import HttpResponse
from django.shortcuts import render
import random

from api.models import User, Game, Item
from mainpage.models import Category

# Create your views here.

def init(request):
    if 'id' not in request.session:
        new_user = User.objects.create()
        request.session['id'] = new_user.id
        request.session['games'] = {}
        print(request.session['games'])
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
    
    items_list = list(Item.objects.filter(category_id=category))
    
    if len(items_list) <= 0: 
        return HttpResponse("ERR")
    
    new_game = Game.objects.create(
        url="", 
        owner_id=current_user ,
        player_id=current_user,
        category_id=category)
    new_game.url = f"game/{new_game.id}"
    new_game.save()
    
    print(items_list)
    print(new_game.id)
    request.session['games'][str(new_game.id)] = random.choice(items_list).id
    request.session.modified = True
    print(request.session['games'])
    
    return HttpResponse(new_game.id)

def join(request, game_id):
    current_game = Game.objects.get(id=game_id)
    if 'id' not in request.session:
        return HttpResponse("ERR") #user is not authenticated
    
    items_list = list(Item.objects.filter(category_id=current_game.category_id)) 
    if len(items_list) <= 0: 
        return HttpResponse("ERR") # there are no items in this category

    if current_game.player_id != current_game.owner_id:
        return HttpResponse("ERR") #game is locked for other players to join
    
    current_user = User.objects.get(id=request.session['id'])
    if current_user.id == current_game.owner_id:
        return HttpResponse("ERR") #user tries to join its own game
    
    #if current_game.player_id == current_game.owner_id it means that 
    #game is open to other players. Backend will attept to join a player
    
    current_game.player_id = current_user
    current_game.save()
    
    print(game_id)
    request.session['games'][str(game_id)] = random.choice(items_list).id
    request.session.modified = True
    print(request.session['games'])

    return HttpResponse("OK")
