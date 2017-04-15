# coding=utf8

import datetime

from peewee import *

DATABASE = SqliteDatabase('soleka.sqlite')


class Prediction(Model):
    text = TextField()
    datetime = DateTimeField(default=datetime.datetime.now)
    prediction = CharField()

    class Meta:
        database = DATABASE


class Trainer(Model):
    text = TextField()
    datetime = DateTimeField()

    class Meta:
        database = DATABASE

def initilize():
    DATABASE.connect()
    DATABASE.create_tables([Prediction, Trainer], safe=True)
