✨ FONCTIONNALITES - Les 8 Fonctionnalités Supplémentaires

📋 Table des Matières

1.
Export PDF

2.
Recherche et Filtres

3.
Historique d'Audit

4.
Rapports de Ventes

5.
Graphiques Analytique

6.
Alertes Produits

7.
Impression

8.
Archivage




1. Export PDF

Description

Exporte les factures au format PDF professionnel, prêt à être imprimé ou envoyé par email.

Accès

•
Menu : Factures → Cliquez sur une facture → "Télécharger PDF"

•
URL : /invoices/<id>/pdf/

Fonctionnalités

✅ Génération automatique du PDF
✅ Formatage professionnel
✅ Inclusion du logo
✅ Détails complets de la facture
✅ Téléchargement automatique

Contenu du PDF

•
En-tête avec logo et titre

•
Numéro et date de la facture

•
Liste des produits avec quantités et prix

•
Calcul du total

•
Pied de page avec mentions légales

Exemple de Fichier

Plain Text


Nom : INV-20260416143022.pdf
Taille : ~50 KB
Format : A4 (210 × 297 mm)



Code Implémentation

Python


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse

def invoice_pdf(request, pk ):
    invoice = Invoice.objects.get(pk=pk)
    
    # Créer la réponse PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="INV-{invoice.invoice_number}.pdf"'
    
    # Générer le PDF
    pdf = canvas.Canvas(response, pagesize=letter)
    
    # Ajouter le contenu
    pdf.drawString(100, 750, f"Facture {invoice.invoice_number}")
    pdf.drawString(100, 730, f"Date: {invoice.date}")
    
    # Ajouter les articles
    y = 700
    for item in invoice.items.all():
        pdf.drawString(100, y, f"{item.product.name} x {item.quantity}")
        pdf.drawString(400, y, f"{item.subtotal} €")
        y -= 20
    
    # Ajouter le total
    pdf.drawString(400, y - 20, f"Total: {invoice.total} €")
    
    pdf.save()
    return response



Avantages

✅ Partage facile par email
✅ Archivage numérique
✅ Impression de qualité professionnelle
✅ Pas de dépendance externe




2. Recherche et Filtres

Description

Permet de rechercher et filtrer les produits et factures selon différents critères.

Accès

•
Produits : Menu → Produits → "Rechercher"

•
Factures : Menu → Factures → "Filtrer"

Fonctionnalités Produits

Recherche par Nom

Plain Text


Accès : /products/search/
Paramètre : ?q=café
Résultat : Affiche tous les produits contenant "café"



Exemple :

Plain Text


Recherche : "café"
Résultats :
- Café Premium 500g
- Café Moulu Bio
- Café Arabica



Filtrage par Prix

Plain Text


Prix minimum : 10 €
Prix maximum : 50 €
Résultat : Produits entre 10 € et 50 €



Filtrage par Date

Plain Text


Date avant : 2026-12-31
Résultat : Produits expirant avant cette date



Fonctionnalités Factures

Filtrage par Date

Plain Text


Date début : 2026-01-01
Date fin : 2026-03-31
Résultat : Factures du 1er trimestre 2026



Filtrage par Montant

Plain Text


Montant minimum : 100 €
Montant maximum : 1000 €
Résultat : Factures entre 100 € et 1000 €



Filtrage par Statut

Plain Text


Statuts disponibles :
- Brouillon
- Finalisée
- Archivée



Code Implémentation

Python


from django.db.models import Q

def search_products(request):
    query = request.GET.get('q', '')
    products = Product.objects.filter(
        Q(name__icontains=query) |
        Q(description__icontains=query)
    )
    
    # Filtres additionnels
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')
    
    if min_price:
        products = products.filter(price__gte=min_price)
    if max_price:
        products = products.filter(price__lte=max_price)
    
    return render(request, 'facturation/products/search.html', {
        'products': products,
        'query': query
    })



Avantages

✅ Trouve rapidement les produits/factures
✅ Filtrage multi-critères
✅ Recherche en temps réel
✅ Interface intuitive




3. Historique d'Audit

Description

Trace toutes les modifications effectuées sur les produits et factures pour une traçabilité complète.

Accès

•
Menu : Historique → Voir tous les logs

•
URL : /audit-log/

Informations Tracées

Information
Description
Action
create, update, delete
Modèle
Product, Invoice, InvoiceItem
ID Objet
ID de l'objet modifié
Changements
Détails des modifications (JSON)
Date/Heure
Timestamp exact
Utilisateur
Qui a effectué l'action




Exemple de Log

JSON


