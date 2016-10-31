import csv

def maximos():
    """
    Se tiene un archivo de texto formado por líneas compuestas por números enteros positivos separados por comas.
    Escribir una función que lea el archivo y genere un diccionario que indique en qué líneas el máximo está entre
    0 y 9 (clave 1), en qué líneas el máximo está entre 10 y 19 (clave 10), etc. Por ejemplo: si la entrada es:

    25,2,103,18
    0,1,2,3
    4,8,4,5
    102,99,8,7

    la salida deberá ser: {100: [1, 4], 1: [2,3]}.
    """
    diccionario_salida = {}
    reader = csv.reader(open("numeros.csv", "r"), delimiter=",")
    for num_fila, fila in enumerate(reader):
        lista_enteros = convertir_lista_string_a_enteros(fila)
        maximo = max(lista_enteros)
        digitos_maximo = str(maximo).count("")-1
        if digitos_maximo == 1:
            clave = 1
        else:
            primer_digito_maximo = str(maximo)[0]
            clave = primer_digito_maximo+"0"*(digitos_maximo-1)
        lista_lineas = diccionario_salida.setdefault(clave, [])
        lista_lineas.append(num_fila+1)
    return diccionario_salida

def convertir_lista_string_a_enteros(lista):
    return [eval(x) for x in lista]


if __name__ == '__main__':
    print(maximos())