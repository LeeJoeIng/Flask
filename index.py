import networkx as nx
import community
import numpy as np
import pyrebase
from flask import *
import json

#import firebase_admin
#from firebase_admin import credentials

#cred = credentials.Certificate("key.json")
#firebase_admin.initialize_app(cred)

config = {
  "apiKey": "AIzaSyA7N3W1eqC00CnLi4KZtIly-z5PD3fWDDo",
  "authDomain": "rejoelusion.firebaseapp.com",
  "databaseURL": "https://rejoelusion.firebaseio.com",
  "projectId": "rejoelusion",
  "storageBucket": "rejoelusion.appspot.com",
  "messagingSenderId": "981870293946",
  "appId": "1:981870293946:web:23a62d3fdac5ca2e89a383",
  "measurementId": "G-E7N4B5JGCP"
}

firebase = pyrebase.initialize_app (config)

db = firebase.database()
all_users = db.child("Users").get()

for user in all_users.each():
    #print(user.key())
    #print(user.val())
    #python_dict = json.dumps(str(user.val()))
    #print(python_dict)
    if user.val() is not None:
        #hereeeeee to 
        print(user.val()["ami"])

app = Flask(__name__)

@app.route("/")
def hello_world():
  return "Welcome to PACT 4.2 Drink'O'Neccted!"

@app.route('/community')
def count_community():

  return jsonify(louvain())

def louvain():
    matrix = np.zeros( (10, 10) )
    for i in range (len(matrix)):
        for j in range(len(matrix)):
            matrix[i, i] = 0 #can't be friend with yourself
            matrix[i, j] = np.random.randint(low=0, high=2) #randomly be friends with someone else

    graphPACT = nx.Graph()
    for i in range (len(matrix)):
        for j in range(len(matrix)):
            if(matrix[i,j] == 1):
                graphPACT.add_edges_from([(i, j)])

    #first compute the best partition
    partitionPACT = community.best_partition(graphPACT)

    for k in partitionPACT :
        if k is 2 :
            kom = '{"User": '+str(k)+', "Community": '+str(partitionPACT[k])+'}'

    return kom
