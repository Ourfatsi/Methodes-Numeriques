# import 
import math

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

#Main - programme principal        
print("recherche de racine sinus \n")  
Newton(sinus,d_sinus,math.pi/2,10)
#Diverge puisque cos(pi/2) = 0 !

print("recherche de racine pour la fonction polynomiale \n")
Newton(polynomial,d_polynomial,-4,10)

print("recherche de racine pour la fonction exponentielle \n")
Newton(exponential,d_exponential,-1,10)
