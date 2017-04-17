# coding=utf8

import os
import random
import csv
from collections import Counter

import pandas as pd
import nltk
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import NaiveBayesClassifier, classify

csv.field_size_limit(500 * 1024 * 1024)

stoplist = stopwords.words('spanish')
custom_stop_list = [
    'margin:0px', 'padding:0px', 'body.hmmessage', 'font-size:12pt', 'font-family', 'sans-serif', '<', 'calibri'
    'font-face', 'margin-bottom'
    '--', '}', '{', '>', ',', '.', ';', ':','@', ')', '(', '"', '--'
]
stoplist.extend(custom_stop_list)

dataframe = pd.read_excel('./TRAINING_SET/training_set_homologation_brand.xlsx')

text_corpus_list = []
for text_unit in dataframe['TEXTO']:
    text_corpus_list.append(text_unit)
    print(text_unit)
    corpus = ', '.join(text_corpus_list)
    #print(text_unit)


def preprocess(sentence):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(str(sentence))]


def get_features(text, setting):
    if setting=='bow':
        return {word: count for word, count in Counter(preprocess(text)).items() if not word in stoplist}
    else:
        return {word: True for word in preprocess(text) if not word in stoplist}

 # extract the features
all_features = [(get_features(corpus, 'bow'))]

print(all_features[0])
#
# with open('clasificador.csv','wb') as csv_classifier:
#     w = csv.writer(csv_classifier, delimiter='\t')
#     w.writerows(all_features[0].items())
