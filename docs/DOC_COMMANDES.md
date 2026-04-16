🔧 COMMANDES - Toutes les Commandes Django

📋 Table des Matières

1.
Commandes de Base

2.
Commandes de Gestion de Base de Données

3.
Commandes d'Utilisateurs

4.
Commandes de Développement

5.
Commandes de Production

6.
Commandes Personnalisées




🚀 Commandes de Base

Démarrer le Serveur de Développement

Bash


python manage.py runserver
# Accédez à http://localhost:8000/



Options :

Bash


# Utiliser un port différent
python manage.py runserver 8001

# Écouter sur toutes les interfaces
python manage.py runserver 0.0.0.0:8000

# Verbose (affiche plus d'informations )
python manage.py runserver --verbosity 2






Vérifier la Configuration

Bash


python manage.py check
# Affiche les erreurs de configuration



Exemple de Sortie :

Plain Text


System check identified no issues (0 silenced).






Afficher la Version Django

Bash


python manage.py --version
# Affiche : 4.2.0 (ou votre version)






Afficher l'Aide

Bash


python manage.py help
# Liste toutes les commandes disponibles

python manage.py help <commande>
# Affiche l'aide pour une commande spécifique






💾 Commandes de Gestion de Base de Données

Afficher l'État des Migrations

Bash


python manage.py showmigrations
# Affiche toutes les migrations et leur statut



Exemple de Sortie :

Plain Text


facturation
 [X] 0001_initial
 [X] 0002_add_audit_log
 [ ] 0003_add_alerts






Créer une Migration

Bash


python manage.py makemigrations
# Crée les migrations basées sur les changements du modèle

python manage.py makemigrations facturation
# Crée les migrations pour l'app 'facturation' uniquement



Exemple de Sortie :

Plain Text


Migrations for 'facturation':
  facturation/migrations/0003_product_description.py
    - Add field description to product






Appliquer les Migrations

Bash


python manage.py migrate
# Applique toutes les migrations

python manage.py migrate facturation
# Applique les migrations pour l'app 'facturation' uniquement

python manage.py migrate facturation 0002
# Applique jusqu'à la migration 0002






Annuler les Migrations

Bash


python manage.py migrate facturation zero
# Annule toutes les migrations de 'facturation'

python manage.py migrate facturation 0001
# Revient à la migration 0001






Afficher le SQL d'une Migration

Bash


python manage.py sqlmigrate facturation 0001
# Affiche le SQL de la migration 0001






Vider la Base de Données

Bash


python manage.py flush
# Supprime toutes les données (demande confirmation)

python manage.py flush --noinput
# Supprime sans demander confirmation






👤 Commandes d'Utilisateurs

Créer un Super-Utilisateur (Admin)

Bash


python manage.py createsuperuser
# Demande : username, email, password



Exemple d'Interaction :

Plain Text


Username: admin
Email address: admin@example.com
Password: 
Password (again): 
Superuser created successfully.






Créer un Utilisateur Normal

Bash


python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.create_user('username', 'email@example.com', 'password')
>>> exit()






Modifier le Mot de Passe d'un Utilisateur

Bash


python manage.py changepassword username
# Demande le nouveau mot de passe






Lister les Utilisateurs

Bash


python manage.py shell
>>> from django.contrib.auth.models import User
>>> for user in User.objects.all():
...     print(f"{user.username} - {user.email}")
>>> exit()






Supprimer un Utilisateur

Bash


python manage.py shell
>>> from django.contrib.auth.models import User
>>> User.objects.get(username='username').delete()
>>> exit()






🛠️ Commandes de Développement

Accéder à la Console Python Django

Bash


python manage.py shell
# Accès interactif à la base de données



Exemples :

Python


# Importer les modèles
from facturation.models import Product, Invoice

# Créer un produit
product = Product.objects.create(
    name="Café Premium",
    price=15.99,
    expiration_date="2026-12-31"
)

# Récupérer tous les produits
products = Product.objects.all()

# Filtrer les produits
expensive = Product.objects.filter(price__gte=20)

# Supprimer un produit
product.delete()

# Quitter
exit()






Exécuter des Tests

Bash


python manage.py test
# Lance tous les tests

python manage.py test facturation
# Lance les tests de l'app 'facturation'

python manage.py test facturation.tests.ProductTests
# Lance les tests d'une classe spécifique






Collecter les Fichiers Statiques

Bash


python manage.py collectstatic
# Collecte tous les fichiers statiques

python manage.py collectstatic --noinput
# Collecte sans demander confirmation






Générer les Fichiers Statiques

Bash


python manage.py compress
# Compresse les fichiers CSS et JS






🚀 Commandes de Production

Préparer pour la Production

Bash


python manage.py check --deploy
# Vérifie la configuration de production






