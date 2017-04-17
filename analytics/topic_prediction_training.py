# coding=utf8

import os
import random
import csv
from collections import Counter

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

with open('care_inbox.csv', 'rb') as csv_trainer:
    raw_email_database = csv.reader(csv_trainer, delimiter='\t')
    email_database = list(raw_email_database)
    email_corpus = []
    for email in range(200):
        email_corpus.append(email_database[email][5])
        emails = ', '.join(email_corpus)

def preprocess(sentence):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word.lower()) for word in word_tokenize(unicode(sentence, errors='ignore'))]


def get_features(text, setting):
    if setting=='bow':
        return {word: count for word, count in Counter(preprocess(text)).items() if not word in stoplist}
    else:
        return {word: True for word in preprocess(text) if not word in stoplist}


# extract the features
all_features = [(get_features(emails, 'bow'))]

print(all_features[0])

with open('clasificador.csv','wb') as csv_classifier:
    w = csv.writer(csv_classifier, delimiter='\t')
    w.writerows(all_features[0].items())
