import csv


def escribir_archivo(texto, ruta):
    file = open(ruta, "w")
    file.write(texto)
    file.close()


def leer_csv():
    dicc_obras_sociales = {}
    reader = csv.reader(open("obras_sociales.csv", "r"), delimiter=",")
    next(reader)
    for registro in reader:
        fecha_y_hora, nombre, obra_social, cod_paciente, tipo_consulta = registro[0], registro[1], registro[2], \
                                                                         registro[3], registro[4]

        dicc_paciente = dicc_obras_sociales.setdefault(obra_social, {"Pacientes": [], "Total": 0})
        lista = dicc_paciente["Pacientes"]
        lista.append([fecha_y_hora, nombre, cod_paciente, tipo_consulta])
        dicc_paciente["Total"] += 1
    volcar_registro_en_txt(dicc_obras_sociales)


def volcar_registro_en_txt(diccionario):
    salida = ""
    for obra_social in diccionario.keys():
        salida += obra_social + ":\n"
        for registro in diccionario[obra_social]["Pacientes"]:
            salida += str(registro)+"\n"
        salida += "{0}. Total: {1} pacientes\n".format(obra_social, diccionario[obra_social]["Total"])
    escribir_archivo(salida, "salida.txt")

if __name__ == '__main__':
    leer_csv()