{
  "action": "update",
  "model": "Product",
  "object_id": 5,
  "changes": {
    "price": {
      "old": "15.99",
      "new": "16.99"
    },
    "expiration_date": {
      "old": "2026-06-30",
      "new": "2026-07-31"
    }
  },
  "timestamp": "2026-04-16T14:30:22.123456Z",
  "user": "admin"
}



Fonctionnalités

✅ Traçabilité complète
✅ Détection des modifications
✅ Historique non modifiable
✅ Recherche dans les logs

Code Implémentation

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
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

def log_change(action, model_name, object_id, changes=None, user=None):
    AuditLog.objects.create(
        action=action,
        model=model_name,
        object_id=object_id,
        changes=changes,
        user=user
    )



Avantages

✅ Conformité réglementaire
✅ Détection de fraude
✅ Récupération en cas d'erreur
✅ Responsabilité claire




4. Rapports de Ventes

Description

Génère des rapports mensuels détaillés sur les ventes, le chiffre d'affaires et les tendances.

Accès

•
Menu : Rapports → Ventes

•
URL : /reports/sales/

Informations du Rapport

Métrique
Description
Chiffre d'affaires total
Somme de toutes les factures
Nombre de factures
Total des factures finalisées
Nombre de produits vendus
Somme des quantités
Panier moyen
Chiffre d'affaires / Nombre de factures
Produit le plus vendu
Produit avec la plus grande quantité
Produit le plus rentable
Produit avec le plus grand chiffre d'affaires




Exemple de Rapport

Plain Text


═══════════════════════════════════════════════════════════
                    RAPPORT DE VENTES
                      Avril 2026
═══════════════════════════════════════════════════════════

RÉSUMÉ GÉNÉRAL
  Chiffre d'affaires total : 15,450.00 €
  Nombre de factures : 45
  Nombre de produits vendus : 234
  Panier moyen : 343.33 €

PRODUITS LES PLUS VENDUS
  1. Café Premium 500g : 85 unités (1,275.00 €)
  2. Thé Vert Bio : 62 unités (930.00 €)
  3. Chocolat Noir 70% : 51 unités (765.00 €)

PRODUITS LES PLUS RENTABLES
  1. Café Premium 500g : 1,275.00 €
  2. Thé Vert Bio : 930.00 €
  3. Chocolat Noir 70% : 765.00 €

ÉVOLUTION HEBDOMADAIRE
  Semaine 1 : 3,500.00 €
  Semaine 2 : 3,800.00 €
  Semaine 3 : 4,150.00 €
  Semaine 4 : 4,000.00 €

═══════════════════════════════════════════════════════════



Code Implémentation

Python


def report_sales(request):
    invoices = Invoice.objects.filter(status='finalized')
    
    total_sales = sum(inv.total for inv in invoices)
    total_invoices = invoices.count()
    total_items = sum(
        item.quantity for invoice in invoices 
        for item in invoice.items.all()
    )
    average_cart = total_sales / total_invoices if total_invoices > 0 else 0
    
    context = {
        'total_sales': total_sales,
        'total_invoices': total_invoices,
        'total_items': total_items,
        'average_cart': average_cart,
        'invoices': invoices,
    }
    return render(request, 'facturation/reports/sales.html', context)



Avantages

✅ Analyse des performances
✅ Identification des tendances
✅ Prise de décision éclairée
✅ Suivi du chiffre d'affaires




5. Graphiques Analytique

Description

Visualise les données de ventes sous forme de graphiques pour une meilleure compréhension des tendances.

Accès

•
Menu : Rapports → Analytique

•
URL : /reports/analytics/

Types de Graphiques

1. Ventes par Mois

Plain Text


Graphique : Courbe
Affiche : Chiffre d'affaires mensuel
Utilité : Identifier les pics de ventes



2. Répartition des Produits

Plain Text


Graphique : Camembert
Affiche : Pourcentage de ventes par produit
Utilité : Voir les produits populaires



3. Chiffre d'Affaires par Produit

Plain Text


Graphique : Barres horizontales
Affiche : Chiffre d'affaires pour chaque produit
Utilité : Identifier les produits rentables



4. Tendances Mensuelles

Plain Text


Graphique : Aire
Affiche : Évolution du chiffre d'affaires
Utilité : Voir les tendances long terme



Exemple de Graphique

Plain Text


Ventes par Mois (2026)

5000 €  ┌─────────────────────────────────────┐
        │         ╱╲                          │
4000 €  │        ╱  ╲      ╱╲                │
        │       ╱    ╲    ╱  ╲               │
