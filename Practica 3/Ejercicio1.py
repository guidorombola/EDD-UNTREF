def oops():
    #raise IndexError
    raise KeyError

def funcion_con_try_except():
    try:
        oops()
    except IndexError:
        return "Excepcion IndexError capturada"
    except KeyError:
        return "Excepcion KeyError capturada"
