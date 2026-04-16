📚 UTILISATION - Guide Complet

📋 Table des Matières

1.
Connexion

2.
Tableau de Bord

3.
Gestion des Produits

4.
Gestion des Factures

5.
Fonctionnalités Avancées

6.
Conseils Pratiques




🔐 Connexion

Accès à l'Application

1.
Ouvrez votre navigateur

2.
Allez à http://localhost:8000/

3.
Vous verrez la page de connexion

Comptes de Test

Utilisateur
Mot de passe
admin
admin123
user
user123




Processus de Connexion

1.
Entrez votre nom d'utilisateur

2.
Entrez votre mot de passe

3.
Cliquez sur "Se connecter"

4.
Vous serez redirigé vers le tableau de bord

Déconnexion

1.
Cliquez sur "Déconnexion" dans le menu

2.
Vous serez redirigé vers la page de connexion




📊 Tableau de Bord

Vue d'Ensemble

Le tableau de bord affiche :

•
✅ Nombre total de produits

•
✅ Nombre total de factures

•
✅ Chiffre d'affaires total

•
✅ Produits expirés (alertes )

•
✅ Liens rapides vers les fonctionnalités

Navigation Principale

Sidebar (Menu Gauche) :

•
🏠 Accueil - Tableau de bord

•
📦 Produits - Gestion des produits

•
📄 Factures - Gestion des factures

•
📊 Rapports - Rapports et analytique

•
🔔 Alertes - Alertes produits

•
📋 Historique - Historique d'audit

•
📦 Archivage - Factures archivées

•
⚙️ Admin - Interface admin Django




📦 Gestion des Produits

Afficher la Liste des Produits

1.
Cliquez sur "Produits" dans le menu

2.
Vous verrez la liste des produits avec pagination (10 par page)

Colonnes affichées :

•
ID

•
Nom

•
Prix

•
Date de péremption

•
Actions (Modifier, Supprimer)

Créer un Produit

1.
Cliquez sur "Ajouter un produit"

2.
Remplissez le formulaire :

•
Nom : Nom du produit (ex: "Café Premium")

•
Prix : Prix unitaire (ex: 15.99)

•
Date de péremption : Date d'expiration (ex: 2026-12-31)



3.
Cliquez sur "Créer"

4.
Le produit apparaît dans la liste

Modifier un Produit

1.
Dans la liste des produits, cliquez sur "Modifier"

2.
Modifiez les champs souhaités

3.
Cliquez sur "Mettre à jour"

4.
Les modifications sont sauvegardées

Supprimer un Produit

1.
Dans la liste des produits, cliquez sur "Supprimer"

2.
Confirmez la suppression

3.
Le produit est supprimé et n'apparaît plus dans la liste

⚠️ Attention : La suppression est définitive !

Rechercher un Produit

1.
Allez à "Produits" → "Rechercher"

2.
Entrez le nom du produit

3.
Cliquez sur "Rechercher"

4.
Les résultats s'affichent

Filtrer les Produits

1.
Allez à "Produits" → "Filtrer"

2.
Définissez les critères :

•
Prix minimum : ex: 10

•
Prix maximum : ex: 50

•
Date de péremption : ex: 2026-06-30



3.
Cliquez sur "Appliquer les filtres"

4.
Les produits correspondants s'affichent




📄 Gestion des Factures

Afficher la Liste des Factures

1.
Cliquez sur "Factures" dans le menu

2.
Vous verrez la liste des factures avec pagination (10 par page)

Colonnes affichées :

•
Numéro de facture

•
Date

•
Nombre de produits

•
Total

•
Statut

•
Actions (Détail, Imprimer, PDF, Supprimer)

Créer une Facture

1.
Cliquez sur "Créer une facture"

2.
Sélectionnez les produits :

•
Cochez les produits à inclure

•
Définissez la quantité pour chaque produit



3.
Le total se calcule automatiquement

4.
Cliquez sur "Créer la facture"

5.
La facture est créée et affichée

Consulter le Détail d'une Facture

1.
Dans la liste des factures, cliquez sur le numéro de facture

2.
Vous verrez :

•
Numéro et date de la facture

•
Liste des produits inclus

•
Quantités et prix unitaires

•
Sous-totaux

•
Total à payer (calculé automatiquement)

•
Nombre total de produits



Imprimer une Facture

1.
Dans la liste des factures, cliquez sur "Imprimer"

2.
Une version imprimable s'ouvre

3.
Utilisez Ctrl + P (ou Cmd + P sur macOS) pour imprimer

Exporter en PDF

1.
Dans la liste des factures, cliquez sur "PDF"

2.
Le fichier PDF se télécharge automatiquement

3.
Vous pouvez l'ouvrir, l'imprimer ou l'envoyer

Supprimer une Facture

1.
Dans la liste des factures, cliquez sur "Supprimer"

2.
Confirmez la suppression

