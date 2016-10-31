"""
# diccionario de recetas de comida clave nombre de plato, valor lista de pares (ingred, cant) como cant para una
# porcion. Se tiene otro dicc con productos en mi alacena con clave ingrediente y valor cantidad disponible.

# (a) dado una lista que_se_cocina que contiene pares (plato, cantidad de porciones) construir un dicc de compras
# con los ingredientes que faltan para cocinar

# (b) escribir funciones para hacer persistente el dicc
"""


def crear_lista_compras(recetas, alacena, que_se_cocina):
    salida = {}
    for alimento in que_se_cocina:
        comida = alimento[0]
        cant_comida = alimento[1]
        if comida in recetas:
            for ingrediente in recetas[comida]:
                nombre_ingrediente = ingrediente[0]
                cantidad_ingrediente = ingrediente[1]
                if nombre_ingrediente not in alacena:
                    salida.setdefault(nombre_ingrediente, 0)
                    salida[nombre_ingrediente] += cantidad_ingrediente*cant_comida
                elif cantidad_ingrediente*cant_comida > alacena[nombre_ingrediente]:
                    salida.setdefault(nombre_ingrediente, 0)
                    salida[nombre_ingrediente] += (cantidad_ingrediente*cant_comida) - alacena[nombre_ingrediente]
                    alacena[nombre_ingrediente] = 0

    return salida

if __name__ == '__main__':
    recetas = {"pizza": [("harina", 1), ("tomate", 1), ("queso", 25)],
               "ensalada": [("lechuga", 100), ("tomate", 1), ("zanahoria", 1)],
               "flan": [("huevo", 1), ("leche", 100), ("azucar", 60)]}
    alacena = {"huevo": 6, "harina": 500, "queso": 250, "tomate": 2}
    que_se_cocina = [("pizza", 4), ("ensalada", 2)]
    print(crear_lista_compras(recetas, alacena, que_se_cocina))
