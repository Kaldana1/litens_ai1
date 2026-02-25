import json
import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

def fabriquer_pdf():
    if not os.path.exists("data/fiche.json"):
        raise FileNotFoundError("Le fichier fiche.json est introuvable")

    with open("data/fiche.json", "r", encoding="utf-8") as f:
        donnees = json.load(f)

    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("template.html")
    html_final = template.render(**donnees)

    output = "Fiche_APC_ENS.pdf"
    HTML(string=html_final).write_pdf(output)

    return output