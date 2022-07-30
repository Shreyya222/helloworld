from flask import Flask   #import Flask module from flask package

app = Flask(__name__)     #create an instance of web application

@app.route("/")          # define the routes
def hello():
    return "Hello World!"  # flask app will being run if we run from app.py


if __name__ == '__main__':
    app.run(debug=True)     #we are setting the debug parameter to true