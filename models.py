# coding=utf8

import datetime

from argon2 import PasswordHasher
from peewee import *

DATABASE = SqliteDatabase('soleka.sqlite')

class User(Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    password = CharField()

    class Meta:
        database = DATABASE

    def create_user(cls, username, email, password, **kwargs):
        email = email.lower()


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
