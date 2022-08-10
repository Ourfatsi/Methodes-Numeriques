import math
import random
import Resolutiond_d_Equations
import Res_d_Equations_erreur

#Fonctions des devoirs
def EX1_f(x): return(x+math.e**x)
def EX2_f(x): return(x-math.cos(x))
def EX3_f(x): return(x**2 - 3)
def d_EX3_f(x) : return(3*x**2)
def EX4_f(x) : return(2-x+math.log(x))
def d_EX4_f(x) : return(-1+(1/x))

#fonction auxiliaires
def miniPente(d_func,a0,b0): return(min(abs(d_func(a0)),abs(d_func(b0))))
def maxiPente(d_func,a0,b0): return(max(abs(d_func(a0)),abs(d_func(b0))))


#Dichotomie(func,a0,b0,nIterations)
# Conditions : Intervalle fermé ; fonction continue ; contraste de signe

#Banach(func,M,a0,b0,nIterations)
# Conditions : Intervalle fermé ; fonction monotone, fonction m-infra-Lipschizienne, M-supra-Lipschitzienne ; contraste de signe

#Newton(func,dfunc,x0,nIterations)
# Conditions : Intervalle ouvert ; fonction est C2 on suppose que le point zéro existe et que la dérivée n'y est pas nulle

#Secante(func,x0,x1)
# Conditions : Intervalle ouvert ; fonction est C2 on suppose que le point zéro existe et que la dérivée n'y est pas nulle

#Resolution(func,methode,Liste_de_parametres)

#1
#Resolutiond_d_Equations.Dichotomie(EX1_f,1,0,50)

#2
#Resolutiond_d_Equations.Dichotomie(EX2_f,0,math.pi/2,50)

#3
#limiteHypothetique = math.sqrt(3)
#Res_d_Equations_erreur.Dichotomie(EX3_f,1,2,20,limiteHypothetique)
#Resolutiond_d_Equations.Secante(EX3_f,1,2)
#Resolutiond_d_Equations.Newton(EX3_f,d_EX3_f,2,50)

#4
#a0=3
#b0=3.5
#nIterations = 10
#Parametres=[a0,b0,nIterations]
#Resolutiond_d_Equations.Dichotomie(EX4_f,a0,b0,nIterations)