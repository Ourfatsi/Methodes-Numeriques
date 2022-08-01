# import 
import math
from random import random

def sinus(x):
    return math.sin(x)

def polynomial(x):
    return (x*(x-math.pi)*(x+3))

def exponential(x):
    return (3**x-1)    
    
def Banach(func,M,a0,b0,depth):
    # Conditions : Intervalle fermé ; fonction monotone, fonction m-infra-Lipschizienne, M-supra-Lipschitzienne ; contraste de signe
    
    print("La fonction est supposée monotone et la pente de toute corde sur sa courbe est bornée inférieurement et supérieurement")
    if func(a0)*func(b0)==0:
            print("Err : l'image d'une extrémité est nulle")
            return(-1) #code d'erreur
    elif abs(func(a0))/func(a0) == abs(func(b0))/func(b0): #Test de contraste de signes
            print("Err : contraste de signe inexistant")
            return(-1) #code d'erreur
    else:
        #Initialsation des variables
        verbose1="Séquence définie sur toutes les "+ str(depth) +" itérations"
        x0=a0+(b0-a0)*random() #Le choix du programme est de prendre le point de départ ad hoc dans de l'intervalle
        print("premier point : ( " + str(x0) + " , " + str(func(x0)) + " )\n")
        x=[x0]

        nIterations = depth

        #Kernel algorithm
        for i in range(nIterations):
            #Création des sous-intervalles dichotomiques
            x.append(x[i] - func(x[i])/M)
        
        #Sortie
        print("Iteration, Valeur")
        for k in range(nIterations):
            print(str(k+1)+"\t"+str(x[k]))

#Main - programme principal        
#print("recherche de racine sinus \n")  
#Banach(sinus,1,math.pi/2,3*math.pi/2,6)

#print("recherche de racine pour la fonction polynomiale \n")
#Banach(polynomial,40,-4,-2,100)

#print("recherche de racine pour la fonction exponentielle \n")
#Banach(exponential,3+math.pi,-1,1,200)
