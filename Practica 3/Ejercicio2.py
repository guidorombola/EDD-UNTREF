def leer_teclado(mensaje):
    try:
        valor = input(mensaje)

        if valor =="":
            return None

    except (EOFError, KeyboardInterrupt):
        return None

    return valor