import csv
import sys
import natsort

dicc = {}

def organizar_bicicleterias():

    csv.field_size_limit(sys.maxsize)
    csv_comunas = open("comunas.csv","r",errors="ignore")
    csv_bicicleterias = open("bicicleterias.csv", "r", errors="ignore")
    lector_comunas = csv.reader(csv_comunas, delimiter=",")
    lector_bicicleterias = csv.reader(csv_bicicleterias, delimiter=";")

    lector_comunas.__next__()
    for row in lector_comunas:
        comuna = "Comuna " + str(row[-1])
        barrios = row[-4]
        dicc[comuna] = {}
        dicc[comuna]["Barrios"] = barrios
        dicc[comuna]["Bicicleterias"] = {}
    csv_comunas.close()

    lector_bicicleterias.__next__()
    for row in lector_bicicleterias:
        comuna = row[-1]
        nombre = row[2]
        direccion = row[3]
        dicc[comuna]["Bicicleterias"][nombre] = direccion
    csv_bicicleterias.close()

    return dicc

def listar():
    salida = ""
    dicc_ordenado = natsort.humansorted(dicc.items())

    for item in dicc_ordenado:
        salida += item[0] + ": "+ item[1]["Barrios"] + "\n \n"
        ordenada_interna = natsort.humansorted(item[1]["Bicicleterias"].items())
        for bicicleteria in ordenada_interna:
            salida+= bicicleteria[0] +":   "+ bicicleteria[1] +"\n"
        salida+="\n\n"
    return salida



organizar_bicicleterias()
print(listar())

