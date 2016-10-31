import functools


def calcular_costo_total(lista):
    lista_intermedia = list(map(lambda x: x[1]*x[2], lista))
    costo_total = functools.reduce(lambda x, y: x+y, lista_intermedia, 0)
    return costo_total


if __name__ == '__main__':
    li = [("cuadernos", 10, 100), ("lapiceras", 20, 2), ("libros", 5, 150)]
    print(calcular_costo_total(li))
