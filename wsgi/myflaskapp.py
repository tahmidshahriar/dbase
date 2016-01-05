from flask import Flask
import pymongo
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('./app.html', form=form, myList = [])

@app.route("/test")
def hello():
    return "hello"

if __name__ == "__main__":
	app.debug = True
	app.secret_key = "hi"
    app.run()