3.
La facture est supprimée

⚠️ Attention : La suppression est définitive !

Archiver une Facture

1.
Dans le détail d'une facture, cliquez sur "Archiver"

2.
La facture est archivée et déplacée

3.
Elle reste consultable dans la section "Archivage"




🚀 Fonctionnalités Avancées

1. Rapports de Ventes

Accès : Menu → "Rapports" → "Ventes"

Fonctionnalités :

•
Générer un rapport mensuel

•
Voir le chiffre d'affaires total

•
Voir le nombre de factures

•
Voir le nombre de produits vendus

•
Exporter le rapport

2. Graphiques Analytique

Accès : Menu → "Rapports" → "Analytique"

Graphiques disponibles :

•
📈 Ventes par mois

•
🥧 Répartition des produits

•
💰 Chiffre d'affaires par produit

•
📊 Tendances mensuelles

3. Alertes Produits

Accès : Menu → "Alertes"

Types d'alertes :

•
🔴 Produits expirés - Affichés en rouge

•
🟠 Produits expirant bientôt - Affichés en orange (dans 7 jours)

Actions :

•
Voir la liste des produits en alerte

•
Modifier ou supprimer les produits

•
Marquer l'alerte comme traitée

4. Historique d'Audit

Accès : Menu → "Historique"

Informations tracées :

•
Action effectuée (création, modification, suppression)

•
Type d'objet (produit, facture)

•
Détails des modifications

•
Date et heure

•
Utilisateur

5. Archivage

Accès : Menu → "Archivage"

Fonctionnalités :

•
Voir les factures archivées

•
Restaurer une facture archivée

•
Supprimer définitivement une facture archivée

•
Rechercher dans les archives

6. Admin Django

Accès : Menu → "Admin" ou http://localhost:8000/admin/

Fonctionnalités :

•
Gérer les utilisateurs

•
Gérer les produits (interface admin )

•
Gérer les factures (interface admin)

•
Gérer les alertes

•
Gérer les logs d'audit




💡 Conseils Pratiques

Gestion Efficace des Produits

✅ Créez des produits avec des noms clairs

Plain Text


❌ Mauvais : "Prod1", "Truc"
✅ Bon : "Café Premium 500g", "Thé Vert Bio"



✅ Mettez à jour régulièrement les dates de péremption

•
Vérifiez les alertes chaque semaine

•
Supprimez les produits expirés

✅ Utilisez les prix corrects

•
Vérifiez les prix avant de créer une facture

•
Mettez à jour les prix si nécessaire

Gestion Efficace des Factures

✅ Créez des factures claires

•
Sélectionnez les bons produits

•
Définissez les bonnes quantités

•
Vérifiez le total avant de valider

✅ Archivez régulièrement

•
Archivez les factures de plus de 6 mois

•
Gardez les factures récentes actives

✅ Utilisez les rapports

•
Générez des rapports mensuels

•
Analysez les tendances

•
Identifiez les produits populaires

Utilisation des Alertes

✅ Consultez les alertes régulièrement

•
Vérifiez les produits expirés

•
Agissez rapidement

✅ Marquez les alertes comme traitées

•
Supprimez les produits expirés

•
Mettez à jour les produits

Sécurité

✅ Changez votre mot de passe régulièrement

Plain Text


Accès : Admin Django → Utilisateurs → Changer le mot de passe



✅ Consultez l'historique d'audit

•
Vérifiez qui a fait quoi

•
Identifiez les modifications suspectes

✅ Sauvegardez régulièrement

•
Exportez les rapports

•
Archivez les factures importantes




🆘 Problèmes Courants

Problème : "Je ne vois pas mes produits"

Cause : Vous n'avez pas créé de produits

Solution :

1.
Cliquez sur "Ajouter un produit"

2.
Créez votre premier produit

3.
Il apparaîtra dans la liste

Problème : "Le total de la facture est incorrect"

Cause : Erreur dans les quantités ou prix

Solution :

1.
Vérifiez les quantités

2.
Vérifiez les prix des produits

3.
Recréez la facture si nécessaire

Problème : "Je ne peux pas supprimer un produit"

Cause : Le produit est utilisé dans une facture

Solution :

1.
Archivez ou supprimez la facture

2.
Puis supprimez le produit

Problème : "Les alertes ne s'affichent pas"

Cause : Pas de produits expirés

Solution :

1.
Créez un produit avec une date de péremption passée

2.
L'alerte apparaîtra automatiquement




📞 Support

Pour toute question ou problème :

1.
Consultez DÉPANNAGE.md

2.
Consultez ARCHITECTURE.md

3.
Consultez COMMANDES.md




✨ Prochaines Étapes

•
📊 Explorez les rapports et graphiques

•
🔔 Configurez les alertes

•
📋 Consultez l'historique d'audit

•
📦 Archivez les anciennes factures

Bonne utilisation ! 🚀

