🔗 API - Documentation des Endpoints et Routes

📋 Table des Matières

1.
Vue d'Ensemble

2.
Authentification

3.
Endpoints Produits

4.
Endpoints Factures

5.
Endpoints Rapports

6.
Endpoints Alertes

7.
Endpoints Archivage

8.
Endpoints Admin




🎯 Vue d'Ensemble

Base URL

Plain Text


http://localhost:8000/



Format des Réponses

•
HTML : Pages web rendues

•
JSON : (optionnel ) Données structurées

Authentification

Toutes les routes (sauf login) nécessitent une authentification.




🔐 Authentification

Login

Route :

Plain Text


GET/POST /login/



Méthode : POST

Paramètres :

JSON


{
  "username": "admin",
  "password": "admin123"
}



Réponse :

Plain Text


Redirection vers /
(Cookie de session créé)






Logout

Route :

Plain Text


GET /logout/



Réponse :

Plain Text


Redirection vers /login/
(Session détruite)






Vérifier l'Authentification

Dans le Template :

HTML


{% if user.is_authenticated %}
  <p>Bienvenue {{ user.username }}</p>
{% else %}
  <p>Veuillez vous connecter</p>
{% endif %}






📦 Endpoints Produits

1. Liste des Produits

Route :

Plain Text


GET /products/



Paramètres :

Plain Text


?page=1          # Numéro de page (défaut: 1)
?search=café     # Recherche par nom
?min_price=10    # Prix minimum
?max_price=50    # Prix maximum



Réponse :

HTML


Page HTML avec liste paginée des produits



Exemple :

Plain Text


GET /products/?page=1&search=café






2. Détail d'un Produit

Route :

Plain Text


GET /products/<id>/



Paramètres :

Plain Text


<id>  # ID du produit (entier)



Réponse :

HTML


Page HTML avec détails du produit



Exemple :

Plain Text


GET /products/5/






3. Créer un Produit

Route :

Plain Text


GET/POST /products/create/



Méthode : POST

Paramètres :

JSON


{
  "name": "Café Premium",
  "price": "15.99",
  "expiration_date": "2026-12-31"
}



Réponse :

Plain Text


Redirection vers /products/<id>/
(Produit créé)






4. Modifier un Produit

Route :

Plain Text


GET/POST /products/<id>/edit/



Méthode : POST

Paramètres :

JSON


{
  "name": "Café Premium Nouveau",
  "price": "16.99",
  "expiration_date": "2026-12-31"
}



Réponse :

Plain Text


Redirection vers /products/<id>/
(Produit modifié)



Exemple :

Plain Text


POST /products/5/edit/






5. Supprimer un Produit

Route :

Plain Text


GET/POST /products/<id>/delete/



Méthode : POST

Réponse :

Plain Text


Redirection vers /products/
(Produit supprimé)



Exemple :

Plain Text


POST /products/5/delete/






6. Rechercher des Produits

Route :

Plain Text


GET /products/search/



Paramètres :

Plain Text


?q=café          # Terme de recherche
?min_price=10    # Prix minimum
?max_price=50    # Prix maximum



Réponse :

HTML


Page HTML avec résultats de recherche



Exemple :

Plain Text


GET /products/search/?q=café&min_price=10&max_price=50






📄 Endpoints Factures

1. Liste des Factures

Route :

Plain Text


GET /invoices/



Paramètres :

Plain Text


?page=1          # Numéro de page (défaut: 1)
?status=finalized # Filtrer par statut
?date_from=2026-01-01 # Date début
?date_to=2026-12-31   # Date fin



Réponse :

HTML


Page HTML avec liste paginée des factures



Exemple :

Plain Text


GET /invoices/?page=1&status=finalized






2. Détail d'une Facture

Route :

Plain Text


GET /invoices/<id>/



Paramètres :

Plain Text


<id>  # ID de la facture (entier)



Réponse :

HTML


Page HTML avec détails de la facture



