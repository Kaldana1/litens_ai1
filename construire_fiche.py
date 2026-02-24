import json
from pathlib import Path

# =========================
# GENERATION AUTOMATIQUE
# =========================

def generer_situation_probleme(preambule):
    return {
        "description": (
            f"Une situation concrète liée au module « {preambule['titre_module']} » "
            f"est proposée afin d’amener les élèves à mobiliser la compétence visée."
        ),
        "consignes": (
            "Observer la situation proposée, analyser les données fournies "
            "et proposer une solution en mobilisant les connaissances antérieures."
        ),
        "resultats_attendus": (
            "Les élèves identifient correctement le problème posé et proposent "
            "des solutions cohérentes."
        )
    }


def generer_deroulement():
    return [
        {
            "etape": "Mise en situation",
            "duree": "10 min",
            "opi": "Suscter l’intérêt et identifier le problème",
            "taches_enseignant": "Présente la situation-problème",
            "taches_eleve": "Observe et analyse la situation",
            "methodes": "Discussion dirigée",
            "evaluation": "Observation",
            "ressources": "Tableau, craie",
            "observations": ""
        },
        {
            "etape": "Construction des savoirs",
            "duree": "25 min",
            "opi": "Construire les notions",
            "taches_enseignant": "Guide les échanges et explique",
            "taches_eleve": "Participe et prend des notes",
            "methodes": "Méthode active",
            "evaluation": "Questions orales",
            "ressources": "Support de cours",
            "observations": ""
        },
        {
            "etape": "Application",
            "duree": "15 min",
            "opi": "Appliquer les acquis",
            "taches_enseignant": "Propose des exercices",
            "taches_eleve": "Résout les exercices",
            "methodes": "Travail individuel",
            "evaluation": "Exercices corrigés",
            "ressources": "Cahiers",
            "observations": ""
        }
    ]


def generer_cloture():
    return {
        "evaluation_application": "Exercices d’application immédiate.",
        "evaluation_integration": "Résolution d’une situation intégratrice.",
        "evaluation_transfert": "Réinvestissement dans un autre contexte.",
        "remediation": "Reprise des notions non maîtrisées."
    }


# =========================
# CONSTRUCTION FINALE
# =========================

def construire_fiche():
    user_file = Path("data/fiche_user.json")
    final_file = Path("data/fiche.json")

    if not user_file.exists():
        print("❌ Fichier fiche_user.json introuvable")
        return

    with open(user_file, "r", encoding="utf-8") as f:
        fiche_user = json.load(f)

    fiche_complete = {
        "infos_generales": fiche_user["infos_generales"],
        "preambule": fiche_user["preambule"],
        "situation_probleme": generer_situation_probleme(fiche_user["preambule"]),
        "deroulement": generer_deroulement(),
        "cloture": generer_cloture()
    }

    with open(final_file, "w", encoding="utf-8") as f:
        json.dump(fiche_complete, f, ensure_ascii=False, indent=4)

    print("✅ Fiche complète générée : data/fiche.json")


if __name__ == "__main__":
    construire_fiche()
