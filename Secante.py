# import 
import math
from random import random

def sinus(x):
    return math.sin(x)

def polynomial(x):
    return (x*(x-math.pi)*(x+3))

def exponential(x):
    return (math.e**x-1)

def carre(x):
    return(x**2-2)

def fonction_a_derivee_complique(x):
    return(-x**(3/2)/(x+16)**2+(2*x**(3/2)+48*math.sqrt(x))/(x+16)-12*math.atan(math.sqrt(x)/4))   

def Pente(func,b,a):
    return((func(b)-func(a))/(b-a))

def Secante(func,x0,x1):
    #Entree : fonction, les deux premiers points, nombre d'itérations ("profondeur")
    #Sortie : void.
    #Résultat : constrution de liste contenant les valeurs de la suite itérative. 
    # Conditions : Intervalle ouvert ; fonction est C2 on suppose que le point zéro existe et que la dérivée n'y est pas nulle
    # Remarques : les conditions sont les mêmes que celles de Newton, cette méthode est utilisée quand le calcul de la dérivée est difficile
    # C'est le programme qui décide le nombre maximal des itérations, ...
    # ...c'est-à-dire tant que deux valeurs consécutives ne sont pas trop proches pour le compilateur.
    
    print("La fonction est supposée C2, le point zéro est supposé existant et que la dérivée n'y est pas nulle")

    #Initialsation des variables
    x=[x0, x1]

    print("Iteration, Valeur")
    #Kernel algorithm
    i=1
    while (func(x[i-1])-func(x[i-2]) != 0): #C'est-à-dire tant que les deux valeurs ne sont pas trop proches pour le compilateur
        #Equation itérative caractéristique
        rp=(x[i-1]-x[i-2])/(func(x[i-1])-func(x[i-2]))
        x.append(x[i-1]-(func(x[i-1])*rp))
        i = i+1
        #Sortie
        print(str(i)+"\t"+str(x[i]))
        

#Main - programme principal        
print("recherche de racine sinus \n") 
Secante(sinus,math.pi-2,math.pi-1)
#Diverge

#print("recherche de racine pour la fonction polynomiale \n")
#Secante(polynomial,-4,-3.9)

#print("recherche de racine pour la fonction exponentielle \n")
#Secante(exponential,-0.1,-0.09)

#print("recherche de racine pour la fonction quadratique \n")
#Secante(carre,1,2)

print("recherche de racine pour une fonction dont la derivee est compliquee \n")
Secante(fonction_a_derivee_complique,2,2.1)
