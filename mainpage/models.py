from django.db import models

class Category(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    
    img_src = models.ImageField(upload_to='', default=None, null=True, blank=True)
    

    def __str__(self):
        return self.name