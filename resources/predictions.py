# coding=utf8

from flask import jsonfy

from flask.ext.restful import Resource

import models


class Prediction(Resource):
    def get(self):
        return jsonfy({'prediction': [{'text': 'Unit Text', 'prediction': 'HOmologación'}]})
