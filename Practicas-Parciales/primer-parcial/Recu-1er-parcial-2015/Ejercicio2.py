arreglos = {"pintar pieza chicos": (["rodillo", "pincel brocha gorda", "pincel brocha fina", "escalera"],
                                    [("pintura blanca", 3),("lija fina", 1)]),
            "pintar comedor": (["rodillo", "pincel brocha gorda", "pincel brocha fina", "escalera"],
                               [("pintura blanca", 4), ("lija fina", 1)])}

dicc_artefactos = {"pincel brocha gorda": "Funciona", "escalera": "Funciona","rodillo": "No Funciona",
                   "martillo": "Funciona"}
dicc_materiales = {"pintura blanca":2, "clavos de 0,5": 100, "lija fina": 4}

def lista_de_compras():
    dicc_compras = {}
    dicc_total_consumibles = {}                                # lo uso para contar el total de materiales que necesito
    for arreglo in arreglos.values():                               #Para cada arreglo
        for artefacto in arreglo[0]:                                #Para todos los artefactos que involucra
            if artefacto not in dicc_artefactos or \
                            dicc_artefactos[artefacto] == "No Funciona":    #Si el no tengo el artefacto o no funciona
                dicc_compras[artefacto] = 1
        for consumibles in arreglo[1]:                              #Para todos los elementos con cantidades
            dicc_total_consumibles.setdefault(consumibles[0], 0)
            dicc_total_consumibles[consumibles[0]] += consumibles[1]        #Sumo la cantidad de elementos que necesito
    for consumible in dicc_total_consumibles.keys():                            #Para todos los elementos que necesito
        if dicc_total_consumibles[consumible] > dicc_materiales[consumible]:            #Si no me alcanza la cantidad
            comprar = dicc_total_consumibles[consumible] - dicc_materiales[consumible]  #Veo cuantos comprar
            dicc_compras[consumible] = comprar                                          #Agrego al dicc de compras
    return dicc_compras

print(lista_de_compras())

