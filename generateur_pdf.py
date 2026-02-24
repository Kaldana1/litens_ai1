import json
import os
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import Preformatted

def fabriquer_pdf():
    if not os.path.exists("data/fiche.json"):
        raise FileNotFoundError("Le fichier fiche.json est introuvable")

    with open("data/fiche.json", "r", encoding="utf-8") as f:
        donnees = json.load(f)

    output = "Fiche_APC_ENS.pdf"
    doc = SimpleDocTemplate(output)
    elements = []

    styles = getSampleStyleSheet()
    normal_style = styles["Normal"]

    for cle, valeur in donnees.items():
        elements.append(Paragraph(f"<b>{cle}</b>", styles["Heading3"]))
        elements.append(Spacer(1, 0.2 * inch))
        elements.append(Paragraph(str(valeur), normal_style))
        elements.append(Spacer(1, 0.5 * inch))

    doc.build(elements)

    return output