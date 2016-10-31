import functools


def producto_de_cubos(lista):
    lista_intermedia = map(elevar_al_cubo, lista)
    resultado = functools.reduce(lambda x, y: x*y, lista_intermedia, 1)
    return resultado


def elevar_al_cubo(numero):
    return numero**3

if __name__ == '__main__':
    li = [1, 2, 6, 4, 5]
    print(producto_de_cubos(li))
