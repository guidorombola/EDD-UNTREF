import functools
import csv


def calcular_venta_total():
    file = open("ventas-dia.csv", "r")
    reader = csv.reader(file, delimiter=",")
    # intermedia = list(map(lambda x: int(x[1])*int(x[2]), reader))
    # final = functools.reduce(lambda x1, x2: x1+x2, intermedia)
    # file.close()
    # return final
    archivo_intermedio = list(map(escribir_archivo_intermedio, reader))
    final = functools.reduce(reducir, archivo_intermedio)
    return final


def escribir_archivo_intermedio(linea):
    intermedio = open("intermedio.txt", "a")
    resultado = int(linea[1])*int(linea[2])
    intermedio.write(str(resultado)+"\n")
    intermedio.close()
    return resultado


def reducir(linea1, linea2):
    return int(linea1)+int(linea2)

if __name__ == '__main__':
    print(calcular_venta_total())