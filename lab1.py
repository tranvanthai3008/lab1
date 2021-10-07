import json
# question 1 and 2
char_total = 0 # q1
char_total_format = 0 # q2
text_data  = open("pokemon_full.json", "r")
for line in text_data:
	string_line = str(line)
	# print(len(string_line))
	char_total += len(string_line)
	char_total_format += len(string_line) - string_line.count(" ") - string_line.count(".")

print("character total: "+str(char_total))
print("character total after striming \".\" and \" \": " + str(char_total_format))

# question 3
file_data = open("pokemon_full.json" , "r")
pokemon_data = json.load(file_data) # type of data is list (1 dim array )
max_of_len = 0
index = 0
for i, pokemon in enumerate(pokemon_data):
	if pokemon["description"] != "Description not available yet":
		if len(pokemon["description"]) > max_of_len:
			max_of_len = len(pokemon["description"])
			index = i
		
print(max_of_len)		
print("name: "+pokemon_data[index]["name"]+ "\nindex: "+str(index))
print(pokemon_data[index])

#question 4

file_data = open("pokemon_full.json" , "r")
pokemon_data = json.load(file_data) # type of data is list (1 dim array )
max_of_len = 0
index = 0
for i, pokemon in enumerate(pokemon_data):
	if pokemon["abilities"] != "abilities not available yet":
		if len(pokemon["abilities"]) > max_of_len:
			max_of_len = len(pokemon["abilities"])
			index = i
		
print(max_of_len)		
print("name: "+pokemon_data[index]["name"]+ "\nindex: "+str(index))
print(pokemon_data[index])
