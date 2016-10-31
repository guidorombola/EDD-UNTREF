import string
def cifrar(frase,clave):

    '''Cifra una frase utilizando la tecnica de Caesar, desplazando cada letra
    la cantidad de caracteres indicado en la clave:

    Argumentos:
        frase: cadena de caracteres a cifrar (solo letras minusculas)
        clave: un entero con la cantidad de posiciones a desplazar (entre 0 y 26)

    Retorno:
        Devuelve una cadena de caracteres con la frase cifrada. Si la frase
        original contenia otros caracteres que no fueran letras
        minusculas estos quedan inalterados en la cadena retornada '''

    cadena_cifrada=""

    for x in frase:
        posicion=string.ascii_lowercase.find(x)

        if posicion != -1:
            if posicion+clave >= len(string.ascii_lowercase):
                clave -= len(string.ascii_lowercase)

            cadena_cifrada += string.ascii_lowercase[posicion+clave]
        else:
            cadena_cifrada += x

    return cadena_cifrada

def descifrar(frase_cifrada, clave):

    """ Devuelve la frase descifrada con la clave aplicando el metodo
        Ceasar
        Argumentos:
            frase_cifrada: frase cifrada con el metodo Ceasar y la clave
            clave: clave para descifrar, debe ser igual a la usada cuando
            se cifro
        Retorna:
            frase descifrada
            """
    cadena_descifrada = ""

    for x in frase_cifrada:

        posicion = string.ascii_lowercase.find(x)

        if posicion == -1:
            cadena_descifrada += x
        else:
            cadena_descifrada += string.ascii_lowercase[posicion-clave]

    return cadena_descifrada


def cifrar_archivo(entrada, salida, clave):
    """ Cifra el archivo de entrada usando la tecnica de Caesar"""

    archivo_entrada = open(entrada, "r")
    archivo_salida = open(salida, "w")

    for line in archivo_entrada:
        archivo_salida.write(cifrar(line,clave))

    archivo_entrada.close()
    archivo_salida.close()

def descifrar_archivo(entrada, salida, clave):

    """ Descifra el archivo de entrada usando la tecnica de Caesar

    Argumentos:
    entrada: cadena de caracteres con el path completo al archivo de entrada
    salida: cadena de caracteres con el path completo al archivo de salida
    clave: entero entre 0 y 26 """

    archivo_entrada = open(entrada, "r")
    archivo_salida = open(salida, "w")

    for line in archivo_entrada:
        archivo_salida.write(descifrar(line, clave))

    archivo_entrada.close()
    archivo_salida.close()

descifrar_archivo("1.txt","2.txt",3)



