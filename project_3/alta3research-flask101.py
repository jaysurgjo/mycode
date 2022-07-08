#!/usr/bin/python3
"""Alta3 APIs and HTML"""

## best practice says don't use commas in imports
# use a single line for each import
from flask import Flask
from flask import redirect
from flask import url_for
from flask import request
from flask import render_template
from flask import jsonify


app = Flask(__name__)
## This is where we want to redirect users to

classinfo = {
    "all": [
        {
            "name": "Zach",
            "skill level": "wondrous",
            "spirit animal": "Alpaca",
            "super power": "Structure Weakening",
        },
        {
            "name": "Aaron",
            "skill level": "admirable",
            "spirit animal": "Donkey",
            "super power": "Super Strength",
        },
        {
            "name": "Andy",
            "skill level": "amazing",
            "spirit animal": "Goat",
            "super power": "Weather Control",
        },
        {
            "name": "Asif",
            "skill level": "astonishing",
            "spirit animal": "Guinea pig",
            "super power": "Flight",
        },
        {
            "name": "Brent",
            "skill level": "awesome",
            "spirit animal": "Horse",
            "super power": "X-ray Vision",
        },
        {
            "name": "Christopher",
            "skill level": "brilliant",
            "spirit animal": "Pig",
            "super power": "Helicopter Propulsion",
        },
        {
            "name": "Cory",
            "skill level": "cool",
            "spirit animal": "Rabbit",
            "super power": "Invisibility",
        },
        {
            "name": "Ebrima",
            "skill level": "enjoyable",
            "spirit animal": "Water buffalo",
            "super power": "Immobility",
        },
        {
            "name": "Franco",
            "skill level": "excellent",
            "spirit animal": "Chicken",
            "super power": "Immutability",
        },
        {
            "name": "Frank",
            "skill level": "fabulous",
            "spirit animal": "Duck",
            "super power": "Invulnerability",
        },
        {
            "name": "Greg",
            "skill level": "fantastic",
            "spirit animal": "Goose",
            "super power": "Jet Propulsion",
        },
        {
            "name": "Hoon",
            "skill level": "fine",
            "spirit animal": "Pigeon",
            "super power": "Matter Ingestion",
        },
        {
            "name": "JC",
            "skill level": "incredible",
            "spirit animal": "Turkey",
            "super power": "Mobile Invulnerability",
        },
        {
            "name": "Joey",
            "skill level": "magnificent",
            "spirit animal": "Aardvark",
            "super power": "Muscle Manipulation",
        },
        {
            "name": "Jordan",
            "skill level": "marvelous",
            "spirit animal": "Aardwolf",
            "super power": "Nail Manipulation",
        },
        {
            "name": "LB",
            "skill level": "outstanding",
            "spirit animal": "Elephant",
            "super power": "Needle Projection",
        },
        {
            "name": "Mabel",
            "skill level": "phenomenal",
            "spirit animal": "Leopard",
            "super power": "Organic Constructs",
        },
        {
            "name": "Pat",
            "skill level": "pleasant",
            "spirit animal": "Albatross",
            "super power": "Prehensile Hair",
        },
        {
            "name": "Shon",
            "skill level": "pleasing",
            "spirit animal": "Alligator",
            "super power": "Prehensile Tail",
        },
    ]
}

@app.route("/the/<name>")
def start(name=None):
    name = name or "Julius"
    return render_template('index.html', name=name)

@app.route("/")
def welcome():
    return f"Welcome to my page\n"

@app.route("/names")
def get_names():
    return jsonify(classinfo)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
