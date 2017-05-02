# coding=utf8

from flask import Flask
from flask_restful.utils import cors
from flask_cors import CORS, cross_origin

import config
import models
from resources_v1.predictions import predictions_api_v1
from templates.templates import home


app = Flask(__name__)
CORS(app)
app.register_blueprint(predictions_api_v1, url_prefix='/api/v1', )

@app.route('/')
def index():
    return home

if __name__ == '__main__':
    models.initilize()
    #app.run(host=config.HOST)
    app.run(debug=config.DEBUG, host=config.HOST)
