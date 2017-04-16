# coding=utf8

from flask import jsonify, Blueprint, request
from flask_restful import Resource, Api, reqparse, inputs

import models
import analytics.topic_prediction as tp


class Prediction(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'text',
            required=False,
            help='No text for prediction provided',
            location=['form', 'json']
        )

        super().__init__()

    def get(self):
        return jsonify({'prediction': [{'message': 'POST a text to classify'}]})

    def post(self):
        # To use JSON data
        json_data = request.get_json(force=True)
        text = json_data['text']

        # To use parse_args
        # args = self.reqparse.parse_args()
        # text = args.get('text')
        # text = args['text']

        count = tp.word_count(text=text)
        return jsonify({'prediction': [{'text': text, 'word_count': count}]})


predictions_api = Blueprint('resources.predictions', __name__)
api = Api(predictions_api)
api.add_resource(
    Prediction,
    '/api/v1/prediction',
    endpoint='prediction'
)
