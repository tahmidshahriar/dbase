import os
from datetime import datetime
from forms import DataForm
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory, jsonify
import pymongo

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route("/", methods=['GET', 'POST'])
def hello():
    form = DataForm()
    if request.method== 'POST':
        try:
            conn=pymongo.MongoClient()
            db = conn.test
            information = db.information
            data = {}
            data['program'] = request.form['program']
            data['eligibility'] = request.form['eligibility']
            data['date'] = request.form['date']
            data['applicationDeadline'] = request.form['applicationDeadline']
            data['programHyper'] = request.form['programHyper']
            data['applicationHyper'] = request.form['applicationHyper']
            data['login'] = request.form['login']
            data['courses'] = request.form['courses']
            data['faq'] = request.form['faq']
            data['sat'] = request.form['sat']
            data['lor'] = request.form['lor']
            data['essay'] = request.form['essay']
            data['note'] = request.form['note']
            information.insert(data)
            return redirect('/')
        except:
            print "Failed to post"
            return redirect('/')
    else:
        try:
            conn=pymongo.MongoClient()
            db = conn.test
            information = db.information
            myList = list(information.find())
            return render_template('./app.html', form=form, myList = myList)
        except:
            print "Failed to get"
            return render_template('./app.html', form=form, myList = [])


@app.route("/delete", methods=['POST'])
def delete():
    try:
        print request.form['program']
        conn=pymongo.MongoClient()
        db = conn.test
        information = db.information
        data = {}
        data['program'] = request.form['program']
        data['eligibility'] = request.form['eligibility']
        data['date'] = request.form['date']
        data['applicationDeadline'] = request.form['applicationDeadline']
        data['programHyper'] = request.form['programHyper']
        data['applicationHyper'] = request.form['applicationHyper']
        data['login'] = request.form['login']
        data['courses'] = request.form['courses']
        data['faq'] = request.form['faq']
        data['sat'] = request.form['sat']
        data['lor'] = request.form['lor']
        data['essay'] = request.form['essay']
        data['note'] = request.form['note']
        information.delete_many(data)
        return redirect('/')
    except:
        print "Failed to delete now"
        return redirect('/')

if __name__ == '__main__':
    app.run(debug="True")
