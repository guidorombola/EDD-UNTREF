#!/usr/bin/env python3
# ----------------------------------------------------------------------------
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
# ----------------------------------------------------------------------------
# Author: Matteo Bertozzi <theo.bertozzi@gmail.com>
# Site: http://th30z.blogspot.com
# ----------------------------------------------------------------------------

import unicodedata
import functools
from BTrees.OOBTree import *

# Lista de Stop Words en español
# http://snowball.tartarus.org/algorithms/spanish/stop.txt
_WORD_MIN_LENGTH = 3
_STOP_WORDS = frozenset(['de', 'la', 'que', 'el', 'en', 'y', 'a', 'los',
'del', 'se', 'las', 'por', 'un', 'para', 'con', 'no', 'una', 'su', 'al', 'es',
'lo', 'como', 'más', 'pero', 'sus', 'le', 'ya', 'o', 'fue', 'este', 'ha', 'sí',
'porque', 'esta', 'son', 'entre', 'está', 'cuando', 'muy', 'sin', 'sobre',
'ser', 'tiene', 'también', 'me', 'hasta', 'hay', 'donde', 'han', 'quien',
'están', 'estado', 'desde', 'todo', 'nos', 'durante', 'estados', 'todos',
'uno', 'les', 'ni', 'contra', 'otros', 'fueron', 'ese', 'eso', 'había',
'ante', 'ellos', 'e', 'esto', 'mí', 'antes', 'algunos', 'qué', 'unos', 'yo',
'otro', 'otras', 'otra', 'él', 'tanto', 'esa', 'estos', 'mucho', 'quienes',
'nada', 'muchos', 'cual', 'sea', 'poco', 'ella', 'estar', 'haber', 'estas',
'estaba', 'estamos', 'algunas', 'algo', 'nosotros', 'mi', 'mis', 'tú', 'te',
'ti', 'tu', 'tus', 'ellas', 'nosotras', 'vosotros', 'vosotras', 'os', 'mío',
'mía', 'míos', 'mías', 'tuyo', 'tuya', 'tuyos', 'tuyas', 'suyo', 'suya',
'suyos', 'suyas', 'nuestro', 'nuestra', 'nuestros', 'nuestras', 'vuestro',
'vuestra', 'vuestros', 'vuestras', 'esos', 'esas', 'estoy', 'estás', 'está',
'estamos', 'estáis', 'están', 'esté', 'estés', 'estemos', 'estéis', 'estén',
'estaré', 'estarás', 'estará', 'estaremos', 'estaréis', 'estarán', 'estaría',
'estarías', 'estaríamos', 'estaríais', 'estarían', 'estaba', 'estabas',
'estábamos', 'estabais', 'estaban', 'estuve', 'estuviste', 'estuvo',
'estuvimos', 'estuvisteis', 'estuvieron', 'estuviera', 'estuvieras',
'estuviéramos', 'estuvierais', 'estuvieran', 'estuviese', 'estuvieses',
'estuviésemos', 'estuvieseis', 'estuviesen', 'estando', 'estado', 'estada',
'estados', 'estadas', 'estad', 'he', 'has', 'ha', 'hemos', 'habéis', 'han',
'haya', 'hayas', 'hayamos', 'hayáis', 'hayan', 'habré', 'habrás', 'habrá',
'habremos', 'habréis', 'habrán', 'habría', 'habrías', 'habríamos', 'habríais',
'habrían', 'había', 'habías', 'habíamos', 'habíais', 'habían', 'hube',
'hubiste', 'hubo', 'hubimos', 'hubisteis', 'hubieron', 'hubiera', 'hubieras',
'hubiéramos', 'hubierais', 'hubieran', 'hubiese', 'hubieses', 'hubiésemos',
'hubieseis', 'hubiesen', 'habiendo', 'habido', 'habida', 'habidos', 'habidas',
'soy', 'eres', 'es', 'somos', 'sois', 'son', 'sea', 'seas', 'seamos', 'seáis',
'sean', 'seré', 'serás', 'será', 'seremos', 'seréis', 'serán', 'sería',
'serías', 'seríamos', 'seríais', 'serían', 'era', 'eras', 'éramos', 'erais',
'eran', 'fui', 'fuiste', 'fue', 'fuimos', 'fuisteis', 'fueron', 'fuera',
'fueras', 'fuéramos', 'fuerais', 'fueran', 'fuese', 'fueses', 'fuésemos',
'fueseis', 'fuesen', 'siendo', 'sido', 'sed', 'tengo', 'tienes', 'tiene',
'tenemos', 'tenéis', 'tienen', 'tenga', 'tengas', 'tengamos', 'tengáis',
'tengan', 'tendré', 'tendrás', 'tendrá', 'tendremos', 'tendréis', 'tendrán',
'tendría', 'tendrías', 'tendríamos', 'tendríais', 'tendrían', 'tenía',
'tenías', 'teníamos', 'teníais', 'tenían', 'tuve', 'tuviste', 'tuvo',
'tuvimos', 'tuvisteis', 'tuvieron', 'tuviera', 'tuvieras', 'tuviéramos',
'tuvierais', 'tuvieran', 'tuviese', 'tuvieses', 'tuviésemos', 'tuvieseis',
'tuviesen', 'teniendo', 'tenido', 'tenida', 'tenidos', 'tenidas', 'tened', ''])


