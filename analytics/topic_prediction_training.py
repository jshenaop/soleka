# coding=utf8

import csv
from itertools import islice
from collections import Counter
from collections import defaultdict

import pandas as pd
from nltk import word_tokenize, WordNetLemmatizer
from nltk.corpus import stopwords
from nltk import NaiveBayesClassifier, classify

csv.field_size_limit(500 * 1024 * 1024)

""" ---------------------------------------------- Stop Words Module ----------------------------------------------"""

stoplist = stopwords.words('spanish')
custom_stop_list = [
    'margin:0px', 'padding:0px', 'body.hmmessage', 'font-size:12pt', 'font-family', 'sans-serif', '<', 'calibri',
    'font-face', 'margin-bottom', '--', '}', '{', '>', ',', '.', ';', ':', '@', ')', '(', '"', '--', '``', ''
]
stoplist.extend(custom_stop_list)

""" ----------------------------------------------- Functions Module -----------------------------------------------"""

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


""" ------------------------------------------------ Script Module ------------------------------------------------"""
if __name__ == '__main__':

    dataframe = pd.read_excel('TRAINING_SET/training_topic_v2.xlsx')

    text = get_corpus(dataframe=dataframe)
    all_features = get_features(text, 'bow')
    all_features_list = []

    for feature in all_features:
        all_features_list.append(feature)

    dictionary = lambda: defaultdict(dictionary)
    classify_dictionary = dictionary()
    headers = []

    for column in islice(dataframe.columns, 1, None):
        for category in dataframe[column].unique():

            header = column + ' - ' + category
            headers.append(header)

    dataframe_csv = pd.DataFrame(data=0, index=all_features_list, columns=headers)

    for column in islice(dataframe.columns, 1, None):
        for category in dataframe[column].unique():

            header = column + ' - ' + category
            headers.append(header)

            filtered_dataframe = dataframe.loc[dataframe[column] == category]

            filtered_text = get_corpus(dataframe=filtered_dataframe)
            filtered_features = get_features(filtered_text, 'bow')

            for feature in all_features:
                try:
                    value = (filtered_features[feature])
                    classify_dictionary[feature][column][category] = value
                    dataframe_csv.set_value(feature, header, value)
                except KeyError:
                    value = 0
                    classify_dictionary[feature][column][category] = value
                    dataframe_csv.set_value(feature, header, value)

    dataframe_csv.to_csv('FRECUENCY_SET/frecuency_topic_v2.csv', sep=',')
