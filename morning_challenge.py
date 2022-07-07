#!/usr/bin/python3
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/one")
def first():
    return "Hello Admin"

@app.route("/two/<adj>")
def second(adj):
    return f"Python is {adj}!"

@app.route("/three", methods= ["GET"])
def third():
    return redirect(url_for("third"))

@app.route("/four", methods= ["GET", "POST"])
def fourth():
    return redirect(url_for("eightyninebajillionth"))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