Exemple :

Plain Text


GET /invoices/5/






3. Créer une Facture

Route :

Plain Text


GET/POST /invoices/create/



Méthode : POST

Paramètres :

JSON


{
  "items": [
    {
      "product_id": 1,
      "quantity": 2
    },
    {
      "product_id": 3,
      "quantity": 1
    }
  ]
}



Réponse :

Plain Text


Redirection vers /invoices/<id>/
(Facture créée)






4. Modifier une Facture

Route :

Plain Text


GET/POST /invoices/<id>/edit/



Méthode : POST

Paramètres :

JSON


{
  "items": [
    {
      "product_id": 1,
      "quantity": 3
    }
  ]
}



Réponse :

Plain Text


Redirection vers /invoices/<id>/
(Facture modifiée)



Exemple :

Plain Text


POST /invoices/5/edit/






5. Supprimer une Facture

Route :

Plain Text


GET/POST /invoices/<id>/delete/



Méthode : POST

Réponse :

Plain Text


Redirection vers /invoices/
(Facture supprimée)



Exemple :

Plain Text


POST /invoices/5/delete/






6. Exporter en PDF

Route :

Plain Text


GET /invoices/<id>/pdf/



Paramètres :

Plain Text


<id>  # ID de la facture (entier)



Réponse :

Plain Text


Fichier PDF téléchargé
Nom : INV-<invoice_number>.pdf



Exemple :

Plain Text


GET /invoices/5/pdf/






7. Imprimer une Facture

Route :

Plain Text


GET /invoices/<id>/print/



Paramètres :

Plain Text


<id>  # ID de la facture (entier)



Réponse :

HTML


Page HTML optimisée pour l'impression



Exemple :

Plain Text


GET /invoices/5/print/






8. Finaliser une Facture

Route :

Plain Text


POST /invoices/<id>/finalize/



Paramètres :

Plain Text


<id>  # ID de la facture (entier)



Réponse :

Plain Text


Redirection vers /invoices/<id>/
(Statut changé à 'finalized')



Exemple :

Plain Text


POST /invoices/5/finalize/






📊 Endpoints Rapports

1. Rapport de Ventes

Route :

Plain Text


GET /reports/sales/



Paramètres :

Plain Text


?month=4        # Mois (1-12)
?year=2026      # Année



Réponse :

HTML


Page HTML avec rapport de ventes



Exemple :

Plain Text


GET /reports/sales/?month=4&year=2026






2. Analytique

Route :

Plain Text


GET /reports/analytics/



Réponse :

HTML


Page HTML avec graphiques analytiques






3. Exporter Rapport en PDF

Route :

Plain Text


GET /reports/sales/pdf/



Réponse :

Plain Text


Fichier PDF téléchargé
Nom : rapport_ventes_<date>.pdf






🚨 Endpoints Alertes

1. Liste des Alertes

Route :

Plain Text


GET /alerts/



Paramètres :

Plain Text


?type=expired        # Filtrer par type
?is_active=true      # Filtrer par statut



Réponse :

HTML


Page HTML avec liste des alertes



Exemple :

Plain Text


GET /alerts/?type=expired






2. Détail d'une Alerte

Route :

Plain Text


GET /alerts/<id>/



Réponse :

HTML


Page HTML avec détails de l'alerte



Exemple :

Plain Text


GET /alerts/5/






3. Marquer une Alerte comme Résolue

Route :

Plain Text


POST /alerts/<id>/resolve/



Réponse :

Plain Text


Redirection vers /alerts/
(Alerte marquée comme résolue)



Exemple :

Plain Text


POST /alerts/5/resolve/






📦 Endpoints Archivage

1. Liste des Factures Archivées

Route :

Plain Text


GET /archived-invoices/



Paramètres :

Plain Text


?page=1  # Numéro de page



Réponse :

HTML


Page HTML avec liste des factures archivées






2. Détail d'une Facture Archivée

Route :

