from boutique.views import *
from django.urls import path


urlpatterns = [
    path("",index,name="home"),
    path('updateMagasin/<int:pk>/',
         update_magasin,
         name='updateMagasin'),
    path('updateProfil/<int:pk>/',
         update_profil,
         name='updateProfil'),
    path('updateProduit/<int:pk>/',
         update_produit,
         name='updateProduit')
]
