import math
import Resolutiond_d_Equations
import fonctions

def Resolution(func,methode,Liste_de_parametres):
    #Entrée : 
    # - la fonction dont on désire lui trouver un point zéro ;
    # - la méthode à choisir parmi : Dichotomie, Banach, Newton, Secante
    # - liste de paramètres propres à chaque méthode
    #Sortie : void
    #Resultat : liste d'indices et valeurs itérée jusqu'au point zero si conversion

    if methode == 'Dichotomie':
        a0 = Liste_de_parametres[0]
        b0 = Liste_de_parametres[1]
        nIterations = Liste_de_parametres[2]
        Resolutiond_d_Equations.Dichotomie(func,a0,b0,nIterations)
    elif methode == 'Banach':
        M = Liste_de_parametres[0]
        a0 = Liste_de_parametres[1]
        b0 = Liste_de_parametres[2]
        nIterations = Liste_de_parametres[3]
        Resolutiond_d_Equations.Banach(func,M,a0,b0,nIterations)
    elif methode == 'Newton':
        dfunc = Liste_de_parametres[0]
        x0 = Liste_de_parametres[1]
        nIterations = Liste_de_parametres[2]
        Resolutiond_d_Equations.Newton(func,dfunc,x0,nIterations)
    elif methode == 'Secante':
        x0 = Liste_de_parametres[0]
        x1 = Liste_de_parametres[1]
        Resolutiond_d_Equations.Secante(func,x0,x1)
    else:
        print("Err")

print("Mis l'oeuvre du programme")

print("1-fonction a derivee compliquee par la methode de la secante")
print("C'est la fonction qui choisit le nombre maximal d'iterations")
Parametres = [2,2.1]
Resolution(fonctions.fonction_a_derivee_compliquee,'Secante',Parametres)

print("2-methode de dichotomie pour fonction sinus")
Parametres = [math.pi/2,3*math.pi/2,50]
Resolution(fonctions.sinus,'Dichotomie',Parametres)

print("3-methode de Newton pour fonction exponentielle")
Parametres = [fonctions.d_exponential,-1,10]
Resolution(fonctions.exponential,'Newton',Parametres)

print("4-methode de Banach pour fonction polynomiale")
print("Le point de depart est choisi de maniere aleatoire dans l'intervalle donne")
Parametres = [40,-4,-2,100] 
#N.B. : 40 c'est la valeur lue sur wxMaxima sur la courbe dérivée à l'extrémité de l'intervalle, choisie pour M-lipscitzienne car vue comme valeur maximale
Resolution(fonctions.polynomial,'Banach',Parametres)