Collecter et Compresser les Fichiers Statiques

Bash


python manage.py collectstatic --noinput
python manage.py compress --force-inline






Créer une Sauvegarde de la Base de Données

Bash


# Windows
copy db.sqlite3 db.sqlite3.backup

# macOS/Linux
cp db.sqlite3 db.sqlite3.backup






Restaurer une Sauvegarde

Bash


# Windows
copy db.sqlite3.backup db.sqlite3

# macOS/Linux
cp db.sqlite3.backup db.sqlite3






🔧 Commandes Personnalisées

Exporter les Données

Bash


python manage.py dumpdata > data.json
# Exporte toutes les données en JSON

python manage.py dumpdata facturation > facturation.json
# Exporte les données de 'facturation' en JSON






Importer les Données

Bash


python manage.py loaddata data.json
# Importe les données depuis un fichier JSON






Vérifier les Erreurs

Bash


python manage.py check
# Vérifie la configuration

python manage.py check --deploy
# Vérifie pour la production






Générer les Graphiques de Modèles

Bash


python manage.py graph_models -a -o models.png
# Génère un graphique des modèles (nécessite graphviz)






📊 Commandes Utiles Combinées

Installation Complète

Bash


# 1. Créer l'environnement virtuel
python -m venv venv

# 2. Activer l'environnement
# Windows PowerShell
.\venv\Scripts\Activate.ps1
# Windows CMD
venv\Scripts\activate.bat
# macOS/Linux
source venv/bin/activate

# 3. Installer les dépendances
pip install django reportlab

# 4. Appliquer les migrations
python manage.py migrate

# 5. Créer un super-utilisateur
python manage.py createsuperuser

# 6. Démarrer le serveur
python manage.py runserver






Réinitialisation Complète

Bash


# 1. Arrêter le serveur (Ctrl + C)

# 2. Supprimer la base de données
rm db.sqlite3  # macOS/Linux
del db.sqlite3  # Windows

# 3. Réappliquer les migrations
python manage.py migrate

# 4. Créer un nouveau super-utilisateur
python manage.py createsuperuser

# 5. Redémarrer le serveur
python manage.py runserver






Développement Complet

Bash


# 1. Créer une migration
python manage.py makemigrations

# 2. Appliquer la migration
python manage.py migrate

# 3. Lancer les tests
python manage.py test

# 4. Vérifier la configuration
python manage.py check

# 5. Démarrer le serveur
python manage.py runserver






📝 Commandes Utiles pour l'Admin

Accéder à l'Admin Django

Plain Text


URL : http://localhost:8000/admin/
Utilisateur : admin
Mot de passe : admin123



Fonctionnalités :

•
Ajouter/modifier/supprimer des produits

•
Ajouter/modifier/supprimer des factures

•
Gérer les utilisateurs

•
Voir les logs d'audit




Exécuter des Commandes SQL Personnalisées

Bash


python manage.py dbshell
# Accès à la console SQL



Exemples :

SQL


-- Voir tous les produits
SELECT * FROM facturation_product;

-- Voir toutes les factures
SELECT * FROM facturation_invoice;

-- Compter les produits
SELECT COUNT(* ) FROM facturation_product;

-- Quitter
.quit






🎯 Commandes par Cas d'Usage

Je veux Ajouter une Nouvelle Fonctionnalité

Bash


# 1. Modifier le modèle dans models.py
# 2. Créer une migration
python manage.py makemigrations

# 3. Appliquer la migration
python manage.py migrate

# 4. Tester
python manage.py test

# 5. Démarrer le serveur
python manage.py runserver






Je veux Corriger une Erreur

Bash


# 1. Vérifier les erreurs
python manage.py check

# 2. Voir les logs détaillés
python manage.py runserver --verbosity 2

# 3. Corriger le code
# 4. Redémarrer le serveur
python manage.py runserver






Je veux Sauvegarder les Données

Bash


# Exporter les données
python manage.py dumpdata > backup.json

# Ou sauvegarder la base de données
cp db.sqlite3 db.sqlite3.backup






Je veux Restaurer les Données

Bash


# Importer les données
python manage.py loaddata backup.json

# Ou restaurer la base de données
cp db.sqlite3.backup db.sqlite3






📚 Ressources Supplémentaires

•
Documentation Django Officielle

•
Django Management Commands

•
Django Models




✨ Prochaines Étapes

•
📚 Consultez UTILISATION.md pour apprendre à utiliser l'application

•
🏗️ Consultez ARCHITECTURE.md pour comprendre la structure

•
🆘 Consultez DÉPANNAGE.md en cas de problème




🎉 Conclusion

Ces commandes vous permettent de gérer complètement votre application Django !

Bonne chance ! 🚀

