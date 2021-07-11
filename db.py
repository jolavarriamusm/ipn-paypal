import psycopg2
import urllib.parse as urlparse

import os
from dotenv import load_dotenv
load_dotenv()
database_url = os.environ['DATABASE_URL']

def get_connection_unsafe():
    return psycopg2.connect(
                dbname='deg506b08u73i2',
                user='smtckjvoabcoxs',
                password='e069b8102d92c09270411baaa566d6a742994ebe43c5ebf778341fcf4494fec1',
                host='ec2-35-174-127-63.compute-1.amazonaws.com',
                port='5432'
            )

def get_connection():
    url = urlparse.urlparse(database_url)
    dbname = url.path[1:]
    print(dbname)
    print(url.path)
    user = url.username
    password = url.password
    host = url.hostname
    port = url.port
    return psycopg2.connect(
                dbname=dbname,
                user=user,
                password=password,
                host=host,
                port=port
            )

def select_messages():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SET TIMEZONE = 'America/Santiago'")
    cursor.execute("SELECT * FROM messages")
    fetch = cursor.fetchall()
    connection.close()
    return fetch


def add_message(username, message):
    connection = get_connection()
    cursor = connection.cursor()
    query = "INSERT INTO messages (username, message, time) VALUES ('" + username + "', '" + message + "', NOW())"
    cursor.execute(query)
    #query = 'INSERT INTO messages(message_id, username, message, time) VALUES (default, %s, %s, NOW())'
    #cursor.execute(query, ['nick_test', 'message_test'])
    cursor.close()
    connection.commit()
    connection.close()

def delete_message(id):
    connection = get_connection()
    cursor = connection.cursor()
    query = "DELETE FROM messages WHERE message_id = '" + id + "'"
    cursor.execute(query)
    #query = "DELETE FROM messages WHERE id = %s"
    #cursor.execute(query, ['nick_test', 'message_test'])
    cursor.close()
    connection.commit()
    connection.close()
    