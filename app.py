from flask import Flask, render_template, redirect, request

import db

import os
from dotenv import load_dotenv
load_dotenv()
debugmode = os.environ.get('WEBPROJECT_PRODUCTION')!='TRUE'

app = Flask(__name__)

@app.route('/')
def index():
    message_list = db.select_messages()
    return render_template("index.html", messages = message_list)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/env')
def env():
    if debugmode:
        return 'Corriendo en desarrollo'
    else:
        return 'Corriendo en producción (heroku)'

@app.route('/db')
def database():
    conn = db.get_connection()
    if conn == None:
        return "No se puede conectar a la base de datos"    
    else:
        return "Conexión con base de datos exitosa"

@app.route('/new', methods=['POST'])
def new():
    user_param = request.form['user_data']
    msg_param = request.form['msg_data']
    db.add_message(user_param, msg_param)
    return redirect('/')

#ALTER SEQUENCE messages_message_id_seq RESTART WITH 1
@app.route('/delete', methods=['GET'])
def delete():
    id_param = request.args['id']
    db.delete_message(id_param)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = debugmode)