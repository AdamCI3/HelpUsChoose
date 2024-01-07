from django.urls import path
from django.http import HttpResponse

from . import views

urlpatterns = [
    path("init", views.init, name="init"),
    path("session_check", views.session_check, name="session_check"),
    path(r'new_game/<int:category_id>', views.new_game, name='new game'),
    path(r'join/<int:game_id>', views.join)
]