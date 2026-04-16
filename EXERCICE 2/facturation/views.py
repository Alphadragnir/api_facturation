from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Sum
from django.views.decorators.http import require_http_methods
from .models import Product, Invoice, InvoiceItem
from datetime import datetime

# ============ AUTHENTIFICATION ============

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, 'Identifiants invalides')
    return render(request, 'facturation/login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')
        
        if password != password_confirm:
            messages.error(request, 'Les mots de passe ne correspondent pas')
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Cet utilisateur existe déjà')
            return redirect('register')
        
        User.objects.create_user(username=username, password=password)
        messages.success(request, 'Inscription réussie. Connectez-vous.')
        return redirect('login')
    
    return render(request, 'facturation/register.html')

def logout_view(request):
    logout(request)
    return redirect('login')

# ============ PRODUITS ============

@login_required(login_url='login')
def product_list(request):
    products = Product.objects.all()
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'facturation/product_list.html', {'page_obj': page_obj})

@login_required(login_url='login')
def product_create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        expiration_date = request.POST.get('expiration_date')
        
        Product.objects.create(
            name=name,
            price=price,
            expiration_date=expiration_date
        )
        messages.success(request, 'Produit créé avec succès')
        return redirect('product_list')
    
    return render(request, 'facturation/product_form.html')

@login_required(login_url='login')
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    if request.method == 'POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.expiration_date = request.POST.get('expiration_date')
        product.save()
        messages.success(request, 'Produit modifié avec succès')
        return redirect('product_list')
    
    return render(request, 'facturation/product_form.html', {'product': product})

@login_required(login_url='login')
@require_http_methods(["POST"])
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    messages.success(request, 'Produit supprimé avec succès')
    return redirect('product_list')

# ============ FACTURES ============

@login_required(login_url='login')
def invoice_list(request):
    invoices = Invoice.objects.all()
    paginator = Paginator(invoices, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'facturation/invoice_list.html', {'page_obj': page_obj})

