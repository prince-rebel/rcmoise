from django.db import models

# Create your models here.
class Membre(models.Model):


    CHOICES_TYPE = ( 
        ('CLIENT', 'Client'),
        ('FOURNISSEUR', 'Fournisseur'),
        ('CLIENT_ET_FORUNISSEUR', 'Client et Fournisseur'),
       
    )
    name = models.CharField('nom et prenom', max_length=200 ,)
    type_client = models.CharField(max_length=21,choices=CHOICES_TYPE,)
    mobile= models.CharField('nom et prenom',max_length=50,)
    email=models.EmailField(max_length = 254)
    password= models.CharField(max_length=50)
    password_confirm= models.CharField(max_length=50)
    company=models.CharField('Entreprise',max_length=100,)

    def __str__(self):
        template = '{0.name} {0.type_client} {0.mobile}  {0.email} {0.company}'
        return template.format(self)

class Facture(models.Model):
    Num_Fact =models.CharField('N Facture', max_length=200 ,)
    Total =models.FloatField("Total")

    def __str__(self):
    
        template = '{0.Num_Fact} {0.Articles} {0.Total} '
        return template.format(self)

class Article(models.Model):
    designation = models.CharField('Designation', max_length=200 ,)
    qte = models.FloatField("Quantité")
    Prix_unitaire=models.FloatField("Prix U")
    Prix_total=models.FloatField("Prix T")
    # Facture= models.ForeignKey(Facture,on_delete=models.CASCADE) 

    def __str__(self):
        template = '{0.designation} {0.qte} {0.Prix_unitaire} '
        return template.format(self)


