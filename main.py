from flask import Flask 

app = Flask(__name__)
@app.route("/")
def hello():
	return "Hello world"
@app.route("/about")
def about():
	return "This blog is own by FlexBox inc"
@app.route("/hello")
def greet():
	return "Hello world at greet"
app.run(debug=True)	