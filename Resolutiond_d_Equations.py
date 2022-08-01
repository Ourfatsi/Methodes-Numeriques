# import 
import math
from random import random

def Dichotomie(func,a0,b0,nIterations):
    #Entree : fonction, l'extrêmité gauche de l'intervalle fermé, l'extrêmité droite de l'intervalle fermé, nombre d'itérations ("profondeur").
    #Sortie : void.
    #Résultat : constrution de liste contenant les valeurs de la suite itérative.
    # Conditions : Intervalle fermé ; fonction continue ; contraste de signe
    #Test de contraste de signes
    if func(a0) == 0 : 
        print("Zero a la limite gauche de l'intervalle")
        return(-1) #code d'erreur
    elif func(b0) == 0 :
        print("Zero a la limite droite de l'intervalle")
        return(-1) #code d'erreur
    elif func(a0)/abs(func(a0)) == func(b0)/abs(func(b0)):
        print("Contraste de signe inexistant")
        return(-1) #code d'erreur
    else:
        #Initialsation des variables
        verbose1="Séquence définie sur toutes les "+ str(nIterations) +" itérations"
        a=[a0]
        b=[b0]
        x=[]

        #Kernel algorithm
        for i in range(nIterations):
            #Création des sous-intervalles dichotomiques
            x.append((a[i]+b[i]/2))
            if (func(a[i])*func(x[i]))<0:
                a.append(a[i])
                b.append(x[i])
            elif (func(b[i])*func(x[i]))<0:
                a.append(x[i])
                b.append(b[i])
            else:
                verbose1 = "zero exact en "+str(i)+" itérations"
                nIterations=i
                break
        
        #Sortie
        print("Iteration, Valeur")
        for k in range(nIterations):
            print(str(k+1)+"\t"+str(x[k]))

def Banach(func,M,a0,b0,nIterations):
    #Entree : fonction, pente maximale lischitzienne, l'extrêmité gauche de l'intervalle fermé, l'extrêmité droite de l'intervalle fermé, nombre d'itérations ("profondeur").
    #Sortie : void.
    #Résultat : constrution de liste contenant les valeurs de la suite itérative.
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
        verbose1="Séquence définie sur toutes les "+ str(nIterations) +" itérations"
        x0=a0+(b0-a0)*random() #Le choix du programme est de prendre le point de départ ad hoc dans de l'intervalle
        print("premier point : ( " + str(x0) + " , " + str(func(x0)) + " )\n")
        x=[x0]

        #Kernel algorithm
        for i in range(nIterations):
            #Equation itérative caractéristique
            x.append(x[i] - func(x[i])/M)
        
        #Sortie
        print("Iteration, Valeur")
        for k in range(nIterations):
            print(str(k+1)+"\t"+str(x[k]))
  
def Newton(func,dfunc,x0,nIterations):
    #Entree : fonction, fonction dérivée, point de départ, nombre d'itérations ("profondeur").
    #Sortie : void.
    #Résultat : constrution de liste contenant les valeurs de la suite itérative.
    # Conditions : Intervalle ouvert ; fonction est C2 on suppose que le point zéro existe et que la dérivée n'y est pas nulle
    # Vitesse de la convérgence est quadratique (Ordre au moins 2)
    # Amélioration possible : on entre en donnée d0, le diamètre du voisinage de x0, et on vérifie que la suite reste toujours à l'intérieur de l'intervalle ouvert ...
    # ... (boucle while autour de celle de for par ex), utile en cas de divergence, mais il faut être cohérent avec le nombre des itérations.
    
    print("La fonction est supposée C2, le point zéro est supposé existant et que la dérivée n'y est pas nulle")

    #Initialsation des variables
    verbose1="Séquence définie sur toutes les "+ str(nIterations) +" itérations"
    x=[x0]

    #Kernel algorithm
    for i in range(nIterations):
        #Equation itérative caractéristique
        x.append(x[i] - func(x[i])/dfunc(x[i]))
    
    #Sortie
    print("Iteration, Valeur")
    for k in range(nIterations):
        print(str(k+1)+"\t"+str(x[k]))

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
        