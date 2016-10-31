#Hecho sin case sensitive
def aparicion_de_caracter(texto, caracter):

    apariciones=0

    for x in texto:
        if x.lower() == caracter.lower():
            apariciones = apariciones + 1
    return "Cantidad de apariciones de " + caracter +": "+ str(apariciones)

print(aparicion_de_caracter("Prueba para ver cuantas veces aparece la p", "p"))