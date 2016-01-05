from flask import Flask, render_template, request, redirect
import pymongo
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('./app.html', form=form, myList = [])


if __name__ == "__main__":
    app.run()

