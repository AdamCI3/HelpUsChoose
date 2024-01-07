from django.db import models
from mainpage.models import Category

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'User {self.id}'

class Item(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 200)  
    category_id = models.OneToOneField(Category, on_delete=models.CASCADE) 
    # img_src = models.CharField(max_length = 200)   
    img_src = models.ImageField(upload_to='img/', default=None)   
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
class Game(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.CharField(max_length = 200)  
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'Game {self.id} of {self.owner_id}'

class Match(models.Model):
    id = models.AutoField(primary_key=True)
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE)
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)