Plain Text


GET /archived-invoices/<id>/



Réponse :

HTML


Page HTML avec détails de la facture archivée



Exemple :

Plain Text


GET /archived-invoices/5/






3. Archiver une Facture

Route :

Plain Text


POST /invoices/<id>/archive/



Réponse :

Plain Text


Redirection vers /invoices/
(Facture archivée)



Exemple :

Plain Text


POST /invoices/5/archive/






4. Restaurer une Facture

Route :

Plain Text


POST /archived-invoices/<id>/restore/



Réponse :

Plain Text


Redirection vers /invoices/
(Facture restaurée)



Exemple :

Plain Text


POST /archived-invoices/5/restore/






5. Supprimer Définitivement

Route :

Plain Text


POST /archived-invoices/<id>/delete/



Réponse :

Plain Text


Redirection vers /archived-invoices/
(Facture supprimée définitivement)



Exemple :

Plain Text


POST /archived-invoices/5/delete/






👨‍💼 Endpoints Admin

1. Panneau Admin

Route :

Plain Text


GET /admin/



Authentification : Superuser requis

Réponse :

HTML


Interface d'administration Django






2. Gestion des Produits (Admin)

Route :

Plain Text


GET /admin/facturation/product/



Fonctionnalités :

•
Ajouter un produit

•
Modifier un produit

•
Supprimer un produit

•
Filtrer par prix, date




3. Gestion des Factures (Admin)

Route :

Plain Text


GET /admin/facturation/invoice/



Fonctionnalités :

•
Ajouter une facture

•
Modifier une facture

•
Supprimer une facture

•
Filtrer par statut, date




4. Gestion des Utilisateurs (Admin)

Route :

Plain Text


GET /admin/auth/user/



Fonctionnalités :

•
Ajouter un utilisateur

•
Modifier un utilisateur

•
Supprimer un utilisateur

•
Gérer les permissions




5. Historique d'Audit (Admin)

Route :

Plain Text


GET /admin/facturation/auditlog/



Fonctionnalités :

•
Voir tous les logs

•
Filtrer par action, modèle, date




📝 Exemples de Requêtes cURL

Créer un Produit

Bash


curl -X POST http://localhost:8000/products/create/ \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "name=Café&price=15.99&expiration_date=2026-12-31" \
  -b "sessionid=<session_id>"






Récupérer la Liste des Factures

Bash


curl -X GET "http://localhost:8000/invoices/?page=1" \
  -b "sessionid=<session_id>"






Télécharger un PDF

Bash


curl -X GET http://localhost:8000/invoices/5/pdf/ \
  -b "sessionid=<session_id>" \
  -o invoice.pdf






📊 Codes de Statut HTTP

Code
Signification
200
OK - Succès
201
Created - Créé
302
Redirect - Redirection
400
Bad Request - Mauvaise requête
401
Unauthorized - Non authentifié
403
Forbidden - Interdit
404
Not Found - Non trouvé
500
Server Error - Erreur serveur







🔒 Sécurité

CSRF Protection

Tous les formulaires POST doivent inclure un token CSRF :

HTML


<form method="POST">
  {% csrf_token %}
  <!-- Champs du formulaire -->
</form>






Authentification Requise

Toutes les routes (sauf /login/ ) nécessitent une authentification :

Python


from django.contrib.auth.decorators import login_required

@login_required
def product_list(request):
    # Seuls les utilisateurs connectés peuvent accéder
    ...






📚 Ressources Supplémentaires

•
Django URL Configuration

•
Django Views

•
Django Forms




✨ Prochaines Étapes

•
📚 Consultez UTILISATION.md pour apprendre à utiliser l'application

•
🏗️ Consultez ARCHITECTURE.md pour comprendre la structure

•
🔧 Consultez COMMANDES.md pour les commandes Django




🎉 Conclusion

Cette documentation couvre tous les endpoints disponibles dans l'application !

Bonne chance ! 🚀

