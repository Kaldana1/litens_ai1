import streamlit as st
import json
import os
from generateur_pdf import fabriquer_pdf

st.set_page_config(page_title="Générateur fiche de preparation APC ", layout="wide")

st.title("📘 Générateur de fiche de préparation APC ")

st.markdown("Application de génération automatique de fiches pédagogiques APC intégrant le numérique.")

# =========================
# INFORMATIONS GÉNÉRALES
# =========================
st.header("1. Informations générales")

etablissement = st.text_input("Établissement")
classe = st.text_input("Classe")
effectif = st.text_input("Effectif")
discipline = st.text_input("Discipline")
enseignant = st.text_input("Enseignant")
lieu = st.text_input("Lieu de déroulement")
trimestre = st.text_input("Trimestre")
semaine = st.text_input("Semaine")
horaire = st.text_input("Horaire")

# =========================
# PREAMBULE
# =========================
st.header("2. Préambule")

numero_module = st.text_input("Numéro du module")
titre_module = st.text_input("Titre du module")
famille_situations = st.text_area("Famille de situations de vie")
unite_apprentissage = st.text_input("Unité d’apprentissage")
competence = st.text_area("Énoncé de la compétence")
numero_lecon = st.text_input("Numéro de la leçon")
duree = st.text_input("Durée")
titre_lecon = st.text_input("Titre de la leçon")
vocabulaire = st.text_area("Vocabulaire spécifique")
objectif = st.text_area("Objectif d’apprentissage")
actions_programme = st.text_area("Actions du programme")
materiel = st.text_area("Matériel didactique")
demarches = st.text_area("Démarche pédagogique")



methode_pedagogique = st.text_area("Méthode pédagogique")
prerequis = st.text_area("Prérequis")
mediagraphie = st.text_area("Médiagraphie")

# =========================
# SITUATION PROBLÈME
# =========================
st.header("3. Situation problème")

description = st.text_area("Description de la thématique/problème")
consignes = st.text_area("Questions d’orientation / Consignes")
resultats_attendus = st.text_area("Résultats attendus")

# =========================
# DEROULEMENT
# =========================
st.header("4. Déroulement de la leçon")

deroulement = []
for i in range(3):
    st.subheader(f"Étape {i+1}")
    etape = st.text_input(f"Nom de l’étape {i+1}", key=f"etape{i}")
    duree_etape = st.text_input("Durée", key=f"duree{i}")
    opi = st.text_input("OPI", key=f"opi{i}")
    ens = st.text_area("Activités de l’enseignant", key=f"ens{i}")
    eleve = st.text_area("Activités de l’élève", key=f"eleve{i}")
    methodes = st.text_input("Méthodes", key=f"meth{i}")
    evalua = st.text_input("Évaluation", key=f"eval{i}")
    ressources = st.text_input("Ressources", key=f"res{i}")
    obs = st.text_input("Observations", key=f"obs{i}")

    deroulement.append({
        "etape": etape,
        "duree": duree_etape,
        "opi": opi,
        "taches_enseignant": ens,
        "taches_eleve": eleve,
        "methodes": methodes,
        "evaluation": evalua,
        "ressources": ressources,
        "observations": obs
    })

# =========================
# CLOTURE
# =========================
st.header("5. Évaluations et clôture")

eval_app = st.text_area("Évaluation d’application")
eval_int = st.text_area("Évaluation d’intégration")
eval_trans = st.text_area("Évaluation de transfert")
remediation = st.text_area("Remédiation")

# =========================
# GENERATION
# =========================
if st.button("📄 Générer la fiche APC en PDF"):
    data = {
        "infos_generales": {
            "etablissement": etablissement,
            "classe": classe,
            "effectif": effectif,
            "discipline": discipline,
            "enseignant": enseignant,
            "lieu": lieu,
            "trimestre": trimestre,
            "semaine": semaine,
            "horaire": horaire
        },
        "preambule": {
            "numero_module": numero_module,
            "titre_module": titre_module,
            "famille_situations": famille_situations,
            "unite_apprentissage": unite_apprentissage,
            "competence": competence,
            "numero_lecon": numero_lecon,
            "duree": duree,
            "titre_lecon": titre_lecon,
            "vocabulaire": vocabulaire,
            "objectif": objectif,
            "actions_programme": actions_programme,
            "materiel": materiel,
            "demarches": demarches
        },
        "situation_probleme": {
            "methode_pedagogique": methode_pedagogique,
            "prerequis": prerequis,
            "mediagraphie": mediagraphie,
            "description": description,
            "consignes": consignes,
            "resultats_attendus": resultats_attendus
        },
        "deroulement": deroulement,
        "cloture": {
            "evaluation_application": eval_app,
            "evaluation_integration": eval_int,
            "evaluation_transfert": eval_trans,
            "remediation": remediation
        }
    }

    with open("fiche.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    fabriquer_pdf()
    st.success("✅ Fiche APC générée avec succès !")
