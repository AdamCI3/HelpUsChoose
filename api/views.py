from django.http import HttpResponse
from django.shortcuts import render
import random
import json

from api.models import User, Game, Item
from mainpage.models import Category

# Create your views here.

def init(request):
    if 'id' not in request.session:
        new_user = User.objects.create()
        request.session['id'] = new_user.id
        request.session['games'] = {}
        request.session['queues'] = {}
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
    current_user = User.objects.get(id=request.session['id'])
    
    category_list = list(Category.objects.filter(id=category_id)) 
    if len(category_list) <= 0: 
        return HttpResponse("ERR")
    category = Category.objects.get(id=category_id) # there are no categories with this category_id
    
    items_list = list(Item.objects.filter(category_id=category)) 
    if len(items_list) <= 0: 
        return HttpResponse("ERR") # there are no items in this category
    
    new_game = Game.objects.create(
        url="", 
        owner_id=current_user ,
        player_id=current_user,
        category_id=category)
    new_game.url = f"game/{new_game.id}"
    new_game.save()

    request.session['games'][str(new_game.id)] = random.choice(items_list).id
    request.session['queues'][str(new_game.id)] = []
    request.session.modified = True
    
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
    
    request.session['games'][str(game_id)] = random.choice(items_list).id
    request.session['queues'][str(game_id)] = []
    request.session.modified = True

    return HttpResponse("OK")

def next(request, game_id, move):
    # This function should return next move
    # Every time this api enpoint is called it
    # should run logic to calculate matches
    #
    # ARGUMENT game_id: 
    # int - game_id
    #
    # ARGUMENT move: 
    # str - left - Left
    # str - right - Right
    #
    # RETURN:
    # INSTANCE OF ITEM
    
    if 'id' not in request.session:
        return HttpResponse("ERR1")
    current_user = User.objects.get(id=request.session['id'])
    
    game_list = list(Game.objects.filter(id=game_id)) 
    if len(game_list) <= 0: 
        return HttpResponse("ERR2")
    game = Game.objects.get(id=game_id) # there are no games with this game_id
    
    if game.owner_id != current_user and game.player_id != current_user:
        return HttpResponse("ERR3") # user has no permission to make moves in this game
    
    category_id = game.category_id.id
    category_list = list(Category.objects.filter(id=category_id)) 
    if len(category_list) <= 0: 
        return HttpResponse("ERR4")
    category = Category.objects.get(id=category_id) # there are no categories with this category_id
    
    items_list = list(Item.objects.filter(category_id=category)) 
    if len(items_list) <= 0: 
        return HttpResponse("ERR5") # there are no items in this category
    
    next_item: Item = {}
    print(request.session['queues'])
    if len(request.session['queues'][str(game_id)]) != 0:
        next_item_id = request.session['queues'][str(game_id)][0]
        request.session['queues'][str(game_id)].pop(0)
        next_item = Item.objects.get(id=next_item_id)
    else: 
        next_item = random.choice(items_list)
    
    # TO DO:
    # Change next item if move == 'right'
    
    request.session.modified = True
    
    response = {
        "id": next_item.id,
        "name": next_item.name
    }
    print(response)
    return HttpResponse(json.dumps(response))
