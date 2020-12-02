from django.contrib import admin

from .models import * 

class CategorieAdmin(admin.ModelAdmin):
 	list_display = ('nom','desc')

class ProduitAdmin(admin.ModelAdmin):
 	list_display = ('nom','prix','quantite','categorie')



admin.site.register(Produit,ProduitAdmin)
admin.site.register(Categorie,CategorieAdmin)
