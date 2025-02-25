from django.db import models

# Create your models here.

#Déclaration de la classe catégorie
class Categorie(models.Model):
    nom = models.CharField(max_length=100)
    date_ajout = models.DateTimeField(auto_now=True)
    #Fonction d'affichage
    def __str__(self):
        return self.nom



#Déclaration de la classe Client
class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()

    #Fonction d'affichage
    def __str__(self):
        return self.nom
    

#Déclaration de la classe Produit
class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.IntegerField()
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)

    #Fonction d'affichage
    def __str__(self):
        return self.nom
    


#Déclaration de la classe commande  
class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    date_commande = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)

    #Fonction d'affichage
    def __str__(self):
        return f"Commande {self.id}"
    


#Déclaration de la classe LigneCommande
class LigneCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)


    #Fonction d'affichage
    def __str__(self):
        return f"{self.quantite} x {self.produit.nom}"
    


#Déclaration de la classe facture
class Facture(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE)
    date_facture = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    #Fonction d'affichage
    def __str__(self):
        return f"Facture {self.id} pour la commande {self.commande.id}"