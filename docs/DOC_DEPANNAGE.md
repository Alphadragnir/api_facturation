🆘 DÉPANNAGE - Solutions aux Problèmes Courants

📋 Table des Matières

1.
Problèmes d'Installation

2.
Problèmes de Démarrage

3.
Problèmes d'Authentification

4.
Problèmes de Données

5.
Problèmes de Base de Données

6.
Problèmes de Navigateur

7.
Problèmes de Performance




🔧 Problèmes d'Installation

Problème 1 : "Python n'est pas reconnu"

Symptômes :

Plain Text


'python' is not recognized as an internal or external command



Causes Possibles :

•
Python n'est pas installé

•
Python n'est pas dans le PATH

•
Mauvaise version de Python

Solutions :

Solution 1 : Vérifier l'Installation

Bash


python --version
# ou
python3 --version



Solution 2 : Réinstaller Python

1.
Téléchargez Python depuis https://www.python.org/downloads/

2.
IMPORTANT : Cochez "Add Python to PATH" pendant l'installation

3.
Redémarrez l'ordinateur

4.
Vérifiez : python --version

Solution 3 : Utiliser le Chemin Complet

Bash


C:\Python311\python.exe --version



Solution 4 : Utiliser python3 (macOS/Linux )

Bash


python3 --version
python3 -m venv venv






Problème 2 : "Module pip non trouvé"

Symptômes :

Plain Text


No module named pip



Solutions :

Bash


# Réinstaller pip
python -m ensurepip --upgrade

# Vérifier pip
pip --version






Problème 3 : "Erreur lors de la décompression du ZIP"

Symptômes :

Plain Text


Erreur de décompression
Fichier corrompu



Solutions :

Windows

1.
Clic droit sur le ZIP

2.
"Extraire tout"

3.
Choisissez un dossier

4.
Attendez la fin

macOS/Linux

Bash


unzip gestion_facturation_django_final_complete.zip
# ou
tar -xzf gestion_facturation_django_final_complete.tar.gz






🚀 Problèmes de Démarrage

Problème 4 : "Port 8000 déjà utilisé"

Symptômes :

Plain Text


Address already in use
Port 8000 is already in use



Causes :

•
Un autre processus utilise le port 8000

•
Le serveur Django n'a pas été arrêté correctement

Solutions :

Solution 1 : Utiliser un Autre Port

Bash


python manage.py runserver 8001
# Accédez à http://localhost:8001/



Solution 2 : Trouver et Arrêter le Processus

Windows :

Plain Text


# Trouver le processus
netstat -ano | findstr :8000

# Arrêter le processus (remplacez PID par le numéro )
taskkill /PID <PID> /F



macOS/Linux :

Bash


# Trouver le processus
lsof -i :8000

# Arrêter le processus
kill -9 <PID>



Solution 3 : Attendre quelques Minutes

Le port peut être libéré automatiquement après quelques minutes.




Problème 5 : "Django n'est pas installé"

Symptômes :

Plain Text


ModuleNotFoundError: No module named 'django'



Causes :

•
L'environnement virtuel n'est pas activé

•
Les dépendances ne sont pas installées

Solutions :

Bash


# Vérifier que l'environnement virtuel est activé
# (venv) doit être visible dans le prompt

# Réinstaller Django
pip install django reportlab

# Vérifier l'installation
python -c "import django; print(django.get_version())"






Problème 6 : "Erreur lors du démarrage du serveur"

Symptômes :

Plain Text


Error: That port is already in use.
SyntaxError in settings.py



Solutions :

Bash


# Vérifier la syntaxe
python manage.py check

# Voir les erreurs détaillées
python manage.py runserver --verbosity 2

# Réinitialiser la base de données
python manage.py migrate






🔐 Problèmes d'Authentification

Problème 7 : "Impossible de se connecter"

Symptômes :

Plain Text


Identifiants incorrects
Page de connexion en boucle



Causes :

•
Identifiants incorrects

•
Compte utilisateur supprimé

•
Problème de session

Solutions :

Solution 1 : Vérifier les Identifiants

