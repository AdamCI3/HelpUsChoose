from django.contrib import admin
from .models import User, Item, Game, Match

# Register your models here.

admin.site.register(User)
admin.site.register(Item)
admin.site.register(Game)
admin.site.register(Match)