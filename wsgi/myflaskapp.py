from flask import Flask, render_template, request, redirect
import pymongo
app = Flask(__name__)

@app.route("/")
def hello():
    return "hello"


if __name__ == "__main__":
    app.run()

