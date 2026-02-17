import streamlit as st
import json
from pathlib import Path

from construire_fiche import construire_fiche
from generateur_pdf import fabriquer_pdf


st.set_page_config(
    page_title="Générateur de fiche APC - ENS",
    layout="wide"
)

st.title("🧑‍🏫 Générateur de fiche de préparation APC (ENS)")

st.markdown("""
Veuillez renseigner uniquement les **informations générales** et le **préambule**.
Le reste de la fiche sera **généré automatiquement**.
""")

# =========================
# INFORMATIONS GENERALES
# =========================
st.header("1️⃣ Informations générales")

col1, col2, col3 = st.columns(3)

with col1:
    etablissement = st.text_input("Établissement")
    classe = st.text_input("Classe")

with col2:
    discipline = st.text_input("Discipline")
    enseignant = st.text_input("Nom de l’enseignant")

with col3:
    trimestre = st.selectbox("Trimestre", ["1er", "2e", "3e"])
    duree = st.text_input("Durée (ex: 1h, 2h)")

# =========================
# PREAMBULE
# =========================
st.header("2️⃣ Préambule")

col4, col5 = st.columns(2)

with col4:
    module = st.text_input("Module")
    famille_situations = st.text_input("Famille de situations")

with col5:
    competence = st.text_area("Compétence visée", height=80)
    titre_lecon = st.text_input("Titre de la leçon")
    type_lecon = st.selectbox(
        "Type de leçon",
        ["Découverte", "Approfondissement", "Évaluation"]
    )

# =========================
# BOUTON GENERATION
# =========================
# st.markdown("---")

st.markdown("---")

if st.button("📄 Générer le PDF"):
    try:
        # 1. Sauvegarde des informations utilisateur
        fiche_user = {
            "infos_generales": {
                "etablissement": etablissement,
                "classe": classe,
                "discipline": discipline,
                "enseignant": enseignant,
                "trimestre": trimestre,
                "horaire": duree
            },
            "preambule": {
                "titre_module": module,
                "famille_situations": famille_situations,
                "competence": competence,
                "titre_lecon": titre_lecon,
                "type": type_lecon
            }
        }

        Path("data").mkdir(exist_ok=True)

        with open("data/fiche_user.json", "w", encoding="utf-8") as f:
            json.dump(fiche_user, f, ensure_ascii=False, indent=4)

        # 2. Construction automatique de la fiche complète
        construire_fiche()

        # 3. Génération du PDF
        pdf_path = fabriquer_pdf()

        # 4. Téléchargement
        with open(pdf_path, "rb") as pdf_file:
            st.success("✅ PDF généré avec succès !")
            st.download_button(
                label="⬇️ Télécharger la fiche APC (PDF)",
                data=pdf_file,
                file_name="Fiche_APC_ENS.pdf",
                mime="application/pdf"
            )

    except Exception as e:
        st.error(f"❌ Erreur : {e}")

