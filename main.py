import json

def charger_donnees_locales(nom_fichier):
    try:
        with open(nom_fichier, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print("Erreur : Le fichier fiche.json n'a pas été trouvé.")
        return None

def simuler_generation_pdf():
    # 1. Charger les données (au lieu d'appeler l'IA)
    fiche = charger_donnees_locales('fiche.json')
    
    if fiche:
        print(f"--- GENERATION DE LA FICHE : {fiche['preambule']['titre_lecon']} ---")
        
        # 2. Accès aux informations générales [cite: 4]
        print(f"Établissement : {fiche['infos_generales']['etablissement']}")
        
        # 3. Accès à la situation problème [cite: 34]
        print(f"\nSituation Problème : {fiche['situation_probleme']['description']}")
        
        # 4. Parcours du tableau de déroulement (9 colonnes) 
        print("\nStructure du tableau de déroulement :")
        for ligne in fiche['deroulement']:
            print(f"- Phase: {ligne['etape']} | OPI: {ligne['opi']} | Durée: {ligne['duree']}")
            # Ici tu ajouteras le code pour dessiner les lignes du tableau PDF

if __name__ == "__main__":
    simuler_generation_pdf()