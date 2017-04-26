# coding=utf8

import os
import random
import csv
from collections import Counter

import nltk
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import NaiveBayesClassifier, classify

import csv
import sys

import pandas as pd
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords

""" ---------------------------------------------- Stop Words Module ----------------------------------------------"""

stoplist = stopwords.words('spanish')
custom_stop_list = [
    'margin:0px', 'padding:0px', 'body.hmmessage', 'font-size:12pt', 'font-family', 'sans-serif', '<', 'calibri',
    'font-face', 'margin-bottom', '--', '}', '{', '>', ',', '.', ';', ':', '@', ')', '(', '"', '--', '``', ''
]
stoplist.extend(custom_stop_list)

""" ----------------------------------------------- Functions Module -----------------------------------------------"""

text = """

Buenos días que pena con ustedes pero esta es la tercera vez que realizo esta solicitud, estoy tratando de solicitar la homologación de mi equipo Xiaomi mi5, me han respondido tres veces que no aparece el FCC-ID o que las imágenes del IMEI no son claras, pero cuando trato de enviar la información solicitada a la página ComplementacionHomologacion, me solicitan nuevamente todos los dato más y del celular, cuando los ingreso en las tres oportunidades me aparece el aviso de que "AL PARECER" uno de los dos IMEI estará adulterado, que me comunique con el vendedor, y no me deja continuar con el proceso de homologación, el vendedor me contesta que necesita saber cuál de los dos IMEI es el adulterado y hasta el momento no me han respondido las dos veces anteriores cuál de los dos IMEI es el adulterado con seguridad, por lo tanto les solicito que me permitan continuar con la homologación de mi equipo o me respondan cuál de los dos IMEI es el adulterado o me homologuen mi equipo


"""

topic = [
    'tematica - homologacion',
    'tematica - pqr'
]

sub_topic = [
    'subtematica - aclaracion respuesta no coincide marca/modelo',
    'subtematica - formulario: al parecer cuenta con un imei alterado',
    'subtematica - bloqueo/ desbloqueo celulares',
    'subtematica - complementacion postulacion',
    'subtematica - consulta de pertinencia',
    'subtematica - correcion carta de homologacion',
    'subtematica - cuando los equipos vienen sellados',
    'subtematica - equipo bloqueado',
    'subtematica - equipo no homologable vendido por autorizado',
    'subtematica - equipo no homologable vendido por comercio colombiano',
    'subtematica - error al marcar *#06#',
    'subtematica - error en formulario complementacion',
    'subtematica - formato imagenes',
    'subtematica - formulario: al parecer cuenta con un imei alterado',
    'subtematica - imei invalido',
    'subtematica - link de consulta tramite',
    'subtematica - nombre comercial vs modelo equipo',
    'subtematica - peticion por formulario',
    'subtematica - problemas con el operador y ya esta homologado',
    'subtematica - realizar el tramite homologacion',
    'subtematica - sin fcc y otro certificado'
]


sub_subtopic = [
    'sub-subtematica - no aplica'
]

gender = [
    'masculino',
    'femenino'
]

age = [
    'e_10_18',
    'e_19_24',
    'e_25_34',
    'e_35_44',
    'e_45_54',
    'otro'
]


def get_prediction(text, dataframe, prediction):

    def preprocess(text):
        lemmatizer = WordNetLemmatizer()
        if sys.version_info[0] == 2:
            return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(unicode(text, errors='ignore'))]
        else:
            return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(str(text))]

    def get_topic_score(dataframe, indexes, column_name):
        value = 0
        for index in indexes:
            value += dataframe.ix[index, dataframe.columns.get_loc(column_name)]
        return value

    def get_result(topic_scores):
        if topic_scores.count(max(topic_scores)) > 1:
            print(topic_scores.count(max(topic_scores)))
            return 'Imposible to predict'
        else:
            return topic_scores.index(max(topic_scores))

    dictionary = dataframe.ix[:, 0].tolist()
    topic_scores = []

    for category in prediction:
        indexes = []
        for word in preprocess(text=text):
            try:
                s = dictionary.index(word)
                indexes.append(s)
            except ValueError:
                pass
        score = get_topic_score(dataframe=dataframe, indexes=indexes, column_name=category)
        topic_scores.append(score)

    #print(topic_scores)

    if prediction == topic:
        return topic[get_result(topic_scores)]

    if prediction == sub_topic:
        return sub_topic[get_result(topic_scores)]

    if prediction == sub_subtopic:
        return sub_subtopic[get_result(topic_scores)]


""" ------------------------------------------------ Script Module ------------------------------------------------"""

df = pd.read_csv('./analytics/FRECUENCY_SET/frecuency_topic.csv', sep=',', parse_dates=[0], header=0)
#prediction = get_prediction(text=text, dataframe=df, prediction=sub_topic)