def word_split(text):
    """
    Split a text in words. Returns a list of tuple that contains
    (word, location) location is the starting byte position of the word.
    """
    word_list = []
    wcurrent = []
    windex = None

    for i, c in enumerate(text):
        if c.isalnum():
            wcurrent.append(c)
            windex = i
        elif wcurrent:
            word = u''.join(wcurrent)
            word_list.append((windex - len(word) + 1, word))
            wcurrent = []

    if wcurrent:
        word = u''.join(wcurrent)
        word_list.append((windex - len(word) + 1, word))

    return word_list

def words_cleanup(words):
    """
    Remove words with length less then a minimum and stopwords.
    """
    cleaned_words = []
    for index, word in words:
        if len(word) < _WORD_MIN_LENGTH or word in _STOP_WORDS:
            continue
        cleaned_words.append((index, word))
    return cleaned_words

def words_normalize(words):
    """
    Do a normalization precess on words. In this case is just a tolower(),
    but you can add accents stripping, convert to singular and so on...
    """
    normalized_words = []
    for index, word in words:
        wnormalized = word.lower()
        normalized_words.append((index, wnormalized))
    return normalized_words

def word_index(text):
    """
    Just a helper method to process a text.
    It calls word split, normalize and cleanup.
    """
    words = word_split(text)
    words = words_normalize(words)
    words = words_cleanup(words)
    return words

def inverted_index(text):
    """
    Create an Inverted-Index of the specified text document.
        {word:[locations]}
    """
    btree = OOBTree()
    btree_palabras_invertidas = OOBTree()

    for index, word in word_index(text):
        palabra_invertida = word[::-1]
        locations = btree.setdefault(word,[])
        locations.append(index)
        locations_inv = btree_palabras_invertidas.setdefault(palabra_invertida, [])
        locations_inv.append(index)
    return btree, btree_palabras_invertidas

def inverted_index_add(inverted, doc_id, doc_index_b_tree):
    """
    Add Invertd-Index doc_index of the document doc_id to the
    Multi-Document Inverted-Index (inverted),
    using doc_id as document identifier.
        {word:{doc_id:[locations]}}
    """
    for word, locations in doc_index_b_tree.items():
        indices = inverted.setdefault(word, {})
        indices[doc_id] = locations
    return inverted

def search(inverted, query):
    """
    Returns a set of documents id that contains all the words in your query.
    """
    words = [word for _, word in word_index(query) if word in inverted]
    results = [set(inverted[word].keys()) for word in words]
    return functools.reduce(lambda x, y: x & y, results) if results else []

if __name__ == '__main__':
    doc1 = """
Esta colección está ilustrada por el
reconocido artista Alan Lee, quien
también aporta un epílogo.
Además, incluye una introducción
del experto en Tolkien, Tom
Shippey y el ensayo "Sobre los
cuentos de hadas", que ofrece una
"""

    doc2 = """
No sabemos cuándo empezó Tolkien
a dirigir sus pensamientos al Reino
Peligroso del País de las Hadas. En su
ensayo «Sobre los cuentos de hadas», 
que se hallará al final de este libro, 
admite que de niño no sentía ninguna 
inclinación por los relatos de ese tipo: 
sólo eran uno de muchos intereses. «El 
auténtico interés por la literatura 
fantástica», afirma, «me lo despertó la 
filología, ya en el umbral de los años 
mozos, y la guerra lo aceleró.
"""

    # Build Inverted-Index for documents
    inverted = {}
    documents = {'doc1':doc1, 'doc2':doc2}
    for doc_id, text in documents.items():
        doc_index = inverted_index(text)
        inverted_index_add(inverted, doc_id, doc_index)

    # Print Inverted-Index
    for word, doc_locations in inverted.items():
        print (word, doc_locations)

    # Search something and print results
    queries = ['Tolkien', 'Reino Peligroso', 'niño']
    for query in queries:
        result_docs = search(inverted, query)
        print ("Search for '%s': %r" % (query, result_docs))
        for _, word in word_index(query):
            def extract_text(doc, index):
                return documents[doc][index:index+20].replace('\n', ' ')

            for doc in result_docs:
                for index in inverted[word][doc]:
                    print ('   - %s...' % extract_text(doc, index))
        print()

#print(inverted_index("Hola como estas, en el reino de los cielos y las hadas madrinas"))