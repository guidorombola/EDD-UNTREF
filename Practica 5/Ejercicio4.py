import invertedindex


def encontrar_posiciones(palabra):
    intro = open("Introduccion.txt","r",encoding="utf8")
    bombadil = open("Bombadil.txt","r",encoding="utf8")
    egidio = open("Egidio.txt","r",encoding="utf8")
    niggle = open("Niggle.txt","r",encoding="utf8")
    roverandom = open("Roverandom.txt","r",encoding="utf8")
    wootton = open("Wootton.txt","r",encoding="utf8")

    text_intro = "".join(intro.readlines())
    text_bombadil = "".join(bombadil.readlines())
    text_egidio = "".join(egidio.readlines())
    text_niggle = "".join(niggle.readlines())
    text_roverandom = "".join(roverandom.readlines())
    text_wootton = "".join(wootton.readlines())

    intro.close()
    bombadil.close()
    egidio.close()
    niggle.close()
    roverandom.close()
    wootton.close()

    dicc = {"Intro": text_intro, "Bombadil": text_bombadil, "Egidio":text_egidio, "Niggle": text_niggle,
            "Roverandom": text_roverandom, "Wotton": text_wootton}

    indice_invertido = {}

    for id, text in dicc.items():
        indice_invertido_seccion = invertedindex.inverted_index(text)
        invertedindex.inverted_index_add(indice_invertido, id, indice_invertido_seccion)

    #resultado = invertedindex.search(indice_invertido, palabra)
    #return resultado
    resultados = indice_invertido.setdefault(palabra, [])
    return resultados


if __name__ == '__main__':
    print(encontrar_posiciones("geografía"))
