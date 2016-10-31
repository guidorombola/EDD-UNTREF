#Dados los coeficientes de una ecuacion cuadratica, calcula las raices de la misma

import math
def calculoRaices(a,b,c):
    x1=(-b+math.sqrt((b**2)-4*a*c))/2*a
    x2=(-b-math.sqrt((b**2)-4*a*c))/2*a
    return [x1,x2]
    
