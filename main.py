# Importation de Flask et de render_template
from flask import Flask, render_template, session, redirect
# Importation du module os
import os
# Importation de nos questions
from questions import questions
# Importation des resultats
from questions import resultats


# Création de l'instance de l'app Flask
app = Flask("Ma_webapp")
# Création d'une clef secrete
app.secret_key = os.urandom(24)

# Route principal "/"-> notre page d'accueil qui est donc à la racine du site
@app.route("/")
def index():
    session["numero_question"] = 0
    session["score"] = {"Pikachu": 0, "Mew" : 0 , "Salamèche": 0, "Carapuce" :0}

    return render_template("index.html")

# Route pour les différentes questions
@app.route("/question")
def question():
    # On accède à la variable globale question
    global questions
    nb_question = session["numero_question"] 
    # Si on ne dépasse pas le nombre de question
    if nb_question < len(questions) :
        # On récupère l'énoncé de la question
        enonce_question = questions[nb_question]["enonce"]
        # On retire la question
        questions_copy = questions[nb_question].copy()
        questions_copy.pop("enonce")
        # On récupère les réponses sous forme de liste
        reponses = list(questions_copy.values())
        # On récupère les clefs pour le comptage du score
        session["clefs"] = list(questions_copy.keys())

        return render_template("question.html", question = enonce_question, reponses = reponses)
    else :
        global resultats
        # On trie les scores dans l'odre décroissant
        score = sorted(session["score"], key=session["score"].get , reverse = True)
        # On stocke le nom du vainqueur -> Premier de la liste score
        vainqueur = score[0]
        # On récupère la description associé au vainqueur
        description = resultats[vainqueur]
        return render_template("resultat.html", vainqueur = vainqueur, description = description)

# Route pour la sélection d'une réponse puis redirection vers la prochaine question
@app.route("/reponse/<numero>")
def reponse(numero):
    session["numero_question"] += 1
    resultat = session["clefs"][int(numero)]
    session["score"][resultat] += 1
    print(session["score"])
    return redirect("/question")


# Exécution
app.run(host="0.0.0.0", port = 81)
