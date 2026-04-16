from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal

class Product(models.Model):
    """Modèle pour les produits"""
    name = models.CharField(max_length=255, verbose_name="Nom du produit")
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.01'))],
        verbose_name="Prix"
    )
    expiration_date = models.DateField(verbose_name="Date de péremption")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Produit"
        verbose_name_plural = "Produits"

    def __str__(self):
        return f"{self.name} - {self.price}€"


class Invoice(models.Model):
    """Modèle pour les factures"""
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Date de création")
    updated_at = models.DateTimeField(auto_now=True)
    total = models.DecimalField(
        max_digits=12, 
        decimal_places=2, 
        default=0,
        verbose_name="Total"
    )

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Facture"
        verbose_name_plural = "Factures"

    def __str__(self):
        return f"Facture #{self.id} - {self.created_at.strftime('%d/%m/%Y')}"

    def calculate_total(self):
        """Calcule le total de la facture"""
        total = sum(item.get_subtotal() for item in self.items.all())
        self.total = total
        self.save()
        return total

    def get_total_quantity(self):
        """Retourne le nombre total de produits"""
        return sum(item.quantity for item in self.items.all())


class InvoiceItem(models.Model):
    """Modèle pour les articles d'une facture"""
    invoice = models.ForeignKey(
        Invoice, 
        on_delete=models.CASCADE, 
        related_name='items',
        verbose_name="Facture"
    )
    product = models.ForeignKey(
        Product, 
        on_delete=models.PROTECT,
        verbose_name="Produit"
    )
    quantity = models.IntegerField(
        validators=[MinValueValidator(1)],
        verbose_name="Quantité"
    )
    unit_price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name="Prix unitaire"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Article de facture"
        verbose_name_plural = "Articles de facture"
        unique_together = ['invoice', 'product']

    def __str__(self):
        return f"{self.product.name} x{self.quantity}"

    def get_subtotal(self):
        """Calcule le sous-total de l'article"""
        return self.quantity * self.unit_price


class AuditLog(models.Model):
    """Modèle pour l'historique des modifications"""
    ACTIONS = [
        ('CREATE', 'Création'),
        ('UPDATE', 'Modification'),
        ('DELETE', 'Suppression'),
    ]
    
    action = models.CharField(max_length=10, choices=ACTIONS)
    model_name = models.CharField(max_length=50)
    object_id = models.IntegerField()
    object_repr = models.CharField(max_length=255)
    changes = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Historique"
        verbose_name_plural = "Historiques"
    
    def __str__(self):
        return f"{self.get_action_display()} - {self.model_name} ({self.timestamp})"


class ArchivedInvoice(models.Model):
    """Modèle pour les factures archivées"""
    invoice_id = models.IntegerField(unique=True)
    invoice_number = models.CharField(max_length=50)
    total = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField()
    archived_at = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()  # Données complètes de la facture
    
    class Meta:
        ordering = ['-archived_at']
        verbose_name = "Facture archivée"
        verbose_name_plural = "Factures archivées"
    
    def __str__(self):
        return f"Facture archivée #{self.invoice_number}"


class ProductAlert(models.Model):
    """Modèle pour les alertes de produits expirés"""
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='alerts')
    alert_type = models.CharField(max_length=20, choices=[
        ('EXPIRING_SOON', 'Expiration proche'),
        ('EXPIRED', 'Expiré'),
    ])
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Alerte produit"
        verbose_name_plural = "Alertes produits"
    
    def __str__(self):
        return f"Alerte {self.product.name}"