Plain Text


Utilisateur : admin
Mot de passe : admin123



Solution 2 : Créer un Nouvel Utilisateur

Bash


python manage.py createsuperuser
# Suivez les instructions



Solution 3 : Réinitialiser la Base de Données

Bash


# ⚠️ Attention : Cela supprimera toutes les données
python manage.py migrate facturation zero
python manage.py migrate
python manage.py createsuperuser






Problème 8 : "Session expirée"

Symptômes :

Plain Text


Vous avez été déconnecté
Veuillez vous reconnecter



Causes :

•
Session expirée (par défaut : 2 semaines)

•
Navigateur fermé

•
Cookies supprimés

Solutions :

1.
Reconnectez-vous

2.
Cochez "Se souvenir de moi" (si disponible)

3.
Vérifiez les paramètres des cookies du navigateur




💾 Problèmes de Données

Problème 9 : "Produit non trouvé"

Symptômes :

Plain Text


Erreur 404
Produit n'existe pas



Causes :

•
Produit supprimé

•
ID incorrect

•
Produit archivé

Solutions :

Bash


# Vérifier les produits
python manage.py shell
>>> from facturation.models import Product
>>> Product.objects.all()






Problème 10 : "Facture vide"

Symptômes :

Plain Text


Aucun produit dans la facture
Total = 0 €



Causes :

•
Pas de produits sélectionnés

•
Produits supprimés après création

Solutions :

1.
Créez des produits d'abord

2.
Sélectionnez les produits lors de la création de facture

3.
Vérifiez que les produits ne sont pas supprimés




Problème 11 : "Total incorrect"

Symptômes :

Plain Text


Total ne correspond pas aux articles
Calcul erroné



Causes :

•
Quantités incorrectes

•
Prix modifiés après création

•
Erreur de calcul

Solutions :

Bash


# Vérifier les calculs
python manage.py shell
>>> from facturation.models import Invoice, InvoiceItem
>>> invoice = Invoice.objects.get(pk=1)
>>> for item in invoice.items.all():
...     print(f"{item.product.name}: {item.quantity} x {item.unit_price} = {item.subtotal}")






🗄️ Problèmes de Base de Données

Problème 12 : "Erreur de migration"

Symptômes :

Plain Text


Migration error
Table does not exist



Causes :

•
Migrations non appliquées

•
Migrations conflictuelles

•
Base de données corrompue

Solutions :

Bash


# Voir l'état des migrations
python manage.py showmigrations

# Appliquer les migrations
python manage.py migrate

# Réinitialiser les migrations (⚠️ Attention : perte de données)
python manage.py migrate facturation zero
python manage.py migrate






Problème 13 : "Base de données verrouillée"

Symptômes :

Plain Text


database is locked
cannot lock database



Causes :

•
Plusieurs processus accèdent à la base de données

•
Fichier db.sqlite3 en lecture seule

Solutions :

Windows :

Plain Text


# Arrêter tous les processus Python
taskkill /F /IM python.exe

# Supprimer le fichier de verrou
Remove-Item db.sqlite3-wal
Remove-Item db.sqlite3-shm



macOS/Linux :

Bash


# Arrêter tous les processus Python
killall python

# Supprimer les fichiers de verrou
rm db.sqlite3-wal
rm db.sqlite3-shm






Problème 14 : "Données perdues"

Symptômes :

Plain Text


Produits/factures disparus
Base de données vide



Causes :

•
Suppression accidentelle

•
Migration mal appliquée

•
Fichier db.sqlite3 supprimé

Solutions :

Bash


# Vérifier les données
python manage.py shell
>>> from facturation.models import Product
>>> Product.objects.count()

# Restaurer depuis une sauvegarde
# (Si vous avez une sauvegarde)
cp db.sqlite3.backup db.sqlite3






🌐 Problèmes de Navigateur

Problème 15 : "Page blanche"

Symptômes :

Plain Text


Aucun contenu affiché
Page vide



Causes :

•
Erreur serveur

•
Fichiers statiques non chargés

•
Problème de template

Solutions :

Bash


