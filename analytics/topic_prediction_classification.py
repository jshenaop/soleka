# coding=utf8

import csv

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
dia de la homologación y lo que ella representa en el pasado de la CRC
"""

topic = [
    'tematica - homologacion'
]

sub_topic = [
    'subtematica - aclaracion respuesta no coincide marca/modelo',
    'subtematica - formulario: al parecer cuenta con un imei alterado',
    'sub-subtematica - no aplica'
]

sub_subtopic = []

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
        return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(str(text))]

    def get_topic_score(dataframe, indexes, column_name):
        value = 0
        for index in indexes:
            value += dataframe.ix[index, dataframe.columns.get_loc(column_name)]
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

    return get_result(topic_scores)

""" ------------------------------------------------ Script Module ------------------------------------------------"""

df = pd.read_csv('./analytics/FRECUENCY_SET/frecuency_topic.csv', sep=',', parse_dates=[0], header=0)
prediction = get_prediction(text=text, dataframe=df, prediction=sub_topic)
