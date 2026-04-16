from reportlab.lib.pagesizes import letter, A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.units import inch
from io import BytesIO
from datetime import datetime, timedelta
from django.db.models import Sum, Count, Q
from .models import Invoice, Product, AuditLog, ProductAlert
import json

def generate_invoice_pdf(invoice):
    """Génère un PDF pour une facture"""
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, topMargin=0.5*inch)
    elements = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#2c3e50'),
        spaceAfter=30,
    )
    
    # Titre
    elements.append(Paragraph(f"Facture N°{invoice.id}", title_style))
    elements.append(Spacer(1, 0.3*inch))
    
    # Informations
    info_data = [
        ['Date:', invoice.created_at.strftime('%d/%m/%Y %H:%M')],
        ['Total:', f'{invoice.total}€'],
    ]
    info_table = Table(info_data, colWidths=[2*inch, 2*inch])
    info_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 12),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(info_table)
    elements.append(Spacer(1, 0.3*inch))
    
    # Tableau des articles
    data = [['Produit', 'Quantité', 'Prix unitaire', 'Sous-total']]
    for item in invoice.items.all():
        data.append([
            item.product.name,
            str(item.quantity),
            f'{item.unit_price}€',
            f'{item.get_subtotal()}€'
        ])
    
    table = Table(data, colWidths=[2.5*inch, 1.5*inch, 1.5*inch, 1.5*inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black)
    ]))
    elements.append(table)
    elements.append(Spacer(1, 0.3*inch))
    
    # Total
    total_text = Paragraph(f"<b>Total à payer: {invoice.total}€</b>", styles['Heading2'])
    elements.append(total_text)
    
    doc.build(elements)
    buffer.seek(0)
    return buffer

def log_audit(action, model_name, object_id, object_repr, changes=''):
    """Enregistre une action dans l'historique"""
    AuditLog.objects.create(
        action=action,
        model_name=model_name,
        object_id=object_id,
        object_repr=object_repr,
        changes=changes
    )

def archive_invoice(invoice):
    """Archive une facture"""
    from .models import ArchivedInvoice
    
    data = {
        'items': [
            {
                'product': item.product.name,
                'quantity': item.quantity,
                'unit_price': str(item.unit_price),
                'subtotal': str(item.get_subtotal())
            }
            for item in invoice.items.all()
        ]
    }
    
    ArchivedInvoice.objects.create(
        invoice_id=invoice.id,
        invoice_number=f'#{invoice.id}',
        total=invoice.total,
        created_at=invoice.created_at,
        data=data
    )

def check_product_expiration():
    """Vérifie les produits expirés et crée des alertes"""
    today = datetime.now().date()
    soon = today + timedelta(days=7)
    
    # Produits expirés
    expired_products = Product.objects.filter(expiration_date__lt=today)
    for product in expired_products:
        if not ProductAlert.objects.filter(product=product, alert_type='EXPIRED').exists():
            ProductAlert.objects.create(product=product, alert_type='EXPIRED')
    
    # Produits expirant bientôt
    expiring_soon = Product.objects.filter(
        expiration_date__gte=today,
        expiration_date__lte=soon
    )
    for product in expiring_soon:
        if not ProductAlert.objects.filter(product=product, alert_type='EXPIRING_SOON').exists():
            ProductAlert.objects.create(product=product, alert_type='EXPIRING_SOON')

def get_sales_report(start_date=None, end_date=None):
    """Génère un rapport de ventes"""
    if not start_date:
        start_date = datetime.now().date().replace(day=1)
    if not end_date:
        end_date = datetime.now().date()
    
    invoices = Invoice.objects.filter(
        created_at__date__gte=start_date,
        created_at__date__lte=end_date
    )
    
    return {
        'total_invoices': invoices.count(),
        'total_revenue': invoices.aggregate(Sum('total'))['total__sum'] or 0,
        'average_invoice': invoices.aggregate(Sum('total'))['total__sum'] / invoices.count() if invoices.count() > 0 else 0,
        'invoices': invoices
    }
