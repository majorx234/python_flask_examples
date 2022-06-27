from flask_restx import Namespace, Resource
from flask import Flask, jsonify, request
from http import HTTPStatus

persons = [{'id': '1',
            'firstName': 'Alex',
            'lastName': 'Murphy',
            'profession': 'RoboCop'}]
api = Namespace('persons_endpoint',
                description='persons information')


@api.route('')
class PersonEntpoint(Resource):
    def __init__(self, test):
        print("endpoint called")

    def get(self):
        ''' send status '''
        # ToDo:jsonfy #jsonify(persons)
        return persons, HTTPStatus.OK

    def post(self):
        '''Adds a game to games'''
        person_raw = request.json
        print(person_raw)
        # ToDo: add person to database
        return "ok", HTTPStatus.CREATED
