import sys

def segura(funcion, *pargs, **kargs):

    try:
        return funcion(*pargs, **kargs)
    except:
        return "Excepcion atrapada: " + str(sys.exc_info()[0]) + "\n" + str(sys.exc_info()[1]) + "\n" + \
               str(sys.exc_info()[2])

def dividir(x,y):
    return x/y

def sumar(x,y):
    return x+y

if  __name__ == '__main__':

    print(segura(dividir, 1,2)) #Verifico que la funcion funcione correctamente
    print(segura(dividir, 1, 0)) #Atrapo la excepcion

    print("")

    print(segura(sumar,1,2))    #Verifico que la funcion funcione correctamente
    print(segura(sumar,"A",2))  #Atrapo la excepcion