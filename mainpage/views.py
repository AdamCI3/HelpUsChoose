from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from django.template import loader
from django.shortcuts import render

def index(request):
    categories_list= Category.objects.all()
    output=", ".join([c.name for c in categories_list])
    template = loader.get_template("mainpage/index.html")
    context = {
        "categories_list": categories_list,
    }
    return HttpResponse(render(request,"mainpage/index.html",context))