#Dada una lista de numeros, devuelve otra con aquellos que sean primos
def devuelvePrimo(list):
    lista_salida=[]
    for x in list:
        if(es_primo(x)):
            lista_salida.append(x)

    return lista_salida

# Verifica si un numero es primo
def es_primo(num):

    if num < 2:     #si es menos que 2 no es primo, por lo tanto devolverá Falso
        return False

    for i in range(2, num):  #un rango desde el dos hasta el numero que nosotros elijamos
        if num % i == 0:    #si el resto da 0 no es primo, por lo tanto devuelve Falso
            return False

    return True    #de lo contrario devuelve Verdadero

print(devuelvePrimo([3,0,15,20,11]))