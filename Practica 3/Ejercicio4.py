import Ejercicio2

def sumar():

    suma = 0
    continua = True

    while continua:

        valor = Ejercicio2.leer_teclado("Ingrese un numero")

        if valor == None:
            continua = False
            return "Total: " + str(suma)
        elif not verifica_num(valor):
            print("Error de tipos")
        else:
            suma+= verifica_num(valor)
            print("Suma: " + str(suma))



def verifica_num(entrada):

    try:
        return float(entrada)

    except (ValueError, TypeError):

        return False
