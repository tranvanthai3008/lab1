"""
A module show nnformation about the number of characters, characters without \
spaces and punctuation marks, the name of the Pokemon, the name of the skills
"""

import json

# question 1 and 2
CHAR_TOTAL = 0  # q1
CHAR_TOTAL_FORMAT = 0  # q2

file_data = open("pokemon_full.json")
text_data = file_data.readlines()

file_data.seek(0)
pokemon_data = json.load(file_data)
for line in text_data:
    string_line = line
    CHAR_TOTAL += len(string_line)
    CHAR_TOTAL_FORMAT += (
        len(string_line) - string_line.count(" ") - string_line.count(".")
    )

print(f"character total: {CHAR_TOTAL}")
print(f'character total after striming "." and " ": {CHAR_TOTAL_FORMAT}')

# question 3
MAX_LEN = 0
INDEX = 0
for i, pokemon in enumerate(pokemon_data):
    if pokemon["description"] != "Description not available yet":
        if len(pokemon["description"]) > MAX_LEN:
            MAX_LEN = len(pokemon["description"])
            INDEX = i

name_max = pokemon_data[INDEX]["name"]
print(f"Name: {name_max} \nIndex: {INDEX}")
print(pokemon_data[INDEX])

# question 4
MAX_ABILITIY = 0
INDEX = 0
for i, pokemon in enumerate(pokemon_data):
    if pokemon["abilities"] != "abilities not available yet":
        if len(pokemon["abilities"]) > MAX_ABILITIY:
            MAX_ABILITIY = len(pokemon["abilities"])
            INDEX = i

ability_name = pokemon_data[INDEX]["name"]
print(f"Ability name {ability_name}")
print(pokemon_data[INDEX])

file_data.close()
