#!/usr/bin/env python3

rappers = ["JayZ", "Nas", "Eminem", "Tupac", "Biggie", "Kayne"]

print(rappers)

favorite_rapper = input(
    "Whats the name of your favorite rapper from this list?\n You can choose one of these or add your own!\n "
).strip()

if favorite_rapper.lower() == "jayz":
    print(f"Name: {favorite_rapper}" + " is the GOAT!\n ")
elif favorite_rapper.lower() == "nas":
    print(f"Name: {favorite_rapper}" + " is in the top 5 :)!\n ")
elif favorite_rapper.lower() == "eminem":
    print(f"Name: {favorite_rapper}" +
          " is a great choice, best lyricist alive!\n ")
elif favorite_rapper.lower() == "tupac":
    print(f"Name: {favorite_rapper}" +
          " is a one of the best and maybe the GOAT!\n ")
elif favorite_rapper.lower() == "biggie":
    print(f"Name: {favorite_rapper}" + " BABY BABY UGH!\n ")
elif favorite_rapper.lower() == "kayne":
    print(f"Name: {favorite_rapper}" +
          " is a solid choice but is a macadamia nut but good!\n ")
else:
    print(" Try again, you can only pick from these six rappers!\n ")
    print(
        " Well I'll let you add some people in here but dont add anyone thats trash!\n "
    )

    other_rappers = input(
        " You can add other rappers to the list but my list is the best!\n  Who is the rapper you want to add?\n "
    )

    while other_rappers == other_rappers:
        print(f" {other_rappers} " +
              "is probaly not that good but thats subjective :)!\n ")
        rappers.append(other_rappers)
        print(
            f" Ill add the rappers you chose to my list so you can feel included :p.\n "
        )
        print(f" Updated list: {rappers}\n ")
        second_rapper = input(" Please add another rapper to the list!\n ").strip()
        print(f" Heres the rapper you chose: {second_rapper}\n ")
        rappers.append(second_rapper)
        print(f" Heres the updated list of rappers: {rappers}\n ")
        third_rapper = input(
            " You get one more selection! Choose wisely because this is a public list!\n "
        ).strip()
        rappers.append(third_rapper)
        print(f" Heres the updated list of rappers: {rappers}\n ")
        print(f" Awesome selection of {third_rapper}\n ")
        print(
            f" Thanks for being a good sport and good selections of {other_rappers}, {second_rapper}, and {third_rapper}.\n "
        )
        print(" Goodbye! ")
        break
