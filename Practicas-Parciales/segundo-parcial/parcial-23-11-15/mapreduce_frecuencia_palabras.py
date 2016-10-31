import re

'''
texto -> lista de lineas donde aparecen las palabras y frecuencia

map : lista de pares (palabra, linea)
reduce : diccionario con frecuencia y lineas de aparicion de cada palabra
'''


def frecuencia_palabras(texto):
    lista_lineas = re.split(r"\n", texto)
    lista_intermedia = []
    for num_linea, linea in enumerate(lista_lineas, start=1):
        lista_intermedia += mapper(linea, num_linea)
    return reducer(lista_intermedia)


def reducer(lista_intermedia):
    '''
    Recibe la lista de tuplas intermedia y devuelve un diccionario con frecuencia y lineas de aparicion de la palabra
    '''
    salida = {}
    for tupla in lista_intermedia:
        apariciones = salida.setdefault(tupla[0], {"lineas": set(), "frecuencia": 0})
        #apariciones = salida.setdefault(tupla[0], ([], frec))
        #apariciones[0].append(tupla[1])
        apariciones["lineas"].add(tupla[1])
        apariciones["frecuencia"] += 1
    return salida


def mapper(linea, nro_linea):
    '''
    Recibe una linea y devuelve una lista de tuplas (palabra, linea_aparicion)
    '''
    lista_tuplas = []
    palabras_linea = re.split(r'\W+', linea)
    for palabra in palabras_linea:
        lista_tuplas.append((palabra, nro_linea))
    return lista_tuplas


if __name__ == '__main__':
    print(frecuencia_palabras("hola esto, es. un* test\ de split split\n split split"))