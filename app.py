from flask import Flask, request
from db import add

app = Flask(__name__)

@app.route('/')
def index():
    print("hola") #add(request.data)
    return "200"

if __name__ == '__mcheain__':
    app.run(debug = True)