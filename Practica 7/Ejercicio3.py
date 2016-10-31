from lxml import etree
import string

def list_play_groups():
    display = ""
    for play in open("shaks200/playlist", "r"):
        path = "shaks200/"+play[0:-1]
        tree = etree.parse(path)
        group_list = tree.xpath("//PGROUP")
        title = tree.xpath("/PLAY/TITLE")[0].text
        display += title+"\n"
        for node in group_list:
            character_list = node.findall("PERSONA")
            group_description = node.findall("GRPDESCR")[0]
            display += "\t" + group_description.text + "\n"
            for x in character_list:
                display += "\t\t" + x.text + "\n"
    return display


def count_romeo_and_juliet_lines():
    tree = etree.parse("shaks200/r_and_j.xml")
    lineas_romeo = tree.xpath("//SPEECH[SPEAKER='ROMEO']/LINE")
    lineas_julieta = tree.xpath("//SPEECH[SPEAKER='JULIET']/LINE")
    return "Lineas Romeo: " + str(len(lineas_romeo)) + "\n" + "Lineas Julieta: " + str(len(lineas_julieta))


def inverted_index():
    inverted = {}
    for play in open("shaks200/playlist", "r"):
        path = "shaks200/" + play[0:-1]
        tree = etree.parse(path)
        characters = tree.xpath("//PERSONA")
        title = tree.xpath("/PLAY/TITLE")[0].text
        for persona in characters:
            lista_obras = inverted.setdefault(persona.text, [])
            lista_obras.append(title)
    lista_dicc = list(inverted.items())
    return sorted(lista_dicc, key=clave)


def clave(elemento):
    return len(elemento[1])

if __name__ == '__main__':
    print(inverted_index())