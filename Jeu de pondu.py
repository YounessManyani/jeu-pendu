
#Jeu de pendu Youness Manyani

from random import *
import os

# Définition des fonctions

def get_caractere():
    return input("Entrez un caractère : ")

def get_nombre_aleatoire(minimum, maximum):
    return randint(minimum, maximum)

def choisir_mot(mots):
    index_mot = get_nombre_aleatoire(0, len(mots) - 1)
    return mots[index_mot]

def test_caractere(caractere, mot_cache, lettres_decouvertes):
    if caractere in mot_cache:
        for i in range(len(mot_cache)):
            if mot_cache[i] == caractere:
                lettres_decouvertes[i] = caractere

def test_gagne(mot_cache, lettres_decouvertes):
    return mot_cache == "".join(lettres_decouvertes)

def charger_mots(fichier):
    with open(fichier, "r") as f:
        return f.read().splitlines()


def dessine_pendu(coups_restants):
    pendu = ["",
             " \n" + " \n" + " \n" + " \n" + " | \n" + " | \n" + " | \n" + "_|_\n",
             " _______\n |/\n |\n |\n |\n_|_\n",
             " _______\n |/     |\n |      O\n |     /|\\\n |     / \\\n_|_\n"]
    return pendu[coups_restants]

# liste_mots = ["un", "deux", "cinq", "rouge", "membre", "conseil", "donner", "reponse", "etat", "son", "armement", "peu", "apres", "vacances", "annonce", "mercredi", "evident", "regime", "affirmer", "arme"]

# Programme principal

# mots= charger_mots(list_mots)
mots = charger_mots(os.path.dirname(__file__) + '\\mots.txt')
continuer = True

while continuer:
    mot_cache = choisir_mot(mots)
    lettres_decouvertes = ["*" for _ in range(len(mot_cache))]
    coups_restants = 3
    gagne = False
    
    print("Bienvenue dans le jeu du pendu !")
    
    while coups_restants > 0 and not gagne:
        print(dessine_pendu(coups_restants))
        print("Mot à deviner :", "".join(lettres_decouvertes))
        caractere = get_caractere()
        test_caractere(caractere, mot_cache, lettres_decouvertes)
        if caractere not in mot_cache:
            coups_restants -= 1
        gagne = test_gagne(mot_cache, lettres_decouvertes)
    
    if gagne:
        print("Bravo, vous avez gagné !")
    else:
        print(dessine_pendu(coups_restants))
        print("Dommage, vous avez perdu. Le mot était :", mot_cache)
    
    choix = input("Voulez-vous rejouer ? (o/n) ")
    continuer = choix.lower() == "o"

print("Merci d'avoir joué au jeu du pendu !")
