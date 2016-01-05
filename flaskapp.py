import os
from datetime import datetime
from forms import TodoForm
from flask import Flask, request, flash, url_for, redirect, \
     render_template, abort, send_from_directory

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug="True")
