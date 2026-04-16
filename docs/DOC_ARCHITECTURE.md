🏗️ ARCHITECTURE - Documentation Technique

📋 Table des Matières

1.
Vue d'Ensemble

2.
Principes de Conception

3.
Modèles de Données

4.
Flux de Données

5.
Structure des Dossiers

6.
Authentification

7.
Vues Principales

8.
Fonctions Utilitaires




🎯 Vue d'Ensemble

Architecture MVC (Model-View-Controller)

L'application suit le pattern MVC de Django :

Plain Text


┌─────────────────────────────────────────────────────┐
│                   Django Application                 │
├─────────────────────────────────────────────────────┤
│                                                       │
│  ┌─────────────────────────────────────────────┐   │
│  │ Models (models.py)                          │   │
│  │ - Product, Invoice, InvoiceItem             │   │
│  │ - AuditLog, ArchivedInvoice, ProductAlert   │   │
│  └─────────────────────────────────────────────┘   │
│                        ↓                             │
│  ┌─────────────────────────────────────────────┐   │
│  │ Views (views.py)                            │   │
│  │ - ProductListView, InvoiceDetailView        │   │
│  │ - ReportView, AlertView, etc.               │   │
│  └─────────────────────────────────────────────┘   │
│                        ↓                             │
│  ┌─────────────────────────────────────────────┐   │
│  │ Templates (templates/)                      │   │
│  │ - base.html, product_list.html              │   │
│  │ - invoice_detail.html, etc.                 │   │
│  └─────────────────────────────────────────────┘   │
│                                                       │
└─────────────────────────────────────────────────────┘






🔧 Principes de Conception

1. Séparation des Préoccupations

•
Models : Logique métier et données

•
Views : Logique de présentation

•
Templates : Rendu HTML

•
Utils : Fonctions réutilisables

2. DRY (Don't Repeat Yourself)

•
Fonctions réutilisables dans utils.py

•
Templates hérités (base.html)

•
Mixins pour les vues communes

3. Sécurité

•
Authentification obligatoire

•
CSRF protection

•
SQL injection prevention (ORM Django)

•
Validation des formulaires

4. Performance

•
Pagination des listes

•
Index sur les clés étrangères

•
Requêtes optimisées (select_related, prefetch_related)

•
Cache des rapports




📊 Modèles de Données

1. Product

Python


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    @property
    def is_expired(self):
        return self.expiration_date < date.today()



Champs :

•
id : Clé primaire (auto-incrémentée)

•
name : Nom du produit (255 caractères max)

•
price : Prix unitaire (10 chiffres, 2 décimales)

•
expiration_date : Date de péremption

•
created_at : Date de création (automatique)

•
updated_at : Date de modification (automatique)

Méthodes :

•
is_expired : Vérifie si le produit est expiré

2. Invoice

Python


class Invoice(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Brouillon'),
        ('finalized', 'Finalisée'),
        ('archived', 'Archivée'),
    ]
    
    invoice_number = models.CharField(max_length=50, unique=True)
    date = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='draft')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Facture {self.invoice_number}"



Champs :

•
id : Clé primaire

•
invoice_number : Numéro unique de facture

•
date : Date de création

•
total : Total calculé

•
status : Statut (brouillon, finalisée, archivée)

•
created_at : Date de création

3. InvoiceItem

Python


class InvoiceItem(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    
    @property
    def subtotal(self):
        return self.quantity * self.unit_price



Champs :

•
id : Clé primaire

•
invoice : Clé étrangère vers Invoice

•
product : Clé étrangère vers Product

•
quantity : Quantité commandée

•
unit_price : Prix unitaire au moment de la commande

Propriétés :

•
subtotal : Calcul automatique (quantité × prix)

4. AuditLog

Python


class AuditLog(models.Model):
    ACTION_CHOICES = [
        ('create', 'Création'),
        ('update', 'Modification'),
        ('delete', 'Suppression'),
    ]
    
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    model = models.CharField(max_length=50)
    object_id = models.IntegerField()
    changes = models.JSONField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)



Champs :

•
action : Type d'action (create, update, delete)

•
model : Nom du modèle affecté

•
object_id : ID de l'objet

•
changes : Détails des modifications (JSON)

