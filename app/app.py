from flask import Flask, request, jsonify
from service import ToDoService
from models import Schema

import json

# create an app instance
app = Flask(__name__)             

@app.route("/todo", methods=["POST"])                   
def create_todo():                      
    return jsonify(ToDoService().create(request.get_json()))

# on running python app.py, run the flask app       
if __name__ == "__main__":  
    Schema()      
    app.run(debug=True)                   