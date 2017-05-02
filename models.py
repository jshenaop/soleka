# coding=utf8

import datetime

from peewee import *

DATABASE = SqliteDatabase('soleka.sqlite')

class Prediction(Model):
    text = TextField()
    prediction_topic = CharField()
    prediction_subtopic = CharField()
    prediction_sub_subtopic = CharField()
    gender = CharField(default='')
    age = CharField(default='')
    sentiment = CharField(default='')
    datetime = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE

def initilize():
    DATABASE.connect()
    DATABASE.create_tables([Prediction], safe=True)
