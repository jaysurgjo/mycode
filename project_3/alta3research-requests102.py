#!/usr/bin/env python3

from flask import Flask
from flask import request
from flask import redirect
from flask import jsonify

app= Flask(__name__)

URL= "http://127.0.0.1:2224/names"

new_name= [{
     "name": "Jordy",
     "skill level": "The Best",
     "spirit animal": "Hedgehog",
     "super power": "Super loud voice",
}]

@app.route("/", methods=["GET","POST"])
def index():
    if request.method == 'POST':
        data = request.json
        if data:
           data= json.loads(data)
           name = data["name"]
           realName = data["skill level"]
           since = data["spirit animal"]
           powers = data["super power"]
           new_name.append({"name":name,"skill level":realName,"spirit animal":since,"super powers":powers})

    return jsonify(new_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
