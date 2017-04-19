# coding=utf8

import nltk

from . import topic_prediction_classification
from . import topic_prediction_training

def word_count(text):
    words_list = text.split()
    count = len(words_list)
    return count
