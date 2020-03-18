# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 09:50:37 2020

@author: Ambre
"""

from piece import Pion
import plateau as plt
from joueur import Humain #, IA


#le cas ou il s'agit d'une dame

if __name__ == "__main__":
    print("Bienvenue sur le meilleur jeu qui existe.")
    
    choix = input("Voulez-vous jouer contre un 'joueur' ou un 'ordi' ? ")
    if choix == 'joueur':
        j1 = Humain(1,0)
    #else:
        #j1 = IA()
    j2 = Humain(2,0)
    
    plateau = plt.cree_plateau()
    plt.affichage(plateau)
    
    while j1.score < 20 or j2.score <20:
        etat = "joue encore"
        while etat == "joue encore":
            print(" ")
            print("Joueur 1, à vous de jouer. Votre score est de ", j1.score, ".")
            print(" ")
            jeu = j1.joue()
            
            while  j1.unTour(jeu[0],jeu[1],jeu[2],jeu[3],plateau) == "pb":
                jeu = j1.joue()
                plt.affichage(plateau)
                
            pion = Pion(jeu[0],jeu[1],jeu[2],jeu[3],1)
    
            if j1.unTour(jeu[0],jeu[1],jeu[2],jeu[3],plateau) == "je me deplace":
                plateau = pion.bouger(plateau)
                etat = "fin du tour"
                
            else:
                plateau = pion.manger(plateau)
                j1.gagne()
                
            if pion.check_dame():
                plateau = pion.devient_dame(plateau)
                
            plt.affichage(plateau)
        
        etat = "joue encore"
        while etat == "joue encore":
            print(" ")
            print("Joueur 2, à vous de jouer. Votre score est ", j2.score, ".")
            print(" ")
            jeu = j2.joue()
            
            while  j2.unTour(jeu[0],jeu[1],jeu[2],jeu[3],plateau) == 0:
                jeu = j2.joue()
                plt.affichage(plateau)
                
            pion = Pion(jeu[0],jeu[1],jeu[2],jeu[3],2)
    
            if j2.unTour(jeu[0],jeu[1],jeu[2],jeu[3],plateau) == 1:
                plateau = pion.bouger(plateau)
                etat = "fin du tour"
            else:
                plateau = pion.manger(plateau)
                j2.gagne()
                
            if pion.check_dame():
                plateau = pion.devient_dame(plateau)
            plt.affichage(plateau)

    print(" ")    
    if j1.score < j2.score:
        print("Le joueur 2 a gagné.")
    else:
        print("Le joueur 1 a gagné.")
        