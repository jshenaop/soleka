# coding=utf8

from flask import Flask

import config
import models
from resources_v1.predictions import predictions_api_v1

app = Flask(__name__)
app.register_blueprint(predictions_api_v1, url_prefix='/api/v1')

@app.route('/')
def index():
    return """<h1>Text predictor for Voice of the Citizen</h1>
              <p>Instructions: make a POST request to /api/v1/prediction sending {"text": "some text"} """

if __name__ == '__main__':
    models.initilize()
    app.run(debug=config.DEBUG, host=config.HOST, port=config.PORT)
