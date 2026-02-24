import json
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch

def fabriquer_pdf():
    if not os.path.exists("data/fiche.json"):
        raise FileNotFoundError("Le fichier fiche.json est introuvable")

    with open("data/fiche.json", "r", encoding="utf-8") as f:
        donnees = json.load(f)

    output = "Fiche_APC_ENS.pdf"
    doc = SimpleDocTemplate(output)
    elements = []

    styles = getSampleStyleSheet()
    normal_style