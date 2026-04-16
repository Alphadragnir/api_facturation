📖 README - Gestion de Produits et Factures

🎯 Vue d'Ensemble

Gestion de Produits et Factures est une application web Django complète permettant de gérer efficacement les produits et de générer des factures professionnelles avec des fonctionnalités avancées.

Informations Générales

•
Framework : Django 4.x

•
Base de Données : SQLite (extensible à MySQL/PostgreSQL)

•
Langage : Python 3.8+

•
Interface : HTML5 / CSS3 / JavaScript

•
Version : 1.0.0

•
Date : Avril 2026

•
Licence : MIT




✨ Fonctionnalités Principales

1. Gestion des Produits

•
✅ Créer, modifier, supprimer des produits

•
✅ Afficher la liste paginée des produits (10 par page)

•
✅ Champs : id, nom, prix, date de péremption

•
✅ Recherche par nom

•
✅ Filtrage par prix et date

2. Gestion des Factures

•
✅ Créer des factures avec sélection de produits

•
✅ Définir la quantité pour chaque produit

•
✅ Afficher la liste paginée des factures

•
✅ Consulter le détail d'une facture

•
✅ Calcul automatique du total

3. Fonctionnalités Supplémentaires (8 fonctionnalités)

1.
Export PDF - Télécharger les factures en PDF

2.
Recherche & Filtres - Rechercher produits et factures

3.
Historique d'Audit - Tracer toutes les modifications

4.
Rapports de Ventes - Générer des rapports mensuels

5.
Graphiques Analytique - Visualiser les statistiques

6.
Alertes Produits - Alerter sur les produits expirés

7.
Impression - Imprimer les factures

8.
Archivage - Archiver les anciennes factures




🚀 Démarrage Rapide

Prérequis

•
Python 3.8 ou supérieur

•
pip (gestionnaire de paquets Python)

•
Git (optionnel)

Installation (5 étapes)

Bash


# 1. Décompressez le ZIP
unzip gestion_facturation_django_final_complete.zip
cd gestion_facturation_django

# 2. Créez l'environnement virtuel
python -m venv venv

# 3. Activez-le
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# Windows CMD
venv\Scripts\activate.bat
# macOS/Linux
source venv/bin/activate

# 4. Installez les dépendances
pip install django reportlab

# 5. Appliquez les migrations
python manage.py migrate

# 6. Démarrez le serveur
python manage.py runserver



Accès à l'Application

•
URL : http://localhost:8000/

•
Admin Django : http://localhost:8000/admin/




🔐 Authentification

Comptes de Test

Utilisateur
Mot de passe
Rôle
admin
admin123
Administrateur
user
user123
Utilisateur




Connexion

1.
Accédez à http://localhost:8000/

2.
Entrez vos identifiants

3.
Cliquez sur "Se connecter"




📁 Structure du Projet

Plain Text


gestion_facturation_django/
├── manage.py                 # Point d'entrée Django
├── config/                   # Configuration du projet
│   ├── settings.py          # Paramètres Django
│   ├── urls.py              # URLs principales
│   └── wsgi.py              # Configuration WSGI
├── facturation/             # Application principale
│   ├── models.py            # Modèles de données
│   ├── views.py             # Vues (logique métier )
│   ├── urls.py              # URLs de l'app
│   ├── admin.py             # Admin Django
│   ├── forms.py             # Formulaires
│   ├── utils.py             # Fonctions utilitaires
│   ├── static/              # Fichiers statiques
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │       └── logo.png     # Logo de l'application
│   └── templates/           # Templates HTML
│       └── facturation/
│           ├── base.html
│           ├── index.html
│           ├── products/
│           ├── invoices/
│           └── ...
├── db.sqlite3               # Base de données SQLite
└── venv/                    # Environnement virtuel






🎨 Design & Interface

•
Logo : PRO GESTION DE FACTURES (bleu et blanc)

•
Favicon : Identique au logo

•
Thème : Professionnel et moderne

•
Responsive : Compatible mobile, tablette, desktop

•
Navigation : Sidebar avec menu principal




📊 Modèles de Données

Product

•
id : Identifiant unique

•
name : Nom du produit

•
price : Prix unitaire

•
expiration_date : Date de péremption

•
created_at : Date de création

•
updated_at : Date de modification

Invoice

•
id : Identifiant unique

•
invoice_number : Numéro de facture

•
date : Date de création

•
total : Total de la facture

•
status : Statut (brouillon, finalisée, archivée)

•
created_at : Date de création

InvoiceItem

•
id : Identifiant unique

•
invoice : Référence à la facture

•
product : Référence au produit

•
quantity : Quantité

•
unit_price : Prix unitaire

•
subtotal : Sous-total

AuditLog

•
id : Identifiant unique

•
action : Action effectuée (create, update, delete)

•
model : Modèle affecté

•
object_id : ID de l'objet

•
changes : Détails des modifications

•
timestamp : Date/heure

ArchivedInvoice

•
id : Identifiant unique

•
original_id : ID de la facture originale

•
data : Données JSON de la facture

•
archived_at : Date d'archivage

ProductAlert

•
id : Identifiant unique

•
product : Référence au produit

•
alert_type : Type d'alerte (expiré, bientôt expiré)

•
is_active : Statut de l'alerte

•
created_at : Date de création




🔧 Configuration

Fichier settings.py

Les paramètres importants :

Python


# Base de données
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Applications installées
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'facturation',
]

# Pagination
PAGINATION_SIZE = 10






📖 Documentation Complète

Pour plus de détails, consultez les autres fichiers :

•
INSTALLATION.md - Guide d'installation détaillé

•
UTILISATION.md - Guide d'utilisation

•
ARCHITECTURE.md - Architecture technique

•
FONCTIONNALITES.md - Détail des fonctionnalités

•
DÉPANNAGE.md - Solutions aux problèmes

•
COMMANDES.md - Commandes Django

•
API.md - Documentation des endpoints




🤝 Support

Problèmes Courants

•
Python non reconnu → Voir DÉPANNAGE.md

•
Module Django manquant → Voir COMMANDES.md

•
Port déjà utilisé → Voir DÉPANNAGE.md

Contact

Pour toute question, consultez la documentation ou contactez l'équipe support.




📋 Mentions Légales

© 2026 - Gestion de Produits et Factures
Tous droits réservés.

Pour les mentions légales complètes, consultez la page /legal/ de l'application.




✅ Checklist de Démarrage




Python 3.8+ installé




ZIP décompressé




Environnement virtuel créé




Dépendances installées




Migrations appliquées




Serveur démarré




Application accessible à http://localhost:8000/




Connecté avec les comptes de test




🎉 Bienvenue !

L'application est prête à être utilisée. Commencez par créer vos premiers produits, puis générez vos factures !

Bonne utilisation ! 🚀

