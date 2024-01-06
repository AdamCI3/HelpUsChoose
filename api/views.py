from django.http import HttpResponse
from django.shortcuts import render
import uuid

# Create your views here.

def init(request):
    if 'id' not in request.session:
        request.session['id'] = str(uuid.uuid4())
        return HttpResponse("OK")
    else:
        return HttpResponse("ERR")


def session_check(request):
    id = request.session.get('id', 'Guest')
    return HttpResponse(f"id is, {id}.")