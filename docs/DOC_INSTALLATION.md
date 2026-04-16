🔧 INSTALLATION - Guide Complet

📋 Table des Matières

1.
Prérequis

2.
Installation Rapide

3.
Installation Détaillée

4.
Vérification

5.
Dépannage




✅ Prérequis

Système d'Exploitation

•
Windows 10/11

•
macOS 10.14+

•
Linux (Ubuntu, Debian, etc.)

Logiciels Requis

Python

Bash


# Vérifier la version
python --version  # ou python3 --version

# Doit être 3.8 ou supérieur
# Télécharger : https://www.python.org/downloads/



pip

Bash


# Vérifier l'installation
pip --version  # ou pip3 --version



Git (optionnel )

Bash


git --version






🚀 Installation Rapide

Pour les utilisateurs pressés (5 minutes)

Windows PowerShell

Plain Text


# 1. Décompressez le ZIP
Expand-Archive -Path gestion_facturation_django_final_complete.zip -DestinationPath .
cd gestion_facturation_django

# 2. Créez l'environnement virtuel
python -m venv venv

# 3. Activez-le
.\venv\Scripts\Activate.ps1

# 4. Installez les dépendances
pip install django reportlab

# 5. Appliquez les migrations
python manage.py migrate

# 6. Démarrez le serveur
python manage.py runserver



Windows CMD

Plain Text


# 1. Décompressez le ZIP (ou utilisez l'Explorateur)
cd gestion_facturation_django

# 2. Créez l'environnement virtuel
python -m venv venv

# 3. Activez-le
venv\Scripts\activate.bat

# 4. Installez les dépendances
pip install django reportlab

# 5. Appliquez les migrations
python manage.py migrate

# 6. Démarrez le serveur
python manage.py runserver



macOS/Linux

Bash


# 1. Décompressez le ZIP
unzip gestion_facturation_django_final_complete.zip
cd gestion_facturation_django

# 2. Créez l'environnement virtuel
python3 -m venv venv

# 3. Activez-le
source venv/bin/activate

# 4. Installez les dépendances
pip install django reportlab

# 5. Appliquez les migrations
python manage.py migrate

# 6. Démarrez le serveur
python manage.py runserver



Accès à l'Application

Plain Text


http://localhost:8000/






📖 Installation Détaillée

Étape 1 : Préparer le Système

Windows

Vérifier Python

Plain Text


python --version
# Résultat attendu : Python 3.8.0 ou supérieur



Vérifier pip

Plain Text


pip --version
# Résultat attendu : pip 20.0 ou supérieur



macOS/Linux

Vérifier Python

Bash


python3 --version
# Résultat attendu : Python 3.8.0 ou supérieur



Vérifier pip

Bash


pip3 --version
# Résultat attendu : pip 20.0 ou supérieur



Étape 2 : Décompresser le ZIP

Méthode 1 : Explorateur de Fichiers (Tous les OS )

1.
Localisez le fichier gestion_facturation_django_final_complete.zip

2.
Clic droit → "Extraire tout" (Windows) ou "Décompresser" (macOS)

3.
Choisissez le dossier de destination

4.
Attendez la fin de l'extraction

Méthode 2 : Ligne de Commande

Windows PowerShell

Plain Text


Expand-Archive -Path gestion_facturation_django_final_complete.zip -DestinationPath .



macOS/Linux

Bash


unzip gestion_facturation_django_final_complete.zip



Étape 3 : Naviguer dans le Dossier

Windows PowerShell/CMD

Plain Text


cd gestion_facturation_django



macOS/Linux

Bash


cd gestion_facturation_django



Étape 4 : Créer l'Environnement Virtuel

Windows

Plain Text


python -m venv venv



macOS/Linux

Bash


python3 -m venv venv



Résultat : Un dossier venv/ est créé

Étape 5 : Activer l'Environnement Virtuel

Windows PowerShell

Plain Text


.\venv\Scripts\Activate.ps1



Windows CMD

Plain Text


venv\Scripts\activate.bat



macOS/Linux

Bash


source venv/bin/activate



Vérification : Le prompt doit afficher (venv)

