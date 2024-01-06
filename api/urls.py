from django.urls import path

from . import views

urlpatterns = [
    path("init", views.init, name="init"),
    path("session_check", views.session_check, name="session_check"),
]