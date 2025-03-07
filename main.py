# Importation de Flask et de render_template
from flask import Flask, render_template, session, redirect
# Importation du module os
import os
# Importation du module os
import random


# Création de l'instance de l'app Flask
app = Flask("Jeu du Pendu")
# Création d'une clef secrete
app.secret_key = os.urandom(24)

# Premier route -> première page affichée lorsqu'on arrive sur l'application web 
# Rénitialiser le jeu
@app.route("/")
def accueil():
    # Liste de mots possibles
    liste_de_mots = ["ordinateur", "clavier", "magic", "araignée", "souris", "fenêtre", "papier", "arbre", "fleur"]
    # On choisit un mot au hasard
    mot_a_deviner = random.choice(liste_de_mots)

    print(mot_a_deviner)
    return "Test"














# Exécution
app.run(host="0.0.0.0", port = 81)
