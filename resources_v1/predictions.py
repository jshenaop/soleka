# coding=utf8

from flask import jsonify, Blueprint, request
from flask_restful import Resource, Api, reqparse, inputs
from analytics.topic_prediction_classification import df
from analytics.topic_prediction_classification import topic, sub_topic, sub_subtopic
from analytics.topic_prediction_classification import get_prediction

import models
import analytics.topic_prediction as tp


class Prediction_v1(Resource):
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

        count = tp.word_count(text=text)
        prediction_topic = get_prediction(text=text, dataframe=df, prediction=topic)
        prediction_subtopic = get_prediction(text=text, dataframe=df, prediction=sub_topic)
        prediction_sub_subtopic = get_prediction(text=text, dataframe=df, prediction=sub_subtopic)

        return jsonify({'prediction': [{'text': text,
                                        'topic': prediction_topic, 'sub_topic': prediction_subtopic, 'sub_subtopic': prediction_sub_subtopic,
                                        'gender': 'Experimental', 'age': 'Experimental',
                                        'sentiment': 'Positive-Neutral-Negative'
                                        }]})

predictions_api_v1 = Blueprint('resources_v1.predictions', __name__)
api = Api(predictions_api_v1)
api.add_resource(
    Prediction_v1,
    '/prediction_v1',
    endpoint='prediction'
)