•
timestamp : Date/heure de l'action

5. ArchivedInvoice

Python


class ArchivedInvoice(models.Model):
    original_id = models.IntegerField()
    data = models.JSONField()
    archived_at = models.DateTimeField(auto_now_add=True)



Champs :

•
original_id : ID de la facture originale

•
data : Données JSON complètes de la facture

•
archived_at : Date d'archivage

6. ProductAlert

Python


class ProductAlert(models.Model):
    ALERT_TYPES = [
        ('expired', 'Expiré'),
        ('expiring_soon', 'Expire bientôt'),
    ]
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    alert_type = models.CharField(max_length=20, choices=ALERT_TYPES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)



Champs :

•
product : Clé étrangère vers Product

•
alert_type : Type d'alerte (expiré, expire bientôt)

•
is_active : Statut de l'alerte

•
created_at : Date de création




🔄 Flux de Données

Flux de Création de Facture

Plain Text


1. Utilisateur accède à /invoices/create/
                    ↓
2. Vue InvoiceCreateView affiche le formulaire
                    ↓
3. Utilisateur sélectionne les produits et quantités
                    ↓
4. Formulaire soumis (POST)
                    ↓
5. Vue valide les données
                    ↓
6. Création de l'Invoice
                    ↓
7. Création des InvoiceItems pour chaque produit
                    ↓
8. Calcul du total
                    ↓
9. Création d'un AuditLog
                    ↓
10. Redirection vers le détail de la facture



Flux d'Export PDF

Plain Text


1. Utilisateur clique sur "Télécharger PDF"
                    ↓
2. Vue InvoicePdfView récupère la facture
                    ↓
3. Récupère les InvoiceItems associés
                    ↓
4. Génère le PDF avec ReportLab
                    ↓
5. Retourne le fichier au navigateur
                    ↓
6. Navigateur télécharge le fichier

📁 Structure des Dossiers

Plain Text


gestion_facturation_django/
│
├── manage.py                          # Point d'entrée Django
│
├── config/                            # Configuration du projet
│   ├── settings.py                   # Paramètres Django
│   ├── urls.py                       # URLs principales
│   ├── wsgi.py                       # Configuration WSGI
│   └── asgi.py                       # Configuration ASGI
│
├── facturation/                       # Application principale
│   ├── migrations/                   # Migrations de base de données
│   │   ├── 0001_initial.py
│   │   ├── 0002_*.py
│   │   └── ...
│   │
│   ├── templates/                    # Templates HTML
│   │   └── facturation/
│   │       ├── base.html             # Template de base
│   │       ├── index.html            # Tableau de bord
│   │       ├── products/
│   │       │   ├── list.html
│   │       │   ├── form.html
│   │       │   └── detail.html
│   │       ├── invoices/
│   │       │   ├── list.html
│   │       │   ├── form.html
│   │       │   ├── detail.html
│   │       │   └── print.html
│   │       ├── reports/
│   │       │   ├── sales.html
│   │       │   └── analytics.html
│   │       ├── alerts/
│   │       │   └── list.html
│   │       └── ...
│   │
│   ├── static/                       # Fichiers statiques
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── script.js
│   │   └── images/
│   │       └── logo.png
│   │
│   ├── models.py                     # Modèles de données
│   ├── views.py                      # Vues (logique métier)
│   ├── urls.py                       # URLs de l'app
│   ├── forms.py                      # Formulaires
│   ├── admin.py                      # Configuration admin
│   ├── utils.py                      # Fonctions utilitaires
│   ├── apps.py                       # Configuration de l'app
│   └── __init__.py
│
├── db.sqlite3                         # Base de données SQLite
│
├── venv/                              # Environnement virtuel
│   ├── bin/                           # Exécutables (macOS/Linux)
│   ├── Scripts/                       # Exécutables (Windows)
│   └── lib/                           # Packages Python
│
└── README.md                          # Documentation






🔐 Authentification

Système d'Authentification Django

L'application utilise le système d'authentification intégré de Django :

Python


# Vérification de l'authentification dans les vues
from django.contrib.auth.decorators import login_required

@login_required
def product_list(request):
    # Seuls les utilisateurs connectés peuvent accéder
    products = Product.objects.all()
    return render(request, 'facturation/products/list.html', {'products': products})



