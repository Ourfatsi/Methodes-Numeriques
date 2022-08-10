# import 
import math
from random import random

def Dichotomie(func,a0,b0,nIterations,limiteHypothetique):
    #Entree : fonction, l'extrêmité gauche de l'intervalle fermé, l'extrêmité droite de l'intervalle fermé, nombre d'itérations ("profondeur").
    #Sortie : void.
    #Résultat : 
    #   - constrution de liste contenant les valeurs de la suite itérative ;
    #   - calcul d'erreur : bornée par une suite qui converge vers zéro d'ordre 1.
    # Conditions : Intervalle fermé ; fonction continue ; contraste de signe
    #Test de contraste de signes

    print("Dichotomie avec calcul d'erreur")
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
        erreur=[]
        suite_borntnate=[]

        #Kernel algorithm
        print("Iteration \t Valeur \t erreur \t suite bornante")
        for i in range(nIterations):
            #Création des sous-intervalles dichotomiques
            x.append((a[i]+b[i])/2)
            erreur.append(abs(limiteHypothetique-x[i]))
            suite_borntnate.append((b0-a0)/(2**(i+1)))
            print(str(i+1)+"\t"+str(x[i])+"\t"+str(erreur[i])+"\t"+str(suite_borntnate[i]))
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

def Banach(func,m,M,a0,b0,nIterations):
    #Entree : fonction, pente maximale lischitzienne, l'extrêmité gauche de l'intervalle fermé, l'extrêmité droite de l'intervalle fermé, nombre d'itérations ("profondeur").
    #Sortie : void.
    #Résultat : constrution de liste contenant les valeurs de la suite itérative.
    # Conditions : Intervalle fermé ; fonction monotone, fonction m-infra-Lipschizienne, M-supra-Lipschitzienne ; contraste de signe
    
    print("Banach avec calcul d'erreur")
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
        lmbda = 1-(m/M)
        seq_err=[]

        #Kernel algorithm
        print("Iteration \t Valeur \t erreur_max \t image")  #Sortie
        for i in range(nIterations):
            #Equation itérative caractéristique
            x.append(x[i] - (func(x[i])/M))
            seq_err.append(((lmbda**i)/(1-lmbda))*abs(x[1]-x[0]))
            print(str(i)+"\t"+str(x[i])+"\t"+str(seq_err[i])+"\t"+str(func(x[i]))) #Sortie