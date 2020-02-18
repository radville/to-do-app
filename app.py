from flask import Flask   

# create an app instance
app = Flask(__name__)             

@app.route("/")                   
def hello():                      
    return "Hello World!"  

# on running python app.py, run the flask app       
if __name__ == "__main__":        
    app.run()                   