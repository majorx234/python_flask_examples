#!/usr/bin/python3

import psycopg2

#dictionary: (id: 0,fisrName: Sevim, lastName: Pruschke, profession: Pfleger)
from enum import Enum
class person(Enum):
    id = 0
    firstName = 1
    lastName = 2
    profession = 3
    

try:
    conn = psycopg2.connect("dbname='persons' user='laura' host='localhost'")
except:
    print("connection could not be established")
cur = conn.cursor()
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

#for person in persons:
print(persons[1])
