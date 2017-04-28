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
from decimal import Decimal
from fractions import Fraction

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
    'TEMATICA - HOMOLOGACION',
    'TEMATICA - PQR'
]

sub_topic_homologacion = [
    'SUBTEMATICA - SEGUIMIENTO RESPUESTA',
    'SUBTEMATICA - EQUIPO BLOQUEADO',
    'SUBTEMATICA - OTROS',
    'SUBTEMATICA - IMPOSIBILIDAD OBTENER REQUISITOS',
    'SUBTEMATICA - PROBLEMAS DE REGISTRO',
    'SUBTEMATICA - REALIZAR EL TRAMITE HOMOLOGACION',
    'SUBTEMATICA - PETICION POR FORMULARIO',
    'SUBTEMATICA - EQUIPO NO HOMOLOGABLE VENDIDO POR AUTORIZADO',
    'SUBTEMATICA - CONSULTA DE PERTINENCIA',
    'SUBTEMATICA - EQUIPO NO HOMOLOGABLE VENDIDO POR COMERCIO COLOMBIANO',
    'SUBTEMATICA - CORRECION CARTA DE HOMOLOGACION',
    'SUBTEMATICA - COMPLEMENTACION POSTULACION'
]

sub_topic_pqr = [
    'SUBTEMATICA - PETICION POR FORMULARIO'
]

sub_subtopic = [
    'SUB-SUBTEMATICA - NO APLICA'
]

gender = [
    'MASCULINO',
    'FEMENINO'
]

age = [
    'E_10_18',
    'E_19_24',
    'E_25_34',
    'E_35_44',
    'E_45_54',
    'OTRO'
]


def get_prediction(text, dataframe, prediction):

    def preprocess(text):
        lemmatizer = WordNetLemmatizer()
        if sys.version_info[0] == 2:
            return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(unicode(text, errors='ignore'))]
        else:
            return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(str(text))]

    def get_topic_score(dataframe, indexes, column_name):
        vocabulary = dataframe.shape[0]
        frecuency_count = dataframe[column_name].sum()
        divisor = frecuency_count + vocabulary
        print(divisor)

        value = Decimal(0)
        for index in indexes:
            value += Decimal((dataframe.ix[index, dataframe.columns.get_loc(column_name)] + 1) / (divisor))
        return value

    def get_result(topic_scores):
        if topic_scores.count(max(topic_scores)) > 1:
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
    print(prediction)
    print(topic_scores)
    print(topic_scores.index(min(topic_scores)))


    if Decimal(topic_scores[0]) > Decimal(topic_scores[1]):
        print('A')
    if Decimal(topic_scores[0]) < Decimal(topic_scores[1]):
        print('B')
    if Decimal(topic_scores[0]) == Decimal(topic_scores[1]):
        print('C')


# Decision tree
    try:
        if prediction == topic:
            return topic[get_result(topic_scores)]
    except TypeError:
        return 'Imposible to predict'

    try:
        if prediction == sub_topic_homologacion:
            return sub_topic_homologacion[get_result(topic_scores)]
    except TypeError:
        return 'Imposible to predict'

    try:
        if prediction == sub_topic_pqr:
            return sub_topic_pqr[get_result(topic_scores)]
    except TypeError:
        return 'Imposible to predict'

    try:
        if prediction == sub_subtopic:
            return sub_subtopic[get_result(topic_scores)]
    except TypeError:
        return 'Imposible to predict'


""" ------------------------------------------------ Script Module ------------------------------------------------"""
if __name__ == '__main__':
    # Load dictionaries
    df_topic = pd.read_csv('FRECUENCY_SET/frecuency_topic_v2.csv', sep=',', parse_dates=[0], header=0, encoding='latin1')
    prediction = get_prediction(text=text, dataframe=df_topic, prediction=topic)
    print(prediction)

if __name__ != '__main__':

    df_topic = pd.read_csv('./analytics/FRECUENCY_SET/frecuency_topic.csv', sep=',', parse_dates=[0], header=0)
