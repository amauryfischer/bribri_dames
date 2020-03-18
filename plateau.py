# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 09:51:07 2020

@author: Ambre
"""
import numpy as np

    
def cree_plateau():
    plateau = np.zeros((10,10))
    for k in range(4): 
        for j in range(10):
            if (k+j)%2 == 1:
                plateau[k][j]=1
    for k in range(6,10):
        for j in range(10):
            if (k+j)%2 == 1:
                plateau[k][j]=2
    return (plateau)
        
        
def affichage(plateau):
    print(plateau)