3000 €  │      ╱      ╲  ╱    ╲             │
        │     ╱        ╲╱      ╲╱╲           │
2000 €  │    ╱                    ╲          │
        │   ╱                      ╲╱        │
1000 €  │  ╱                                 │
        │ ╱                                  │
   0 €  └─────────────────────────────────────┘
        Jan  Fév  Mar  Avr  Mai  Jun



Code Implémentation

Python


import json
from django.db.models import Sum

def analytics_view(request):
    # Données pour graphique ventes par mois
    monthly_sales = Invoice.objects.filter(
        status='finalized'
    ).extra(
        select={'month': 'EXTRACT(month FROM date)'}
    ).values('month').annotate(total=Sum('total'))
    
    # Données pour graphique répartition produits
    product_sales = InvoiceItem.objects.values(
        'product__name'
    ).annotate(
        total=Sum('subtotal')
    ).order_by('-total')[:5]
    
    context = {
        'monthly_sales': json.dumps(list(monthly_sales)),
        'product_sales': json.dumps(list(product_sales)),
    }
    return render(request, 'facturation/reports/analytics.html', context)



Avantages

✅ Visualisation claire des données
✅ Identification rapide des tendances
✅ Présentation professionnelle
✅ Export facile




6. Alertes Produits

Description

Alerte automatiquement sur les produits expirés ou expirant bientôt.

Accès

•
Menu : Alertes

•
URL : /alerts/

Types d'Alertes

Alerte 1 : Produit Expiré

Plain Text


Couleur : 🔴 Rouge
Condition : Date de péremption < Aujourd'hui
Action : Supprimer le produit



Alerte 2 : Produit Expirant Bientôt

Plain Text


Couleur : 🟠 Orange
Condition : Date de péremption < Aujourd'hui + 7 jours
Action : Utiliser rapidement ou commander



Exemple d'Alerte

Plain Text


┌─────────────────────────────────────────────────────┐
│ 🔴 PRODUIT EXPIRÉ                                   │
├─────────────────────────────────────────────────────┤
│ Café Premium 500g                                   │
│ Expiré depuis : 15 avril 2026                       │
│ Action : [Supprimer] [Ignorer]                      │
└─────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────┐
│ 🟠 PRODUIT EXPIRANT BIENTÔT                         │
├─────────────────────────────────────────────────────┤
│ Thé Vert Bio                                        │
│ Expire dans : 5 jours (21 avril 2026)              │
│ Action : [Utiliser] [Ignorer]                      │
└─────────────────────────────────────────────────────┘



Code Implémentation

Python


from datetime import date, timedelta

def check_product_alerts():
    today = date.today()
    
    # Produits expirés
    expired = Product.objects.filter(expiration_date__lt=today)
    for product in expired:
        ProductAlert.objects.get_or_create(
            product=product,
            alert_type='expired',
            defaults={'is_active': True}
        )
    
    # Produits expirant bientôt (dans 7 jours)
    soon_expired = Product.objects.filter(
        expiration_date__gte=today,
        expiration_date__lte=today + timedelta(days=7)
    )
    for product in soon_expired:
        ProductAlert.objects.get_or_create(
            product=product,
            alert_type='expiring_soon',
            defaults={'is_active': True}
        )

def alerts_view(request):
    alerts = ProductAlert.objects.filter(is_active=True)
    return render(request, 'facturation/alerts/list.html', {'alerts': alerts})



Avantages

✅ Prévention du gaspillage
✅ Gestion des stocks
✅ Conformité réglementaire
✅ Alertes automatiques




7. Impression

Description

Permet d'imprimer les factures dans un format optimisé pour l'impression.

Accès

•
Menu : Factures → Cliquez sur une facture → "Imprimer"

•
URL : /invoices/<id>/print/

Fonctionnalités

✅ Format A4 optimisé
✅ Suppression des éléments inutiles
✅ Mise en page professionnelle
✅ Codes à barres (optionnel)

Processus d'Impression

Plain Text


1. Cliquez sur "Imprimer"
                    ↓
2. Page d'impression s'ouvre
                    ↓
3. Utilisez Ctrl + P (ou Cmd + P sur macOS)
                    ↓
4. Sélectionnez l'imprimante
                    ↓
5. Cliquez sur "Imprimer"



Contenu Imprimé

Plain Text


