# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 09:51:23 2020

@author: Ambre
"""
#si le joueur ne peut plus bouger mais il lui reste des pions, il perd la partie.

class Joueur():
    def __init__(self,numero,score):
        self.numero = numero
        self.score = score
    
    def unTour(self,ligne_depart,colonne_depart,ligne_destination,colonne_destination,plateau): 
        #verifie que c'est le bon joueur et que la case est bonne
        i = ligne_depart - 1
        j = colonne_depart - 1
        k = ligne_destination - 1
        l = colonne_destination - 1
        
        if self.numero == 1:
            coeff = 1
            numero_adversaire = 2
        else:
            coeff = -1
            numero_adversaire = 1
        
        if (i < 0 or i > 9) or (j < 0 or j > 9) or (k < 0 or k > 9) or (l < 0 or l > 9):            #erreur car dépassement du plateau
            print(" ")
            print("VEUILLEZ SAISIR DES COORDONNEES SUR LE PLATEAU.")
            print(" ")
            return "pb"
        
        else :    
            print(type(plateau[i][j]))                                                       
            if int(plateau[i][j])==self.numero:          #prend bien son pion
                if k == i+coeff and (l == j+1 or l == j-1) and int(plateau[k][l]) == 0:     #le met dans une case acceptée (en bas pour le j1, en haut pour le j2)
                    return "je me deplace"                                                         #alors tout va bien, le pion se déplace !
                
                elif (k == i+2 and l == j+2) and int(plateau[i+1][j+1]) == numero_adversaire:   
                    return "je mange"                                                          #le pion mange
                elif (k == i+2 and l == j-2) and int(plateau[i+1][j-1]) == numero_adversaire:
                    return "je mange" 
                elif (k == i-2 and l == j+2) and int(plateau[i-1][j+1]) == numero_adversaire:
                    return "je mange"
                elif (k == i-2 and l == j-2) and int(plateau[i-1][j-1]) == numero_adversaire:
                    return "je mange"
                
                else:
                    print(" ")
                    print("VOUS NE POUVEZ PAS PLACER VOTRE PION ICI. RECOMMENCEZ.")
                    print(" ")
                    return "pb"                          
            else:
                print(" ")
                print("VEUILLEZ PRENDRE UN DE VOS PIONS.")
                print(" ")
                return "pb"    #erreur
            


        
    
    def gagne(self):
        self.score += 1
        print(" ")
        print("Le joueur ",self.numero," prend un point.")
        print(" ")

    
class Humain(Joueur):
    def __init__(self,numero,score):
        super().__init__(numero,score)
        
    
    def joue(self):
        print("Les lignes et les colonnes commencent à 1 !")
        ligne_depart = int(input("Sur quelle ligne se situe votre pion ? "))
        colonne_depart = int(input("Sur quelle colonne se situe votre pion ? "))
        ligne_destination = int(input("Sur quelle ligne voulez-vous bouger votre pion ? "))
        colonne_destination = int(input("Sur quelle colonne voulez-vous bouger votre pion ? "))
        
        return [ligne_depart,colonne_depart,ligne_destination,colonne_destination]



    
#class IA():
    