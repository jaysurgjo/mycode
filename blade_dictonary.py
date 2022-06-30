#!/usr/bin/env python3

blade = {"name": "blade",
        "species": "Dhampir",
        "Team affiliations": "Avengers",
        "aliase": "day walker",
        "powers": ["Master martial artist", "Skilled swordsman and marksman", "Superhuman strength, speed, agility and stamina", "Accelerated healing", "Slowed aging"],
        "age": 50}

blade['Alter ego'] = "Eric Cross Brooks"

keys = list(blade.keys())

print(keys)

user_input = input("Choice one of these keys: ")

choice = user_input

print(f'Blades {choice} is ' + blade[choice] + ".")
