from flask import Flask, request
from db import add

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    add(request.json())
    #cad=""
    #cad+="URL:"+request.url+"<br/>"
    #cad+="Método:"+request.method+"<br/>"
    #cad+="header:<br/>"
    #for item,value in request.headers.items():
    #    cad+="{}:{}<br/>".format(item,value)    
    #cad+="información en formularios (POST):<br/>"
    #for item,value in request.form.items():
    #    cad+="{}:{}<br/>".format(item,value)
    #cad+="información en URL (GET):<br/>"
    #for item,value in request.args.items():
    #    cad+="{}:{}<br/>".format(item,value)    
    #cad+="Ficheros:<br/>"
    #for item,value in request.files.items():
    #    cad+="{}:{}<br/>".format(item,value)
    #add(cad)
    return "200"

if __name__ == '__mcheain__':
    app.run(debug = True)