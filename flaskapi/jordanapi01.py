#!/usr/bin/env python3
"""DEMO: receiving JSON"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

app= Flask(__name__)

jordanData= [{
    "name": "Jay",
    "realName": "Jordan Surgick",
    "since": 1987,
    "powers": [
        "Super Speed",
        "Super Smart",
        "Super Handsome",
        "super human strength & agility"
              ]
             }]

@app.route("/")
def index():
    # jsonify returns legal JSON
    return jsonify(jordanData)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)