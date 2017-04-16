# coding=utf8

from flask import Flask

import config
import models
from resources.predictions import predictions_api


DEBUG = True
PORT = 8000
HOST = '0.0.0.0'

app = Flask(__name__)
app.register_blueprint(predictions_api)

@app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == '__main__':
    models.initilize()
    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)