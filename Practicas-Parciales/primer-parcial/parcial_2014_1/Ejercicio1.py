import csv


def devolver_dicc_libros():
    dicc_autores, dicc_editoriales = {}, {}
    reader = csv.reader(open("libros.csv", "r"), delimiter=",")
    next(reader)
    for row in reader:
        titulo, autor, editorial, anio_publicacion = row[0], row[1], row[2], row[3]
        lista_autor = dicc_autores.setdefault(autor, [])
        lista_autor.append((titulo, editorial, anio_publicacion))
        lista_editorial = dicc_editoriales.setdefault(editorial, [])
        lista_editorial.append((titulo, autor, anio_publicacion))
    return dicc_autores, dicc_editoriales

if __name__ == '__main__':
    print(devolver_dicc_libros())
