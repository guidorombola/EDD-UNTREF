# encoding utf8
import functools


def generar_linea_intermedia(linea):
    file = open("intermedio.txt", "a")
    anio = linea[0:4]
    temp = linea[9:12]
    calidad = linea[12]
    if (calidad == "1" or calidad == "2") and (temp != "999"):
        linea_intermedia = anio+","+temp
        file.write(linea_intermedia+"\n")
    file.close()
    return linea_intermedia


def generar_txt_final():
    diccionario_temperaturas = {}
    archivo_entrada = open("temperaturas.txt", "r")
    lista_lineas = [x for x in archivo_entrada]
    archivo_entrada.close()
    li = list(map(generar_linea_intermedia, lista_lineas))
    archivo_intermedio = open("intermedio.txt", "r")
    for linea in archivo_intermedio:
        anio = linea[0:4]
        temp = eval(linea[5:8])
        lista_temperaturas = diccionario_temperaturas.setdefault(anio, [])
        lista_temperaturas.append(temp)
    archivo_intermedio.close()
    archivo_final = open("final.txt", "w")
    for key in diccionario_temperaturas:
        maximo = functools.reduce(max, diccionario_temperaturas[key])
        linea = "Ano:{0}, Max-temp:{1} \n".format(key, maximo)
        archivo_final.write(linea)
    archivo_final.close()

if __name__ == '__main__':
    print(generar_txt_final())

