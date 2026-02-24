import json
import os
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
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

    def ajouter_section_titre(titre):
        elements.append(Paragraph(f"<b>{titre}</b>", styles["Heading2"]))
        elements.append(Spacer(1, 0.3 * inch))

    def ajouter_tableau_dict(data_dict):
        table_data = []
        for cle, valeur in data_dict.items():
            table_data.append([cle, str(valeur)])

        table = Table(table_data, colWidths=[2.5 * inch, 3.5 * inch])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), colors.whitesmoke),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))
        elements.append(table)
        elements.append(Spacer(1, 0.5 * inch))

    # ===== INFOS GENERALES =====
    ajouter_section_titre("INFORMATIONS GENERALES")
    ajouter_tableau_dict(donnees["infos_generales"])

    # ===== PREAMBULE =====
    ajouter_section_titre("PREAMBULE")
    ajouter_tableau_dict(donnees["preambule"])

    # ===== SITUATION PROBLEME =====
    ajouter_section_titre("SITUATION PROBLEME")
    ajouter_tableau_dict(donnees["situation_probleme"])

    # ===== DEROULEMENT =====
    ajouter_section_titre("DEROULEMENT")

    deroulement = donnees["deroulement"]

    if deroulement:
        headers = list(deroulement[0].keys())
        table_data = [headers]

        for ligne in deroulement:
            table_data.append([str(ligne[h]) for h in headers])

        table = Table(table_data, repeatRows=1)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ]))

        elements.append(table)
        elements.append(Spacer(1, 0.5 * inch))

    # ===== CLOTURE =====
    ajouter_section_titre("CLOTURE")
    ajouter_tableau_dict(donnees["cloture"])

    doc.build(elements)

    return output