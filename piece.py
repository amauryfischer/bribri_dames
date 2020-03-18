# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 09:50:58 2020

@author: Ambre
"""

# s'occuper des messages d'erreurs
# s'occuper des dames


class Piece():
    def __init__(self, ligne_depart, colonne_depart, ligne_destination, colonne_destination, numero_joueur):
        self.i = ligne_depart - 1
        self.j = colonne_depart - 1
        self.k = ligne_destination - 1
        self.l = colonne_destination - 1
        self.numero_joueur = numero_joueur


class Pion(Piece):
    def __init__(self, ligne_depart, colonne_depart, ligne_destination, colonne_destination, numero_joueur):
        super().__init__(ligne_depart, colonne_depart,
                         ligne_destination, colonne_destination, numero_joueur)

    def bouger(self, plateau):
        plateau[self.i][self.j] = 0
        plateau[self.k][self.l] = self.numero_joueur
        return plateau

    def manger(self, plateau, direction):
        if self.numero_joueur == 1:
            numero_adversaire = 2
        else:
            numero_adversaire = 1

        # pion en bas à droite
        if direction == "en bas a droite":
            plateau[self.i+2][self.j+2] = self.numero_joueur
            plateau[self.i+1][self.j+1] = 0
            plateau[self.i][self.j] = 0
            return plateau
            # pion en bas à gauche
        elif direction == "en bas a gauche":
            plateau[self.i+2][self.j-2] = self.numero_joueur
            plateau[self.i+1][self.j-1] = 0
            plateau[self.i][self.j] = 0
            return plateau
        # pion en haut à droite
        elif direction == "en haut a droite":
            plateau[self.i-2][self.j+2] = self.numero_joueur
            plateau[self.i-1][self.j+1] = 0
            plateau[self.i][self.j] = 0
            return plateau
        # pion en haut à gauche
        elif direction == "en haut a gauche":
            plateau[self.i-2][self.j-2] = self.numero_joueur
            plateau[self.i-1][self.j-1] = 0
            plateau[self.i][self.j] = 0
            return plateau

    def check_dame(self):
        if (self.numero_joueur == 1 and self.k == 9) or (self.numero_joueur == 2 and self.k == 0):
            return True
        else:
            return False

    def devient_dame(self, plateau):
        if int(plateau[self.k][self.l]) == 1:
            plateau[self.k][self.l] = 1.5
        elif int(plateau[self.k][self.l]) == 2:
            plateau[self.k][self.l] = 2.5
        return plateau


# class Dame(Piece):