Middleware d'Authentification

Python


# Dans settings.py
MIDDLEWARE = [
    ...
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    ...
]



Permissions

Python


# Vérifier les permissions
from django.contrib.auth.decorators import permission_required

@permission_required('facturation.delete_product')
def delete_product(request, pk):
    # Seuls les utilisateurs avec la permission peuvent supprimer
    ...






👁️ Vues Principales

1. ProductListView

Python


class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'facturation/products/list.html'
    paginate_by = 10
    context_object_name = 'products'



Fonctionnalités :

•
Affiche la liste des produits

•
Pagination (10 par page)

•
Authentification requise

2. InvoiceDetailView

Python


class InvoiceDetailView(LoginRequiredMixin, DetailView):
    model = Invoice
    template_name = 'facturation/invoices/detail.html'
    context_object_name = 'invoice'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['items'] = self.object.items.all()
        context['total_items'] = sum(item.quantity for item in context['items'])
        return context



Fonctionnalités :

•
Affiche le détail d'une facture

•
Calcule le nombre total de produits

•
Affiche le total à payer

3. ReportView

Python


def report_sales(request):
    invoices = Invoice.objects.filter(status='finalized')
    total_sales = sum(inv.total for inv in invoices)
    total_invoices = invoices.count()
    
    context = {
        'total_sales': total_sales,
        'total_invoices': total_invoices,
        'invoices': invoices,
    }
    return render(request, 'facturation/reports/sales.html', context)



Fonctionnalités :

•
Génère les rapports de ventes

•
Calcule les statistiques

•
Affiche les graphiques




🛠️ Fonctions Utilitaires

utils.py

Python


# Génération de numéro de facture
def generate_invoice_number():
    from datetime import datetime
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    return f"INV-{timestamp}"

# Calcul du total d'une facture
def calculate_invoice_total(invoice):
    return sum(item.subtotal for item in invoice.items.all())

# Vérification des produits expirés
def check_expired_products():
    from datetime import date
    expired = Product.objects.filter(expiration_date__lt=date.today())
    for product in expired:
        ProductAlert.objects.get_or_create(
            product=product,
            alert_type='expired'
        )

# Génération de PDF
def generate_invoice_pdf(invoice):
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    
    # Création du PDF
    pdf = canvas.Canvas("invoice.pdf", pagesize=letter)
    # ... logique de génération
    pdf.save()
    return pdf






🔗 Relations Entre Modèles

Plain Text


Product (1) ──────────── (N) InvoiceItem ──────────── (N) Invoice
   │                                                        │
   │                                                        │
   └─────────────────── (1) ProductAlert                   │
                                                            │
                                                            └─── (1) ArchivedInvoice






📈 Performance

Optimisations Implémentées

1.
Pagination : Limite les résultats affichés

2.
Index : Sur les clés étrangères et les champs de recherche

3.
Requêtes Optimisées : Utilisation de select_related() et prefetch_related()

4.
Cache : Cache des rapports et graphiques

Exemple de Requête Optimisée

Python


# ❌ Mauvais (N+1 queries)
invoices = Invoice.objects.all()
for invoice in invoices:
    items = invoice.items.all()  # Requête par facture

# ✅ Bon (1 requête)
invoices = Invoice.objects.prefetch_related('items').all()






🔒 Sécurité

Mesures de Sécurité

1.
CSRF Protection : Token CSRF sur tous les formulaires

2.
SQL Injection : ORM Django prévient les injections

3.
XSS Protection : Échappement automatique des variables

4.
Authentification : Obligatoire pour toutes les vues

5.
Validation : Validation des formulaires côté serveur




📝 Prochaines Étapes

•
📚 Consultez UTILISATION.md pour apprendre à utiliser l'application

•
🔧 Consultez COMMANDES.md pour les commandes Django

•
🆘 Consultez DÉPANNAGE.md en cas de problème




✨ Conclusion

L'architecture suit les meilleures pratiques Django :

•
✅ Séparation des préoccupations

•
✅ Sécurité renforcée

•
✅ Performance optimisée

•
✅ Maintenabilité assurée

L'application est prête pour la production ! 🚀

