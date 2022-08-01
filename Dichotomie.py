import math

def Moyenne(a,b):
    return((a+b)/2)

def signe(x):
    if x == 0:
        return (0)
    else: 
        return(abs(x)/x)

def sinus(x):
    return math.sin(x)

def polynomial(x):
    return (x*(x-math.pi)*(x+3))
    
def dichotomie(func,a0,b0,depth):
    # Conditions : Intervalle fermé ; fonction continue ; contraste de signe
    #Test de contraste de signes
    if(func(a0) == 0): print("Zero a la limite gauche de l'intervalle")
    if(func(b0) == 0): print("Zero a la limite droite de l'intervalle")

    if signe(func(a0)) == signe(func(b0)):
            print("Contraste de signe inexistant")
            return(-1) #code d'erreur
    else:
        #Initialsation des variables
        verbose1="Séquence définie sur toutes les "+ str(depth) +" itérations"
        a=[a0]
        b=[b0]
        x=[]
             
        nIterations = depth

        #Kernel algorythm
        for i in range(nIterations):
            #Création des sous-intervalles dichotomiques
            x.append(Moyenne(a[i],b[i]))
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

#Main - programme principal        
print("recherche de racine sinus \n")
dichotomie(sinus,1,2*math.pi,50)
#dichotomie(sinus,1,2*math.pi,50,False,True,math.pi)
#print("recherche de racine pour la fonction polynomiale \n")
#dichotomie(polynomial,-5,2,100, True,True)