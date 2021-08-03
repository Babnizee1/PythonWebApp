from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this is a sample Python Web App running on Flask Framework! Greetings from babnizee and I'm very prosperous and wealthy in jesus name amen and so shall it be for my family"

