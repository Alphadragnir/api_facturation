from django.urls import path
from . import views

urlpatterns = [
    # Authentification
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    
    # Dashboard
    path('', views.dashboard, name='dashboard'),
    
    # Produits
    path('products/', views.product_list, name='product_list'),
    path('products/create/', views.product_create, name='product_create'),
    path('products/<int:pk>/edit/', views.product_update, name='product_update'),
    path('products/<int:pk>/delete/', views.product_delete, name='product_delete'),
    
    # Factures
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/create/', views.invoice_create, name='invoice_create'),
    path('invoices/<int:pk>/', views.invoice_detail, name='invoice_detail'),
    path('invoices/<int:pk>/delete/', views.invoice_delete, name='invoice_delete'),
    
    # Export et impression
    path('invoices/<int:pk>/pdf/', views.invoice_pdf, name='invoice_pdf'),
    path('invoices/<int:pk>/print/', views.invoice_print, name='invoice_print'),
    
    # Recherche et filtres
    path('products/search/', views.product_search, name='product_search'),
    path('invoices/filter/', views.invoice_filter, name='invoice_filter'),
    
    # Historique
    path('audit-log/', views.audit_log_view, name='audit_log'),
    
    # Rapports et graphiques
    path('reports/sales/', views.sales_report, name='sales_report'),
    path('dashboard/analytics/', views.dashboard_analytics, name='dashboard_analytics'),
    
    # Alertes
    path('alerts/', views.product_alerts, name='product_alerts'),
    
    # Archivage
    path('invoices/<int:pk>/archive/', views.archive_invoice_view, name='archive_invoice'),
    path('archived-invoices/', views.archived_invoices, name='archived_invoices'),
    
    # Mentions légales
    path('legal/', views.legal_view, name='legal'),
]
