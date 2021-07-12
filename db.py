import psycopg2
import urllib.parse as urlparse

def get_connection_unsafe():
    return psycopg2.connect(
                dbname='de43tdpr0fn1om',
                user='qwykdhdzervpiv',
                password='423b948b683cf5c80cf56c651b24c3381a00fffe0f2311ebf6eb3f3b070544ac',
                host='ec2-54-225-228-142.compute-1.amazonaws.com',
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

def add(data):
    connection = get_connection_unsafe()
    cursor = connection.cursor()
    query = "INSERT INTO paypal_data (data) VALUES ('" + data + "')"
    cursor.execute(query)
    cursor.close()
    connection.commit()
    connection.close()

    