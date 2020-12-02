from django.db import models


class Categorie(models.Model):

	nom       = models.CharField(max_length=25, unique=True,verbose_name="Nom de la catégorie")
	desc      = models.CharField(max_length=25, verbose_name="Description de la catégorie")

	def __str__(self):
		return self.nom

class Produit(models.Model):

	nom       = models.CharField(max_length=25, verbose_name="Nom du produit")
	prix      = models.IntegerField(verbose_name="Prix du produit")
	image     = models.FileField(upload_to='images',verbose_name="Image du produit")
	quantite  = models.IntegerField(verbose_name="Quantité du produit")
	categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,verbose_name="Catégorie")

	def __str__(self):
		return self.nom