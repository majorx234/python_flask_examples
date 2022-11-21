#!/usr/bin/env python3
from flask import Flask
from flask_cors import CORS
from flask_restx import Api
from environment import config
import logging
from resources.persons_endpoint import api as persons_endpoint_api_namespace

app = Flask("persons_profession")

CORS(app)

api = Api(app,
          version='0.1',
          title='persons profession',
          description='macht Sachen',
          doc='/swagger-ui')

api.add_namespace(persons_endpoint_api_namespace)

if __name__ == '__main__':
    logging.basicConfig(filename=config.log_path, level=logging.DEBUG)
    logging.info("start persons profression")

    app.run(debug=config.debug, port=config.port, host='0.0.0.0')