# Collecter les fichiers statiques
python manage.py collectstatic

# Voir les erreurs dans la console
python manage.py runserver --verbosity 2

# Vérifier la console du navigateur (F12)






Problème 16 : "Erreur 404 - Page non trouvée"

Symptômes :

Plain Text


404 Not Found
Page does not exist



Causes :

•
URL incorrecte

•
Route non définie

•
Ressource supprimée

Solutions :

1.
Vérifiez l'URL

2.
Consultez les URLs disponibles dans urls.py

3.
Vérifiez que la ressource existe




Problème 17 : "Erreur 500 - Erreur serveur"

Symptômes :

Plain Text


500 Internal Server Error
Something went wrong



Causes :

•
Erreur dans le code

•
Exception non gérée

•
Problème de base de données

Solutions :

Bash


# Voir les erreurs détaillées
python manage.py runserver --verbosity 2

# Vérifier les logs
# Fichier : console lors du démarrage du serveur

# Activer le mode debug (développement seulement)
# Dans settings.py : DEBUG = True






Problème 18 : "Fichiers statiques non chargés"

Symptômes :

Plain Text


CSS/JS ne s'affichent pas
Images manquantes



Causes :

•
Fichiers statiques non collectés

•
Chemin incorrect

•
Serveur statique non configuré

Solutions :

Bash


# Collecter les fichiers statiques
python manage.py collectstatic --noinput

# Vérifier les chemins dans settings.py
# STATIC_URL = '/static/'
# STATIC_ROOT = BASE_DIR / 'staticfiles'






⚡ Problèmes de Performance

Problème 19 : "Application lente"

Symptômes :

Plain Text


Pages lentes à charger
Requêtes longues



Causes :

•
Beaucoup de données

•
Requêtes non optimisées

•
Ressources insuffisantes

Solutions :

Bash


# Utiliser la pagination
# (Déjà implémentée : 10 éléments par page)

# Optimiser les requêtes
# Dans views.py : utiliser select_related() et prefetch_related()

# Augmenter les ressources
# RAM, CPU, disque






Problème 20 : "Mémoire insuffisante"

Symptômes :

Plain Text


MemoryError
Out of memory



Causes :

•
Trop de données chargées

•
Fuite mémoire

•
Ressources limitées

Solutions :

Bash


# Réduire la taille des requêtes
# Utiliser la pagination

# Redémarrer le serveur
# Ctrl + C, puis python manage.py runserver

# Augmenter la RAM disponible






📝 Checklist de Dépannage

Avant de contacter le support, vérifiez :




Python est installé et dans le PATH




L'environnement virtuel est activé




Les dépendances sont installées (pip install django reportlab)




Les migrations sont appliquées (python manage.py migrate)




Le serveur démarre sans erreur (python manage.py runserver)




Vous pouvez accéder à http://localhost:8000/




Vous pouvez vous connecter avec les identifiants de test




Les produits et factures s'affichent correctement




🆘 Si le Problème Persiste

1.
Consultez les logs :

Bash


python manage.py runserver --verbosity 2





2.
Réinitialisez la base de données :

Bash


python manage.py migrate facturation zero
python manage.py migrate





3.
Supprimez l'environnement virtuel et recommencez :

Bash


rm -rf venv
python -m venv venv
# Réactivez et réinstallez





4.
Consultez la documentation :

•
INSTALLATION.md

•
ARCHITECTURE.md

•
COMMANDES.md






📞 Support Technique

Pour toute question ou problème non résolu :

1.
Consultez les autres fichiers de documentation

2.
Vérifiez les logs du serveur

3.
Essayez les solutions proposées ci-dessus




✨ Prochaines Étapes

•
📚 Consultez UTILISATION.md pour apprendre à utiliser l'application

•
🏗️ Consultez ARCHITECTURE.md pour comprendre la structure

•
🔧 Consultez COMMANDES.md pour les commandes Django




🎉 Bonne Chance !

La plupart des problèmes peuvent être résolus en suivant les solutions proposées ci-dessus.

N'hésitez pas à consulter la documentation ! 📖

