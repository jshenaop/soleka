# coding=utf8

import pandas

stoplist = stopwords.words('spanish')
custom_stop_list = [
    'margin:0px', 'padding:0px', 'body.hmmessage', 'font-size:12pt', 'font-family', 'sans-serif', '<', 'calibri'
    'font-face', 'margin-bottom'
    '--', '}', '{', '>', ',', '.', ';', ':','@', ')', '(', '"', '--'
]
stoplist.extend(custom_stop_list)


def identificador_tema(texto_input, diccionario_clasificador):
    diccionario = diccionario_clasificador.ix[:, 1]
    diccionario_lista = diccionario.tolist()

    def tokenizador_texto(texto_input):
        tokens_texto = texto_input.split()
        return tokens_texto

    def buscador_palabras(tokens_texto, diccionario_lista):
        indices = []
        for word in tokens_texto:
            for row in diccionario_lista:
                if word == row:
                    s = diccionario_lista.index(word)
                    indices.append(s)
        return indices

    def extractor_valores_tema(indices, diccionario_clasificador, tema_a, tema_b):
        lista_tema_a = []
        lista_tema_b  = []
        for line in indices:

            conteo_tema_a = diccionario_clasificador.ix[line, tema_a]
            lista_tema_a.append(conteo_tema_a)

            conteo_tema_b = diccionario_clasificador.ix[line, tema_b]
            lista_tema_b.append(conteo_tema_b)

        suma_tema_a = sum(lista_tema_a)
        suma_tema_b = sum(lista_tema_a)

        return (suma_tema_a, suma_tema_b)

    texto_tokenizado = tokenizador_texto(texto_input)
    indices = buscador_palabras(texto_tokenizado, diccionario_lista)
    conteo_tema_a, conteo_tema_b = extractor_valores_tema(indices, diccionario_clasificador, 2, 3)
