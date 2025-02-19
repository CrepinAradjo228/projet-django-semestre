
from django.urls import path
from .views import gestion_produit,index,ajout_produit,ajout_categorie,supprimer_produit,modifier_produit,gestion_produit,ajouter_au_panier,valider_commande,voir_panier,detail_facture,supprimer_du_panier,gestion_facture,detail_commande,gestion_commandes,tableau_de_bord

urlpatterns = [
    path('', index , name = 'home'),
    path('gestion_produit/', gestion_produit, name='gestion_produit'),
    path('ajout_produit/',ajout_produit,name='ajout_produit'),
    path('ajout_categorie/',ajout_categorie,name='ajout_categorie'),
    path('supprimer_produit/<int:id>/', supprimer_produit, name='supprimer_produit'),
    path('modifier_produit/<int:produit_id>/', modifier_produit, name='modifier_produit'),
    path('ajouter-au-panier/<int:produit_id>/',ajouter_au_panier, name='ajouter_au_panier'),
    path('panier/',voir_panier, name='panier'),
    path('valider-commande/', valider_commande, name='valider_commande'),
    path('detail-facture/<int:facture_id>/',detail_facture, name='detail_facture'),
    path('supprimer-du-panier/<int:produit_id>/', supprimer_du_panier, name='supprimer_du_panier'),
    path('gestion-facture/', gestion_facture, name='gestion_facture'),
    path('detail-commande/<int:commande_id>/', detail_commande, name='detail_commande'),
    path('gestion-commandes/', gestion_commandes, name='gestion_commande'),
    path('tableau_de_bord/',tableau_de_bord,name='tableau_de_bord')
]