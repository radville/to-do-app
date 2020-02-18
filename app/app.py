from flask import Flask   

# create an app instance
app = Flask(__name__)             

@app.route("/<name>")                   
def hello_name(name):                      
    return "Hello " + name  

# on running python app.py, run the flask app       
if __name__ == "__main__":  
    Schema()      
    app.run(debug=True)                   