
from django.urls import path
from .views import gestion_produit,index,ajout_produit,ajout_categorie,supprimer_produit,modifier_produit,gestion_produit,ajouter_au_panier,valider_commande,voir_panier,detail_facture,supprimer_du_panier,gestion_facture,detail_commande,gestion_commandes,tableau_de_bord

urlpatterns = [
    #Chemin vers la vue index ayant pour nom "home"
    path('', index , name = 'home'),

    #Chemin vers la vue gestion_produit ayant pour nom "gestion_produit"
    path('gestion_produit/', gestion_produit, name='gestion_produit'),

    #Chemin vers la vue ajout_produit ayant pour nom "ajout_produit"
    path('ajout_produit/',ajout_produit,name='ajout_produit'),

    #Chemin vers la vue ajout_categorie ayant pour nom "ajout_categorie"
    path('ajout_categorie/',ajout_categorie,name='ajout_categorie'),

    #Chemin vers la vue supprimer_produit ayant pour nom "supprimer_produit"
    path('supprimer_produit/<int:id>/', supprimer_produit, name='supprimer_produit'),

    #Chemin vers la vue modifier_produit ayant pour nom "modifier_produit"
    path('modifier_produit/<int:produit_id>/', modifier_produit, name='modifier_produit'),

    #Chemin vers la vue ajouter_au_panier ayant pour nom "ajouter_au_panier"
    path('ajouter-au-panier/<int:produit_id>/',ajouter_au_panier, name='ajouter_au_panier'),

    #Chemin vers la vue voir_panier ayant pour nom "panier"
    path('panier/',voir_panier, name='panier'),

    #Chemin vers la vue valider_commande ayant pour nom "valider_commande"
    path('valider-commande/', valider_commande, name='valider_commande'),

    #Chemin vers la vue detail_facture ayant pour nom "detail_facture"
    path('detail-facture/<int:facture_id>/',detail_facture, name='detail_facture'),

    #Chemin vers la vue supprimer_du_panier ayant pour nom "supprimer_du_panier"
    path('supprimer-du-panier/<int:produit_id>/', supprimer_du_panier, name='supprimer_du_panier'),

    #Chemin vers la vue gestion_facture ayant pour nom "gestion_facture"
    path('gestion-facture/', gestion_facture, name='gestion_facture'),

    #Chemin vers la vue detail_commande ayant pour nom "detail_commande"
    path('detail-commande/<int:commande_id>/', detail_commande, name='detail_commande'),

    #Chemin vers la vue gestion_commandes ayant pour nom "gestion_commandes"
    path('gestion-commandes/', gestion_commandes, name='gestion_commande'),

    #Chemin vers la vue tableau_de_bord ayant pour nom "tableau_de_bord"
    path('tableau_de_bord/',tableau_de_bord,name='tableau_de_bord')
]