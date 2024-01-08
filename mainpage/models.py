from django.db import models

class Category(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.TextField()
    img_src = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name