@login_required(login_url='login')
def invoice_detail(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    items = invoice.items.all()
    total_quantity = invoice.get_total_quantity()
    return render(request, 'facturation/invoice_detail.html', {
        'invoice': invoice,
        'items': items,
        'total_quantity': total_quantity
    })

@login_required(login_url='login')
def invoice_create(request):
    if request.method == 'POST':
        # Créer la facture
        invoice = Invoice.objects.create(total=0)
        
        # Ajouter les articles
        products = Product.objects.all()
        for product in products:
            quantity = request.POST.get(f'quantity_{product.id}')
            if quantity and int(quantity) > 0:
                InvoiceItem.objects.create(
                    invoice=invoice,
                    product=product,
                    quantity=int(quantity),
                    unit_price=product.price
                )
        
        # Calculer le total
        invoice.calculate_total()
        
        messages.success(request, 'Facture créée avec succès')
        return redirect('invoice_detail', pk=invoice.id)
    
    products = Product.objects.all()
    return render(request, 'facturation/invoice_form.html', {'products': products})

@login_required(login_url='login')
@require_http_methods(["POST"])
def invoice_delete(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    invoice.delete()
    messages.success(request, 'Facture supprimée avec succès')
    return redirect('invoice_list')

@login_required(login_url='login')
def dashboard(request):
    total_products = Product.objects.count()
    total_invoices = Invoice.objects.count()
    total_revenue = Invoice.objects.aggregate(Sum('total'))['total__sum'] or 0
    
    return render(request, 'facturation/dashboard.html', {
        'total_products': total_products,
        'total_invoices': total_invoices,
        'total_revenue': total_revenue
    })


# ============ EXPORT PDF ET IMPRESSION ============

from django.http import HttpResponse
from .utils import generate_invoice_pdf, log_audit, archive_invoice, check_product_expiration, get_sales_report

@login_required(login_url='login')
def invoice_pdf(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    pdf_buffer = generate_invoice_pdf(invoice)
    response = HttpResponse(pdf_buffer, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="facture_{invoice.id}.pdf"'
    return response

@login_required(login_url='login')
def invoice_print(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    items = invoice.items.all()
    total_quantity = invoice.get_total_quantity()
    return render(request, 'facturation/invoice_print.html', {
        'invoice': invoice,
        'items': items,
        'total_quantity': total_quantity
    })

# ============ RECHERCHE ET FILTRES ============

@login_required(login_url='login')
def product_search(request):
    query = request.GET.get('q', '')
    products = Product.objects.all()
    
    if query:
        products = products.filter(Q(name__icontains=query))
    
    paginator = Paginator(products, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'facturation/product_search.html', {
        'page_obj': page_obj,
        'query': query
    })

@login_required(login_url='login')
def invoice_filter(request):
    invoices = Invoice.objects.all()
    
    # Filtrer par date
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    min_amount = request.GET.get('min_amount')
    max_amount = request.GET.get('max_amount')
    
    if start_date:
        invoices = invoices.filter(created_at__date__gte=start_date)
    if end_date:
        invoices = invoices.filter(created_at__date__lte=end_date)
    if min_amount:
        invoices = invoices.filter(total__gte=min_amount)
    if max_amount:
        invoices = invoices.filter(total__lte=max_amount)
    
    paginator = Paginator(invoices, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'facturation/invoice_filter.html', {
        'page_obj': page_obj,
        'start_date': start_date,
        'end_date': end_date,
        'min_amount': min_amount,
        'max_amount': max_amount
    })

# ============ HISTORIQUE ============

@login_required(login_url='login')
def audit_log_view(request):
    from .models import AuditLog
    logs = AuditLog.objects.all()
    paginator = Paginator(logs, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'facturation/audit_log.html', {'page_obj': page_obj})

# ============ RAPPORTS ET GRAPHIQUES ============

@login_required(login_url='login')
def sales_report(request):
    from datetime import datetime, timedelta
    
    # Rapport du mois courant
    today = datetime.now().date()
    start_date = request.GET.get('start_date', today.replace(day=1))
    end_date = request.GET.get('end_date', today)
    
    report = get_sales_report(start_date, end_date)
    
    # Données pour graphique
    invoices_by_day = {}
    for invoice in report['invoices']:
        day = invoice.created_at.date()
        if day not in invoices_by_day:
            invoices_by_day[day] = 0
        invoices_by_day[day] += invoice.total
    
    return render(request, 'facturation/sales_report.html', {
        'report': report,
        'invoices_by_day': invoices_by_day,
        'start_date': start_date,
        'end_date': end_date
    })

@login_required(login_url='login')
def dashboard_analytics(request):
    from datetime import datetime, timedelta
    
    # Statistiques
    total_products = Product.objects.count()
    total_invoices = Invoice.objects.count()
    total_revenue = Invoice.objects.aggregate(Sum('total'))['total__sum'] or 0
    
    # Produits expirés
    today = datetime.now().date()
    expired_products = Product.objects.filter(expiration_date__lt=today).count()
    
    # Factures du mois
    month_start = today.replace(day=1)
    month_invoices = Invoice.objects.filter(created_at__date__gte=month_start).count()
    month_revenue = Invoice.objects.filter(created_at__date__gte=month_start).aggregate(Sum('total'))['total__sum'] or 0
    
    return render(request, 'facturation/dashboard_analytics.html', {
        'total_products': total_products,
        'total_invoices': total_invoices,
        'total_revenue': total_revenue,
        'expired_products': expired_products,
        'month_invoices': month_invoices,
        'month_revenue': month_revenue
    })

# ============ ALERTES PRODUITS EXPIRÉS ============

@login_required(login_url='login')
def product_alerts(request):
    from .models import ProductAlert
    
    check_product_expiration()
    alerts = ProductAlert.objects.filter(is_read=False)
    
    if request.method == 'POST':
        alert_id = request.POST.get('alert_id')
        alert = get_object_or_404(ProductAlert, id=alert_id)
        alert.is_read = True
        alert.save()
        return redirect('product_alerts')
    
    return render(request, 'facturation/product_alerts.html', {'alerts': alerts})

# ============ ARCHIVAGE ============

@login_required(login_url='login')
def archive_invoice_view(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    archive_invoice(invoice)
    log_audit('DELETE', 'Invoice', invoice.id, str(invoice), 'Archivée')
    invoice.delete()
    messages.success(request, 'Facture archivée avec succès')
    return redirect('invoice_list')

@login_required(login_url='login')
def archived_invoices(request):
    from .models import ArchivedInvoice
    archived = ArchivedInvoice.objects.all()
    paginator = Paginator(archived, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'facturation/archived_invoices.html', {'page_obj': page_obj})

# ============ MENTIONS LÉGALES ============

def legal_view(request):
    """Affiche les mentions légales"""
    return render(request, 'facturation/legal.html')
