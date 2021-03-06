from flask import Flask , g

import models

DEBUG=True
PORT=8000
HOST='0.0.0.0'

app=Flask(__name__)

@app.before_request

def before_request():
    '''connect to the database before each request'''
    g.db=models.DATABASE
    g.db.connect()

@app.after_request

def after_request():
    '''Close the data base connection after each request'''
    g.db.close()

    return response


if __name__=="__main__":
    
    app.rin(debug=DEBUG,host=HOST,port=PORT)