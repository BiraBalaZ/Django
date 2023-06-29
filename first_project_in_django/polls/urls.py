from django.urls import path

#Abaixo, ele importa do diretório atual o arquivo "views.py"
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    #path("", views.login, name="login"),
    #path("", views.start_page, name="home"),
]