import json
import os
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML


def fabriquer_pdf():
    # Vérifier l'existence du fichier JSON
    if not os.path.exists('fiche.json'):
        print("Erreur : Le fichier fiche.json est introuvable.")
        return

    # Charger les données depuis le fichier JSON
    with open('fiche.json', 'r', encoding='utf-8') as f:
        donnees = json.load(f)

    # Charger le template HTML avec Jinja2
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('template.html')

    # Générer le HTML final
    html_final = template.render(**donnees)

    # Générer le PDF
    print("Génération du PDF en cours...")
    HTML(string=html_final).write_pdf("Fiche_APC_ENS.pdf")
    print("Succès ! Fiche générée : Fiche_APC_ENS.pdf")


if __name__ == "__main__":
    fabriquer_pdf()
