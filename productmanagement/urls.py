from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('creer', views.creer, name='creer'),
    path('liste', views.liste, name='liste'),
    path('delliste', views.delliste, name='delliste'),
    path('delsucces/<int:id>', views.delsucces, name='delsucces'),
    path('modiliste', views.modiliste, name='modiliste'),
    path('modisucces/<int:pk>', views.modisucces, name='modisucces'),
    path('tra_creer', views.tra_creer, name='tra_creer'),
    path('categorie', views.categorie, name='categorie'),
    path('categorieok', views.categorieok, name='categorieok'),

]