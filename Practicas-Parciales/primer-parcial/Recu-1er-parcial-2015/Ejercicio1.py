import csv


def leer_notas(ruta):
    dicc_salida = {}
    dicc_alumnos = {}
    archivo = open(ruta, "r")
    lector = csv.reader(archivo, delimiter=";")

   # {padron: {codigo_materia:{P1: nota, P2: nota, R1: nota, R2: nota}}}
    lector.__next__()
    for fila in lector:
        dicc_materias_alumno = dicc_alumnos.setdefault(fila[0], {})
        dicc_materia_alumno = dicc_materias_alumno.setdefault(fila[1],{"P1": 0, "P2": 0, "R1":0, "R2":0})
        dicc_materia_alumno[fila[2]] = float(fila[3])

    for alumno in dicc_alumnos.keys():
        dicc_salida[alumno] = []
        for id_materia in dicc_alumnos[alumno].keys():
            max_parcial1 = max(dicc_alumnos[alumno][id_materia]["P1"], dicc_alumnos[alumno][id_materia]["R1"])
            max_parcial2 = max(dicc_alumnos[alumno][id_materia]["P2"], dicc_alumnos[alumno][id_materia]["R2"])
            if max_parcial1 >= 4 and max_parcial2 >=4:
                dicc_salida[alumno].append(id_materia)

    return dicc_salida


print(leer_notas("materias_parcial.csv"))