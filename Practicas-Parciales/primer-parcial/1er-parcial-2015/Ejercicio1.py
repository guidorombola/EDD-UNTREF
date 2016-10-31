import csv


def recopilar_datos_aprobacion(ruta_arch1, ruta_arch2):

    dicc_materias_deptos = {}
    dicc_salida = {}

    archivo_materia_depto = open(ruta_arch1, "r")
    archivo_materia_padron_nota = open(ruta_arch2, "r")
    lector1 = csv.reader(archivo_materia_depto, delimiter=";")
    lector2 = csv.reader(archivo_materia_padron_nota, delimiter=";")

    next(lector1)
    for row in lector1:
        materia = row[0]
        depto = row[1]
        dicc_materias_deptos.setdefault(materia, "")
        dicc_materias_deptos[materia] = depto

    archivo_materia_depto.close()

    next(lector2)
    for row in lector2:
        materia = row[0]
        padron = row[1]
        nota = eval(row[2])

        if nota >= 4:
            depto = dicc_materias_deptos.get(materia)
            set_aprobados_depto = dicc_salida.setdefault(depto, set())
            set_aprobados_depto.add(padron)

    archivo_materia_padron_nota.close()

    for depto in dicc_salida.keys():
        dicc_salida[depto] = len(dicc_salida[depto])

    return dicc_salida

#Resolucion de felipe
def leer_csv():
    dicc = {}
    dicc_materias = {}
    file = open('notas.csv', 'r')
    next(file)
    reader = csv.reader(file, delimiter=';')
    for line in reader:
        if line[0] not in dicc_materias:
            dicc_materias[line[0]] = 0  # necesito agregarla aunque no tenga aprobados
        if float(line[2]) >= 4:
            dicc_materias[line[0]] += 1  # {'Cod_Materia': cant_aprobados}
    file = open('deptos.csv', 'r')
    next(file)
    reader = csv.reader(file, delimiter=';')
    for line in reader:
        dicc[line[1]] = dicc.get(line[1], 0) + dicc_materias[line[0]]
    return dicc

print(recopilar_datos_aprobacion("deptos.csv", "notas.csv"))
#print(leer_csv())