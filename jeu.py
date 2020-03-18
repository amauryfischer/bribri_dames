# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 09:50:37 2020

@author: Ambre
"""

import plateau as plt
from piece import Pion
from joueur import Humain  # , IA
from utils import *
# le cas ou il s'agit d'une dame


def tour_joueur(joueur, plateau, joueur_title, numero_joueur):
    etat = "joue encore"
    while etat == "joue encore":
        print(" ")
        print(joueur_title + ", à vous de jouer. Votre score est de ",
              joueur.score, ".")
        print(" ")
        jeu = joueur.joue()

        current_tour = joueur.unTour(jeu[0], jeu[1], jeu[2], jeu[3], plateau)

        while current_tour["status"] == "pb":
            jeu = joueur.joue()
            plt.affichage(plateau)

        pion = Pion(jeu[0], jeu[1], jeu[2], jeu[3], numero_joueur)

        if current_tour["status"] == "je me deplace":
            plateau = pion.bouger(plateau)
            etat = "fin du tour"

        elif current_tour["status"] == "je mange":
            plateau = pion.manger(plateau, current_tour["direction"])
            joueur.gagne()

        else:
            display_message("relance", "red")

        if pion.check_dame():
            plateau = pion.devient_dame(plateau)

        plt.affichage(plateau)


if __name__ == "__main__":
    display_begining()
    display_message("Bienvenue sur le meilleur jeu qui existe.")
    display_message(
        "Voulez-vous jouer contre un 'joueur' ou un 'ordi' ? ")
    choix = input()
    if choix == 'joueur':
        j1 = Humain(1, 0)
    # else:
        #j1 = IA()
    j2 = Humain(2, 0)

    plateau = plt.cree_plateau()
    plt.affichage(plateau)

    while j1.score < 20 or j2.score < 20:
        tour_joueur(j1, plateau, "Joueur 1", 1)
        tour_joueur(j2, plateau, "Joueur 2", 2)

    print(" ")
    if j1.score < j2.score:
        print("Le joueur 2 a gagné.")
    else:
        print("Le joueur 1 a gagné.")
