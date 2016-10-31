import csv
import natsort

def leer_csv_old(ruta):

    archivo = open(ruta, "r")
    lector = csv.reader(archivo, delimiter=";")
    lista = list(lector)
    dicc = {}

    for reg in range(1,len(lista)):
        clave = lista[reg][-1]
        dicc[clave] = {"Total": 0, "Barrios": None}             #Inicializo diccionario cuya clave es el nombre de la comuna

    for item in dicc:                   #Para cada comuna

        dicc_barrios = {}
        total = 0
        for register in lista:          #Itero sobre la lista

            barrio = register[-2]
            comuna = register[-1]

            if comuna == item:                      #Agrego barrio al diccionario de barrios para una cierta comuna
                if barrio not in dicc_barrios:
                    dicc_barrios[barrio] = 1        #Si no existe la clave la creo (para que no se creen los barrios de clave cero)
                else:
                    dicc_barrios[barrio]+=1         #Si existe, incremento el contador
                total+=1                            #Cuento el total de bicicleterias
        dicc[item]["Barrios"] = dicc_barrios
        dicc[item]["Total"] = total


    archivo.close()

    return dicc


def leer_csv(ruta):
    archivo = open(ruta,"r")
    lector = csv.reader(archivo,delimiter=";")
    lista = list(lector)
    lista.pop(0)                                #Borro la primera linea que dice los nombres de los campos (barrio,comuna,nombre,etc)
    dicc = {}

    for item in lista:
        comuna = item[-1]
        barrio = item[-2]
        if comuna not in dicc:                                  #Si no existe la comuna
            dicc[comuna] = {"Barrios": {}, "Total": 0}          #La agrego al diccionario
            if barrio not in dicc[comuna]["Barrios"]:           #Si el barrio no está registrado dentro de la comuna
                dicc[comuna]["Barrios"][barrio] = 1             #Agrego clave barrio, valor 1 (para que no aparezca si valen cero)
        else:                                                   #Si la comuna esta en el diccionario
            if barrio not in dicc[comuna]["Barrios"]:           #Si el barrio no fue registrado en el diccionario
                dicc[comuna]["Barrios"][barrio] = 1             #Agrego clave barrio, valor 1 (para que no aparezca si vale cero)
            else:                                               #Si esta registrada la clave de la comuna y el barrio
                dicc[comuna]["Barrios"][barrio]+=1              #Sumo una bicicleteria al barrio
        dicc[comuna]["Total"] += 1                              #Sumo el total de bicicleterias en la comuna

    return natsort.humansorted(dicc.items())

def listar(lista):
    salida = "Bicicleterías por Comuna: \n\n"

    for item in lista:
        salida += item[0] + "\n\n"
        sub_lista_ordenada = natsort.humansorted(item[1]["Barrios"].items())
        for bicicleteria in sub_lista_ordenada:
            salida+= "\t" + bicicleteria[0] +": "+ str(bicicleteria[1]) +"\n"
        salida += "Total: " + str(item[1]["Total"]) +"\n\n"
    return salida



dicc = leer_csv("bicicleterias.csv")
print(listar(dicc))