Plain Text


(venv) C:\Users\...\gestion_facturation_django>



Étape 6 : Installer les Dépendances

Bash


pip install django reportlab



Résultat attendu :

Plain Text


Successfully installed django-4.2.0 reportlab-4.0.0



Étape 7 : Appliquer les Migrations

Bash


python manage.py migrate



Résultat attendu :

Plain Text


Operations to perform:
  Apply all migrations: admin, auth, contenttypes, facturation, sessions
Running migrations:
  Applying facturation.0001_initial... OK
  ...



Étape 8 : Créer un Super-Utilisateur (Optionnel)

Bash


python manage.py createsuperuser



Suivez les instructions :

Plain Text


Username: admin
Email address: admin@example.com
Password: ****
Password (again): ****
Superuser created successfully.



Étape 9 : Démarrer le Serveur

Bash


python manage.py runserver



Résultat attendu :

Plain Text


Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.



Étape 10 : Accéder à l'Application

Ouvrez votre navigateur et allez à :

Plain Text


http://localhost:8000/






✅ Vérification

Vérifier l'Installation

Bash


# Vérifier Django
python manage.py --version
# Résultat : 4.2.0 (ou version similaire )

# Vérifier les migrations
python manage.py showmigrations
# Résultat : Toutes les migrations doivent avoir un [X]

# Vérifier les erreurs
python manage.py check
# Résultat : System check identified no issues (0 silenced).



Vérifier l'Accès à l'Application

URL
Accès
Résultat
http://localhost:8000/
✅
Page de connexion
http://localhost:8000/admin/
✅
Admin Django
http://localhost:8000/products/
⚠️
Redirige vers connexion
http://localhost:8000/invoices/
⚠️
Redirige vers connexion







🆘 Dépannage

Problème : "Python n'est pas reconnu"

Cause : Python n'est pas dans le PATH

Solution :

1.
Réinstallez Python

2.
Cochez "Add Python to PATH" pendant l'installation

3.
Redémarrez l'ordinateur

Vérification :

Plain Text


python --version



Problème : "Module django non trouvé"

Cause : Les dépendances ne sont pas installées

Solution :

Bash


# Vérifiez que l'environnement virtuel est activé
# (venv ) doit être visible dans le prompt

# Réinstallez les dépendances
pip install --upgrade pip
pip install django reportlab



Problème : "Port 8000 déjà utilisé"

Cause : Un autre processus utilise le port 8000

Solution :

Bash


# Utilisez un autre port
python manage.py runserver 8001

# Ou arrêtez le processus existant
# Windows : taskkill /PID <PID> /F
# macOS/Linux : kill -9 <PID>



Problème : "Erreur de migration"

Cause : Les migrations ne sont pas appliquées

Solution :

Bash


# Vérifiez les migrations
python manage.py showmigrations

# Appliquez les migrations
python manage.py migrate

# Si problème persiste, réinitialisez
python manage.py migrate facturation zero
python manage.py migrate



Problème : "Erreur de permissions (macOS/Linux)"

Cause : Permissions insuffisantes

Solution :

Bash


# Donnez les permissions
chmod +x manage.py
chmod -R 755 venv/

# Réessayez
python manage.py runserver






🔄 Désactivation de l'Environnement Virtuel

Quand vous avez terminé :

Bash


deactivate



Le prompt revient à la normale (sans (venv))




📝 Notes Importantes

•
✅ L'environnement virtuel doit être activé avant chaque utilisation

•
✅ Les migrations doivent être appliquées une seule fois

•
✅ Le serveur peut être arrêté avec Ctrl + C

•
✅ Pour réutiliser l'application, réactivez simplement l'environnement virtuel




✨ Prochaines Étapes

1.
✅ Installation complète

2.
📖 Consultez UTILISATION.md pour apprendre à utiliser l'application

3.
🏗️ Consultez ARCHITECTURE.md pour comprendre la structure

4.
🆘 Consultez DÉPANNAGE.md en cas de problème




🎉 Installation Réussie !

Vous êtes prêt à utiliser l'application. Accédez à http://localhost:8000/ et commencez à créer vos produits et factures !

