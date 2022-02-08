from re import template
from django.shortcuts import get_object_or_404, redirect, render
from django.template import context

from boutique.models import *
from boutique.forms import *
from django.contrib import messages
# Create your views here.

def index(request,*args, **kwargs):
    template_name = "index.html"
    magasins = Magasin.objects.all()
    profils = ProfilMagasin.objects.all()
    produits = Produit.objects.all()
    context = {
        'magasins' : magasins,
        'profils' : profils,
        'produits' : produits
               }
    return render(request=request, template_name=template_name, context=context)

# Update magasin
def update_magasin(request,*args, **kwargs):
    template_name = 'update-magasin.html'
    obj = get_object_or_404(Magasin, pk = kwargs.get('pk'))
    if request.method == 'GET':
        form = MagasinForm(initial={
            'name' : obj.name,
            'country' : obj.country,
        })
        
        context = {'form':form}
    
        return render(
            request=request,
            template_name=template_name,
            context=context
        )
    if request.method == 'POST':
        form = MagasinForm(
            request.POST,
            request.FILES,
            initial={
                'name' : obj.name,
                'country' : obj.country,
            }
        )
        
        context = {'form':form}
    
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.country = form.cleaned_data.get('country')
            obj.created_at = form.cleaned_data.get('created_at')
            obj.updated_at = form.cleaned_data.get('updated_at')
            obj.save()
            redirect('home')
        return render(
                request=request,
                template_name=template_name,
                context=context
            )
# update profil
def update_profil(request,*args, **kwargs):
    template_name = 'update-profil.html'
    obj = get_object_or_404(ProfilMagasin, pk = kwargs.get('pk'))
    if request.method == 'GET':
        form = ProfilForm(initial={
            'email' : obj.email,
            'phone' : obj.phone,
        })
        
        context = {'form':form}
    
        return render(
            request=request,
            template_name=template_name,
            context=context
        )
    if request.method == 'POST':
        form = ProfilForm(
            request.POST,
            request.FILES,
            initial={
            'email' : obj.email,
            'phone' : obj.phone,
            }
        )
        
        context = {'form':form}
    
        if form.is_valid():
            print(form.cleaned_data)
            obj.email = form.cleaned_data.get('email')
            obj.phone = form.cleaned_data.get('phone')
            obj.created_at = form.cleaned_data.get('created_at')
            obj.updated_at = form.cleaned_data.get('updated_at')
            obj.save()
            redirect('home')
        return render(
                request=request,
                template_name=template_name,
                context=context
            )   
        
# Update Produit         
def update_produit(request,*args, **kwargs):
    template_name = 'update-produit.html'
    obj = get_object_or_404(Produit, pk = kwargs.get('pk'))
    if request.method == 'GET':
        form = ProduitForm(initial={
            'name' : obj.name,
            'country' : obj.country,
            'price' : obj.price,
            'image' : obj.image,
        })
        
        context = {'form':form}
    
        return render(
            request=request,
            template_name=template_name,
            context=context
        )
    if request.method == 'POST':
        form = ProduitForm(
            request.POST,
            request.FILES,
            initial={
                'name' : obj.name,
                'country' : obj.country,
                'price' : obj.price,
                'image' : obj.image,
            }
        )
        
        context = {'form':form}
    
        if form.is_valid():
            print(form.cleaned_data)
            obj.name = form.cleaned_data.get('name')
            obj.country = form.cleaned_data.get('country')
            obj.price = form.cleaned_data.get('price')
            obj.image = form.cleaned_data.get('image')
            obj.created_at = form.cleaned_data.get('created_at')
            obj.updated_at = form.cleaned_data.get('updated_at')
            obj.save()
            redirect('home')
        return render(
                request=request,
                template_name=template_name,
                context=context
            )
    
