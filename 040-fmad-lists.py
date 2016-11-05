#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Picture yourself in a tapas bar in Andalusia, Spain.
# A waiter or waitress will tell you, as fast as he/she can,
# what tapas they have in the bar to enjoy.
# Our play on today's drive consists in programatically mimic his/her speech.

# First of all, the plates in a list. 
# "Bravas" are potatoes. In fact, the full term is "patatas bravas". This kind of bravery stands for spiciness.
# "Calamares" are rings of squid. You know, "calamari" as usual, but fried in olive oil.
# "Pulpo" is octopus. Usually comes from Galicia, northwest Spain. Yes, somehow related to Wales.
# "Acedias" and "pijotas" are fish delicatessen. Best from the sea you ever tasted.
# "Cecina" is dried and smoked meat.
# "Jamón" should always match "de pata negra" because of the black coloured hoof. Best from the grassland.
# "Salpicón" is a sea food cocktail. No alcohol for once.

tapas = ["bravas", "calamares", "pulpo", "chopitos", "acedías", "pijotas", "cecina", "jamón", "salpicón"]

# A small loop is our first approach.

print("We got", end=" ")

for plate in tapas:
     print(plate, end=" ")

print

# But this does not sound natural, at least in the spanish speaking way:
#
# We got bravas calamares pulpo chopitos acedías pijotas cecina jamón salpicón
#
# For a decent orthography, should add a comma after each word except for the last one, 
# and the word "and" before the last instead of the comma like this:
#
# We got bravas, calamares, pulpo, chopitos, acedías, pijotas, cecina, jamón and salpicón.

print("We got", end=" ")
index = 1
final = ", "

for plate in tapas:

    if index == len(tapas):
        final = "."

    if index == len(tapas) - 1:
        final = " and "

    print(plate, end=final)
    index += 1

print()

# Being correct, a spanish waiter will never talk to you as simple as the above. 
# He/she will always add an article before each meal,
# choosing the appropriate one depending of the gender of the tapa.
#
# Yes, in spanish almost everything has a gender. And we are not finished yet. 
# References to most things are performed using a convention 
# with different format depending of number: one or many, singular or plural.
# 
# For learning purposes, in the spanish version (see blog) we are following this criteria:
#
# · Female ends in “a”
# · Male ends in en “o”
# · Plural ends in “s” and gender is defined by an additional check of the penultimate char:
#     · Then ending in “os” denotates male 
#     · And ending in “as” is female
#     · "es” may be whatever, for us will be male (making a rough approach)
# · All ending in “n” will be considered male (with a small margin for errors)
#
# For the english approach we'll prefix names with arbitrary adjectives just for fun.
# This will be done via a dictionary as the Python language lacks the "select/case" structure:
#
# Beginning of the complete source code. 
# This is the final version, you may remove all the code above for your test.

#!/usr/bin/env python3
""" Tapas Bar for english speaking people """


def plural(x):
    return {
        "as": "beautiful",
        "es": "delicious",
        "os": "marvellous",
    }.get(x, "mighty")


def singular(x):
    return {
        "a": "mouthwatering",
        "o": "magnificent",
        "n": "wonderful"
    }.get(x, "rich")


tapas = ["bravas", "calamares", "pulpo", "chopitos", "acedías", "pijotas", "cecina", "jamón", "salpicón"]

print("We got", end=" ")
index = 1
final = ", "

for plate in tapas:

    if index == len(tapas):
        final = ""

    if index == len(tapas) - 1:
        final = " and "

    latest = plate[-1:]

    if latest == "s":
        article = plural(plate[-2:])
    else:
        article = singular(latest)

    print(article + " " + plate, end=final)
    index += 1

print(".")

# The output of this:
#
# We got beautiful bravas, delicious calamares, magnificent pulpo, marvellous chopitos, 
# beautiful acedías, beautiful pijotas, mouthwatering cecina, wonderful jamón and wonderful salpicón.
#
# That's all folks!
