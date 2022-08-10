import math
import random
import Resolutiond_d_Equations as res
import Res_d_Equations_erreur as reser


#Fonctions de l'exercice
def EX8_f(x): return(1-(1/x)-math.e**(-x))
def d_EX8_f(x): return((1/x**2)+math.e**(-x))
def dd_EX8_f(x): return((2/x**3)+math.e**(-x))
def EX8_g(x): return (-x+1+x*(math.e)**(-x))
def d_EX8_g(x): return (-1-(x-1)*math.e**(-x))
def mEX8_g(x): return -1*EX8_g(x)
def md_EX8_g(x): return -1*d_EX8_g(x)

#fonction auxiliaires
def miniPente(d_func,a0,b0): return(min(abs(d_func(a0)),abs(d_func(b0))))
def maxiPente(d_func,a0,b0): return(max(abs(d_func(a0)),abs(d_func(b0))))

#8
nIterations = 10
print("le point de flexion")
res.Dichotomie(dd_EX8_f,-1,-0.5,nIterations)
print("les points zéro de f")
print("[-1,0]")
a0=-1
b0=-0.01
m=miniPente(d_EX8_g,a0,b0)
M=maxiPente(d_EX8_g,a0,b0)
print(m,";",M)
res.Banach(EX8_g,M,a0,b0,nIterations)
res.Dichotomie(EX8_f,a0,b0,nIterations)
x0 = random.uniform(a0,b0)
res.Newton(EX8_f,d_EX8_f,x0,nIterations)

nIterations = 10
print("[1,2]")
a0=1
b0=2
res.Dichotomie(EX8_f,a0,b0,nIterations)
m=miniPente(d_EX8_g,a0,b0)
M=maxiPente(d_EX8_g,a0,b0)
res.Banach(mEX8_g,M,a0,b0,nIterations) #Err : contraste de signe inexistant
x0=random.uniform(a0,b0) #même chose que x0=a0+((b0-a0)*random.random())
res.Newton(EX8_f,d_EX8_f,x0,nIterations)