# coding=utf8

import os
import random
import csv
from itertools import islice
from collections import Counter
from collections import defaultdict

import pandas as pd
import nltk
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import NaiveBayesClassifier, classify

csv.field_size_limit(500 * 1024 * 1024)

dataframe = pd.read_excel('./TRAINING_SET/training_set_homologation_brand.xlsx')

""" Stop Words Module """
stoplist = stopwords.words('spanish')
custom_stop_list = [
    'margin:0px', 'padding:0px', 'body.hmmessage', 'font-size:12pt', 'font-family', 'sans-serif', '<', 'calibri'
                                                                                                       'font-face',
    'margin-bottom'
    '--', '}', '{', '>', ',', '.', ';', ':', '@', ')', '(', '"', '--'
]
stoplist.extend(custom_stop_list)


def get_corpus(dataframe):
    text_corpus = []
    for text_unit in dataframe['TEXTO']:
        text_corpus.append(text_unit)
        corpus = ', '.join(text_corpus)
    return corpus


def get_features(text, setting):
        def preprocess(text):
            lemmatizer = WordNetLemmatizer()
            return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(str(text))]

        if setting == 'bow':
            return {word: count for word, count in Counter(preprocess(text)).items() if not word in stoplist}
        else:
            return {word: True for word in preprocess(text) if not word in stoplist}


all_features = [(get_features(text, 'bow'))]
print(all_features)

dictionary = lambda: defaultdict(dictionary)
classify_dic = dictionary()

for column in islice(dataframe.columns, 1, None):
    for category in dataframe[column].unique():

        filtered_dataframe = dataframe.loc[dataframe[column] == category]
        text_corpus_list = []

        for text_unit in filtered_dataframe:
            text_corpus_list.append(text_unit)
            corpus = ', '.join(text_corpus_list)

        for feature in all_features:
            for key in feature.keys():
                try:
                    value = (feature[key])
                    classify_dic[key][column][category] = value
                except KeyError:
                    value = (feature[key])
                    classify_dic[key][column][category] = value

print(classify_dic['telefónica'])

#with open('clasificador.csv', 'wt', encoding="utf-8") as csv_classifier:
#    csv = csv.writer(csv_classifier, delimiter='\t')

#    for feature in all_features:
#        for key in feature.keys():
#            word = str(key)
#            count = str(feature[key])
#            csv.writerow([word, count])

#            # f.writerow([ciudad, place['nombre'], place['horario'], place['direccion'], place['tipoCAVs']])
