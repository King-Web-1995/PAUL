from django.shortcuts import render
from .models import *



def liste(request):
	context = {"produits": Produit.objects.all()}
	return render(request, 'page/liste.html',context)

def home(request):
	context = {"produits": Produit.objects.all()[0:6]}
	return render(request, 'page/index.html',context)
	

def creer(request):
	context = {"categories": Categorie.objects.all()}
	return render(request, 'page/creer.html',context)

def categorie(request):
	return render(request, 'page/categorie.html')

def categorieok(request):
	if request.method == 'POST':
		categorie = Categorie()
		data = request.POST
		if len(data)== 3:
			categorie.nom         = data['nom']
			categorie.desc        = data['description']
			categorie.save()
			context = {"produits": Produit.objects.all()}
			return render(request, 'page/index.html',context)
	return render(request, 'page/categorie.html')

def tra_creer(request):
	if request.method == 'POST':
		produit = Produit()
		data = request.POST
		if len(data)== 5:
			produit.nom         = data['nom']
			produit.prix        = data['prix']
			produit.image       = request.FILES['image']
			produit.quantite    = data['quantite']
			produit.categorie   = Categorie.objects.get(nom=data['categorie'])	
			produit.save()
			context = {"produits": Produit.objects.all()}
			return render(request, 'page/index.html',context)
	context = {"categories": Categorie.objects.all()}
	return render(request, 'page/creer.html',context)


def delliste(request):
	context = {"produits": Produit.objects.all()}
	return render(request, 'page/delliste.html',context)


def delsucces(request,id):
	id=int(id)
	print(id)
	produit = Produit.objects.get(id=id)
	produit.delete()
	context = {"produits": Produit.objects.all()[0:6]}
	return render(request, 'page/index.html',context)


def modiliste(request):
	context = {"produits": Produit.objects.all()}
	return render(request, 'page/modiliste.html',context)


def modisucces(request,pk):
	id= int(pk)
	if request.method == 'POST':
		produit = Produit.objects.get(id=id)
		data = request.POST
		if len(data)== 5:
			produit.nom         = data['nom']
			produit.prix        = data['prix']
			produit.image       = request.FILES['image']
			produit.quantite    = data['quantite']
			produit.categorie   = Categorie.objects.get(nom=data['categorie'])	
			produit.save()
			context = {"produits": Produit.objects.all()}
			return render(request, 'page/index.html',context)
	context = {"produits":Produit.objects.get(id=id),"categories": Categorie.objects.all()}
	return render(request, 'page/modisucces.html',context)