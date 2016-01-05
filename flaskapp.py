import os
from datetime import datetime
from forms import TodoForm
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/')
def index():
    form = TodoForm()
    if request.method== 'POST':
        try:
            if (request.form['todo'] != ""):
                conn=pymongo.MongoClient()
                db = conn.test
                todo = db.todo
                data = {}
                data['todo'] = request.form['todo']
                todo.insert(data)
            return redirect('/')
        except:
            print "Failed"
            return redirect('/')
    else:
        try:
            conn=pymongo.Connection("mongodb://admin:8lIcmj3N76ZC@127.7.210.130:27017/")
            return "Hi"
            db = conn.test
            todo = db.todo
            myList = list(todo.find())
            return render_template('./app.html', form=form, myList = myList)
        except:
            print "Failed"
            return "OMG"
            return render_template('./app.html', form=form, myList = [])


if __name__ == '__main__':
    app.run(debug="True")
