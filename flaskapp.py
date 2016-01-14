import os
from datetime import datetime
from forms import DataForm, LoginForm, ChangeLoginForm
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory, jsonify, session
import pymongo

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route("/", methods=['GET', 'POST'])
def start():
    try:
        a = session['username']
    except:
        session['username'] = None
        

    if (session['username'] != None):
        return redirect('/database')
    form = LoginForm()
    if request.method== 'POST':
        try:
            conn=pymongo.MongoClient(os.environ['OPENSHIFT_MONGODB_DB_URL'])
            db = conn.test
            log = db.log
            myList = list(log.find({ "username" : request.form['username'], "password" : request.form['password']}))
            if len(myList) > 0:
                session['username'] = myList[0]['username']
                return redirect('/database')
            else:
                myList = list(log.find())
                if len(myList) < 1:
                    if (request.form['username'] == "TAHMID"):
                        session['username'] = "admin"
                        return redirect('/database')
                else:
                    return redirect('/')
        except:
            return redirect('/')        
    else:
        return render_template('./login.html', form=form, session = session)


@app.route("/changePassword", methods=['GET', 'POST'])
def change():
    try:
        a = session['username']
    except:
        session['username'] = None
        

    if (session['username'] != 'admin'):
        return redirect('/')
    form = ChangeLoginForm()
    if request.method== 'POST':
        if (request.form['newPassword'] == request.form['newPassword2']):
            try:
                conn=pymongo.MongoClient(os.environ['OPENSHIFT_MONGODB_DB_URL'])
                db = conn.test
                log = db.log
                data = {}
                myList = list(log.find({ "username" : request.form['username'], "password" : request.form['password']}))
                if len(myList) > 0:
                    data['username'] = request.form['username']
                    data['password'] = request.form['password']
                    log.delete_many(data)
                    data['username'] = request.form['username']
                    data['password'] = request.form['newPassword']
                    log.insert(data)
                    return redirect('/')
                else:
                    return "Username and Password did not match"
            except:
                return redirect('/')
        else:
            return "New passwords do not match"
    else:
        return render_template('./changePassword.html', form=form, session = session)



@app.route("/add-first-time-4e-259-16", methods=['GET'])
def add():
    try:
        a = session['username']
    except:
        session['username'] = None
        

    if (session['username'] != 'admin'):
        return redirect('/')
    else:
        try:
            conn=pymongo.MongoClient(os.environ['OPENSHIFT_MONGODB_DB_URL'])
            db = conn.test
            log = db.log
            log.delete_many({})
            data = {}
            data['username'] = 'general'
            data['password'] = 'general'
            log.insert(data)
            data = {}
            data['username'] = 'admin'
            data['password'] = 'admin'
            log.insert(data)
            return redirect('/database')
        except:
            myList = list(log.find())
            print myList
            return "Failed"
                    

@app.route("/signout", methods=['GET', 'POST'])
def signout():
    try:
        a = session['username']
    except:
        session['username'] = None
        

    if (session['username']):
        session['username'] = None
    return redirect('/')



@app.route("/database", methods=['GET', 'POST'])
def hello():
    try:
        a = session['username']
    except:
        session['username'] = None
        

    if (session['username'] != None):
        form = DataForm()
        if request.method == 'POST' and session['username'] == 'admin':
            try:
                conn=pymongo.MongoClient(os.environ['OPENSHIFT_MONGODB_DB_URL'])
                db = conn.test
                information = db.information
                data = {}
                data['program'] = request.form['program']
                data['category'] = request.form['category']
                data['location'] = request.form['location']
                data['description'] = request.form['description']
                data['eligibility'] = request.form['eligibility']
                data['date'] = request.form['date']
                data['duration'] = request.form['duration']
                data['applicationDeadline'] = request.form['applicationDeadline']
                data['essay'] = request.form['essay']
                data['programHyper'] = request.form['programHyper']
                data['applicationHyper'] = request.form['applicationHyper']
                data['reviewHyper'] = request.form['reviewHyper']
                data['top'] = request.form['top']
                data['collegeCredit'] = request.form['collegeCredit']
                data['courses'] = request.form['courses']
                data['note'] = request.form['note']
                information.insert(data)
                return redirect('/database')
            except:
                print "Failed to post"
                return redirect('/database')
        else:
            try:
                conn=pymongo.MongoClient(os.environ['OPENSHIFT_MONGODB_DB_URL'])
                db = conn.test
                information = db.information
                myList = list(information.find())
                return render_template('./app.html', form=form, myList = myList, session = session)
            except:
                print "Failed to get"
                return render_template('./app.html', form=form, myList = [], session = session)
    else:
        return redirect('/')


@app.route("/delete", methods=['POST'])
def delete():
    try:
        a = session['username']
    except:
        session['username'] = None
        

    if session['username'] == 'admin':
        try:
            conn=pymongo.MongoClient(os.environ['OPENSHIFT_MONGODB_DB_URL'])
            db = conn.test
            information = db.information
            data = {}
            data['program'] = request.form['program']
            data['category'] = request.form['category']
            data['location'] = request.form['location']
            data['description'] = request.form['description']
            data['eligibility'] = request.form['eligibility']
            data['date'] = request.form['date']
            data['duration'] = request.form['duration']
            data['applicationDeadline'] = request.form['applicationDeadline']
            data['essay'] = request.form['essay']
            data['programHyper'] = request.form['programHyper']
            data['applicationHyper'] = request.form['applicationHyper']
            data['reviewHyper'] = request.form['reviewHyper']
            data['top'] = request.form['top']
            data['collegeCredit'] = request.form['collegeCredit']
            data['courses'] = request.form['courses']
            data['note'] = request.form['note']
            information.delete_many(data)
            print "HERE"
            return redirect('/database')
        except:
            print "Failed to delete now"
            return redirect('/database')
    else:
        return redirect('/database')

if __name__ == '__main__':
    app.run(debug="True")
