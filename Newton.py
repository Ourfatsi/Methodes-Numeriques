# import 
import math
from random import random

def sinus(x):
    return math.sin(x)

def d_sinus(x):
    return math.cos(x)

def polynomial(x):
    return (x*(x-math.pi)*(x+3))

def d_polynomial(x):
    return (3*x**2 - 2*math.pi*x + 6*x - 3*math.pi)

def exponential(x):
    return (math.e**x-1)

def d_exponential(x):
    return (math.e**x)    
    
def Banach(func,dfunc,x0,d0,depth):
    # Conditions : Intervalle ouvert ; fonction est C2 on suppose que le point zéro existe et que la dérivée n'y est pas nulle
    
    print("La fonction est supposée C2, le point zéro est supposé existant et que la dérivée n'y est pas nulle")

    #Initialsation des variables
    verbose1="Séquence définie sur toutes les "+ str(depth) +" itérations"
    x=[x0]

    nIterations = depth

    #Kernel algorithm
    for i in range(nIterations):
        #Création des sous-intervalles dichotomiques
        x.append(x[i] - func(x[i])/dfunc(x[i]))
    
    #Sortie
    print("Iteration, Valeur")
    for k in range(nIterations):
        print(str(k+1)+"\t"+str(x[k]))

#Main - programme principal        
#print("recherche de racine sinus \n")  
#Banach(sinus,d_sinus,math.pi/2,3*math.pi/2,10)
#Diverge puisque cos(pi/2) = 0 !

#print("recherche de racine pour la fonction polynomiale \n")
#Banach(polynomial,d_polynomial,-4,-2,10)

print("recherche de racine pour la fonction exponentielle \n")
Banach(exponential,d_exponential,-1,1,10)
