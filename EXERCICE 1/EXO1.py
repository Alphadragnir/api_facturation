LARGEUR_MAX = 100

phrases = {
    "b1_maintenance"    : "le code propre facilite la maintenance",
    "b2_tester"         : "tester souvent évite beaucoup d erreurs",
    "b2_hidden"         : "cette phrase ne doit pas s afficher",
    "b3_hidden_simple"  : "un bon code doit rester simple et clair",
    "b3_hidden_phrase"  : "cette phrase ne doit pas s afficher",
    "b3_simplicite"     : "la simplicité améliore la qualité du code",
    "b3_refactoriser"   : "refactoriser améliore la compréhension",
}


phrases_masquees = {
    "b2_hidden",
    "b3_hidden_simple",
    "b3_hidden_phrase",
}

blocs = [
    ["b1_maintenance"],
    ["b2_tester", "b2_hidden"],
    ["b3_hidden_phrase", "b3_hidden_simple", "b3_simplicite", "b3_refactoriser"],
]

def afficher_bloc(lignes_cles: list[str]) -> None:
    """Affiche un bloc encadré (boîte fermée), en filtrant les phrases masquées."""
    bordure_horizontale = "-" * LARGEUR_MAX
    

    lignes_a_afficher = [cle for cle in lignes_cles if cle not in phrases_masquees]
    
    if not lignes_a_afficher:
        return
    
    print(bordure_horizontale)
    
    for cle in lignes_a_afficher:
        texte = phrases[cle].lower()
        largeur_interieure = LARGEUR_MAX - 3
        ligne = f"| {texte:>{largeur_interieure}}|"
        print(ligne)
    
    print(bordure_horizontale)
    print()

for bloc in blocs:
    afficher_bloc(bloc)