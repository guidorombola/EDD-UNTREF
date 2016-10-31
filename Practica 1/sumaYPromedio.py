def sumaYPromedio(list):
    suma = 0
    for x in list:
        suma+=x
    promedio=suma/len(list)
    return "Suma: " + str(suma) + ", Promedio: " + str(promedio)
    
