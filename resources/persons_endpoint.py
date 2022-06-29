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
        try:
            conn = psycopg2.connect("dbname='persons' user='laura' host='localhost'")
        except:
            print("connection could not be established")
            cur = conn.cursor()

    def get(self):
        ''' send status '''
        cur.execute("""SELECT * FROM person_profession """)
        rows = cur.fetchall()
        persons = []
        for row in rows:
            length = len(row)
            person_obj = dict()
            for i in range(0,length):
                person_obj[person(i)] = row[i]
                persons.append(person_obj)
                print("")

        # ToDo:jsonfy #jsonify(persons)
        return persons, HTTPStatus.OK

    def post(self):
        '''Adds a game to games'''
        person_raw = request.json
        print(person_raw)
        # ToDo: add person to database
        return "ok", HTTPStatus.CREATED