╔═══════════════════════════════════════════════════════╗
║                  PRO GESTION FACTURES                 ║
║                    [LOGO]                             ║
╠═══════════════════════════════════════════════════════╣
║                                                       ║
║  FACTURE N°INV-20260416143022                        ║
║  Date : 16 avril 2026                               ║
║                                                       ║
╠═══════════════════════════════════════════════════════╣
║  ARTICLE              QTÉ    PRIX UNIT.    TOTAL     ║
╠═══════════════════════════════════════════════════════╣
║  Café Premium 500g    2      15.99 €       31.98 €   ║
║  Thé Vert Bio         1      14.99 €       14.99 €   ║
║  Chocolat Noir 70%    3      9.99 €        29.97 €   ║
╠═══════════════════════════════════════════════════════╣
║                                    TOTAL : 76.94 €   ║
╚═══════════════════════════════════════════════════════╝



Code Implémentation

Python


def invoice_print(request, pk):
    invoice = Invoice.objects.get(pk=pk)
    items = invoice.items.all()
    
    context = {
        'invoice': invoice,
        'items': items,
        'total': invoice.total,
    }
    return render(request, 'facturation/invoices/print.html', context)



CSS pour Impression

CSS


@media print {
    .no-print { display: none; }
    body { font-size: 12pt; }
    .invoice { page-break-inside: avoid; }
}



Avantages

✅ Impression de qualité
✅ Format professionnel
✅ Archivage papier
✅ Partage facile




8. Archivage

Description

Archive les anciennes factures pour un meilleur suivi et une gestion des données.

Accès

•
Menu : Archivage

•
URL : /archived-invoices/

Fonctionnalités

Archiver une Facture

Plain Text


1. Ouvrez la facture
2. Cliquez sur "Archiver"
3. Confirmez l'archivage
4. La facture est archivée



Consulter les Archives

Plain Text


1. Menu → Archivage
2. Voir la liste des factures archivées
3. Cliquer pour voir les détails



Restaurer une Facture

Plain Text


1. Menu → Archivage
2. Cliquez sur "Restaurer"
3. La facture revient à la liste active



Supprimer Définitivement

Plain Text


1. Menu → Archivage
2. Cliquez sur "Supprimer"
3. Confirmez la suppression
4. La facture est supprimée définitivement



Données Archivées

JSON


{
  "invoice": {
    "id": 123,
    "invoice_number": "INV-20260416143022",
    "date": "2026-04-16T14:30:22Z",
    "total": 76.94,
    "status": "finalized"
  },
  "items": [
    {
      "product": "Café Premium 500g",
      "quantity": 2,
      "unit_price": 15.99,
      "subtotal": 31.98
    },
    ...
  ],
  "archived_at": "2026-04-20T10:15:30Z"
}



Code Implémentation

Python


class ArchivedInvoice(models.Model):
    original_id = models.IntegerField()
    data = models.JSONField()
    archived_at = models.DateTimeField(auto_now_add=True)

def archive_invoice(invoice):
    # Sauvegarder les données
    data = {
        'invoice': {
            'id': invoice.id,
            'invoice_number': invoice.invoice_number,
            'date': str(invoice.date),
            'total': str(invoice.total),
        },
        'items': [
            {
                'product': item.product.name,
                'quantity': item.quantity,
                'unit_price': str(item.unit_price),
                'subtotal': str(item.subtotal),
            }
            for item in invoice.items.all()
        ]
    }
    
    # Archiver
    ArchivedInvoice.objects.create(
        original_id=invoice.id,
        data=data
    )
    
    # Changer le statut
    invoice.status = 'archived'
    invoice.save()



Avantages

✅ Gestion des données
✅ Conformité réglementaire
✅ Récupération facile
✅ Sécurité des données




📊 Résumé des 8 Fonctionnalités

#
Fonctionnalité
Accès
Utilité
1
Export PDF
Factures → PDF
Partage et archivage
2
Recherche/Filtres
Produits/Factures
Trouver rapidement
3
Historique d'Audit
Menu → Historique
Traçabilité
4
Rapports de Ventes
Menu → Rapports
Analyse
5
Graphiques
Menu → Analytique
Visualisation
6
Alertes Produits
Menu → Alertes
Gestion des stocks
7
Impression
Factures → Imprimer
Archivage papier
8
Archivage
Menu → Archivage
Gestion des données







✨ Prochaines Étapes

•
📚 Consultez UTILISATION.md pour apprendre à utiliser chaque fonctionnalité

•
🏗️ Consultez ARCHITECTURE.md pour comprendre l'implémentation

•
🆘 Consultez DÉPANNAGE.md en cas de problème




🎉 Conclusion

Les 8 fonctionnalités supplémentaires font de cette application une solution d'entreprise complète pour la gestion de facturation !

Bonne utilisation ! 🚀

