from django.contrib import admin

# Register your models here.
from .models import Membre,Article,Facture
admin.site.register(Membre)
admin.site.register(Article)
admin.site.register(Facture)
