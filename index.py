import flask 
import json 
import os
from flask_pymongo import PyMongo
from flask import request, jsonify
from flask_cors import CORS, cross_origin
from flask import render_template
import creds

class Stack:
    def _data_validate(self):
        self._stack['size']=len(self._stack['data'])

    def __init__(self,elements=[], filename="nil" ):
        self._stack={}
        self._stack['size']=[]
        self._stack['data']=elements
        self._stack['size']=len(elements)
    
    def pop(self):
        if not self._stack['size']:
            raise Exception("stack Exausted")
        temp=self._stack['data'][self._stack['size']-1]
        del self._stack['data'][self._stack['size']-1]
        self._stack['size']=len(self._stack['data'])
        
        return temp

    def empty_stack(self):
        self._stack["data"]=[]
        self._data_validate()

    def push(self,newElement=""):
        self._stack['data'].append(newElement)
        self._stack['size']=len(self._stack['data'])
        return 0

    def is_empty(self):
        if self._stack['size']:
            return 0
        else:
            return 1 
    
    def size(self):
            temp=self._stack['size']
            return temp
    
    def top(self):
        if not self._stack['size']:
            raise Exception("stack empty")
        return self._stack['data'][self._stack['size']-1]

    def stack(self):
        temp=self._stack['data']
        return temp 

    def raw_stack(self):
        temp=self._stack
        return temp
   
def get_stack_from_db():
    stackdb=mongo.db.stack.find({"name" :"stack0"})[0]
    stack._stack['data'] = stackdb['data']
    stack._data_validate()
    return "OK",200

def dbupdate():
    temp={
        "$set":{
        "data":stack.stack(),
        "size":stack.size()
        }
    }
    try :
        mongo.db.stack.update_one({"name":"stack0"},temp)
    except: 
        return "Internal Server Error With DB", 500
    get_stack_from_db()    
    return "DB UPDATE OK",200

#  APP CONFIG 
app = flask.Flask(__name__)
CORS(app, support_credentials=True)
app.config["DEBUG"] = False
MONGO_DB_URI = os.environ['MONGO_DB_URI']
app.config['MONGO_URI'] = MONGO_DB_URI
mongo = PyMongo(app)
stackdb=mongo.db.stack.find({"name" :"stack0"})[0]
stack = Stack(elements=stackdb['data'])

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/stack',methods=['GET'])
def view_stack():
    return json.dumps(stack.raw_stack()),200

@app.route('/pop',methods=['GET'])
def pop():
    stack.pop()
    try :
        dbupdate()
    except: 
        return "Internal Server Error With DB", 500
    return {"POP":"OK"},200

@app.route('/push',methods=['GET'])
def push():
    if 'data' not in request.args:
        return "Bad Request Please Pass the data in the Quary Parameters",400
    stack.push(request.args['data'])
    try :
        dbupdate()
    except: 
        return "Internal Server Error With DB", 500
    return {"PUSH":" OK"},200

if __name__ == "__main__":
    app.run(host='0.0.0.0')
