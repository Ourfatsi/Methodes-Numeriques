import math

def sinus(x):
    return math.sin(x)

def polynomial(x):
    return (x*(x-math.pi)*(x+3))

def exponential(x):
    return (math.e**x-1)

def carre(x):
    return(x**2-2)

def fonction_a_derivee_compliquee(x):
    return(-x**(3/2)/(x+16)**2+(2*x**(3/2)+48*math.sqrt(x))/(x+16)-12*math.atan(math.sqrt(x)/4))

def d_sinus(x):
    return math.cos(x)    

def d_polynomial(x):
    return (3*x**2 - 2*math.pi*x + 6*x - 3*math.pi)

def d_exponential(x):
    return (math.e**x)