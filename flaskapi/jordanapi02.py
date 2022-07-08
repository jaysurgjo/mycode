#!/usr/bin/env python3
"""DEMO: receiving JSON"""

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

import json

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

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        data = request.json
        if data:
           data= json.loads(data)
           name = data["name"]
           realName = data["realName"]
           since = data["since"]
           powers = data["powers"]
           herodata.append({"name":name,"realName":realName,"since":since,"powers":powers})

    return jsonify(jordanData)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)