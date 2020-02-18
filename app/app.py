from flask import Flask   

# create an app instance
app = Flask(__name__)             

@app.route("/todo", method=["POST"])                   
def create_todo():                      
    return ToDoService().create(request.get_json())

# on running python app.py, run the flask app       
if __name__ == "__main__":  
    Schema()      
    app.run(debug=True)                   