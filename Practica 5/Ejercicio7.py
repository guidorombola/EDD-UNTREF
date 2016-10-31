import invertedindex as inv_dicc
from invertedindex_con_btree import *
import string

def palabras_que_empiezan_con(prefijo):
    f_bombadil = open("Bombadil.txt","r", encoding="utf8")
    text_bombadil = "".join(f_bombadil.readlines())
    f_bombadil.close()

    invertido = inv_dicc.inverted_index(text_bombadil)
    salida = [palabra for palabra in invertido if palabra.startswith(prefijo)]
    return salida

def palabras_que_terminan_con(sufijo):
    f_bombadil = open("Bombadil.txt", "r", encoding="utf8")
    text_bombadil = "".join(f_bombadil.readlines())
    f_bombadil.close()

    invertido = inv_dicc.inverted_index(text_bombadil)
    salida = [palabra for palabra in invertido if palabra.endswith(sufijo)]
    return salida

def palabras_que_empiezan_y_terminan_con(prefijo, sufijo):
    f_bombadil = open("Bombadil.txt", "r", encoding="utf8")
    text_bombadil = "".join(f_bombadil.readlines())
    f_bombadil.close()

    invertido = inv_dicc.inverted_index(text_bombadil)
    prefijos = {palabra for palabra in invertido if palabra.startswith(prefijo)}
    sufijos = {palabra for palabra in invertido if palabra.endswith(sufijo)}
    return prefijos & sufijos

# print(palabras_que_empiezan_y_terminan_con("vue","as"))
# print(palabras_que_empiezan_con("vue"))
# print(palabras_que_terminan_con("as"))

def btree_palabras_que_empiezan_con(prefijo):
    f_bombadil = open("Bombadil.txt", "r", encoding="utf8")
    text_bombadil = "".join(f_bombadil.readlines())
    f_bombadil.close()

    invertido = inverted_index(text_bombadil)[0]
    busqueda = prefijo
    nro_caracter = string.ascii_lowercase.find(busqueda[-1])

    if nro_caracter != 25:
        busqueda = busqueda.replace(busqueda[-1],string.ascii_lowercase[nro_caracter+1])
    else:
        busqueda = busqueda.replace(busqueda[-1],"a")

    lista_resultados = []
    for clave in invertido.keys():
        if clave >= prefijo and clave < busqueda:
            lista_resultados.append(clave)

    return lista_resultados

def btree_palabras_que_terminan_con(sufijo):
    f_bombadil = open("Bombadil.txt", "r", encoding="utf8")
    text_bombadil = "".join(f_bombadil.readlines())
    f_bombadil.close()

    ind_inv_con_btree_inv = inverted_index(text_bombadil)[1]            #El segundo valor de la tupla devuelve el arbol
                                                                        # con las palabras invertidas
    ind_inv_con_btree = inverted_index(text_bombadil)[0]
    sufijo_invertido = sufijo[::-1]                                     #[::-1] invierte la cadena (begin:end:step)
    cota_superior_busqueda = sufijo_invertido
    nro_caracter = string.ascii_lowercase.find(sufijo_invertido[-1])

    if nro_caracter != 25:
        cota_superior_busqueda = cota_superior_busqueda.replace(cota_superior_busqueda[-1],
                                                                string.ascii_lowercase[nro_caracter+1])
    else:
        cota_superior_busqueda = cota_superior_busqueda.replace(cota_superior_busqueda[-1],"a")

    lista_resultados = []

    for key in ind_inv_con_btree_inv.keys():
        if key >= sufijo_invertido and key < cota_superior_busqueda:
            inv_key = key[::-1]
            lista_resultados.append(inv_key)

    return lista_resultados


print(btree_palabras_que_terminan_con("as"))