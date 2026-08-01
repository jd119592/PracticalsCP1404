import pickle
import json
from programming_language import ProgrammingLanguage


"""
CP1404 Pickle and JSON Demo
- Using JSON strings
- Using pickling to save and load variables 
in memory to and from a binary file
"""
# First we start with this data string, stored in JSON form
#a list of dictionary like objects
start_string =  '[{"name": "Python", "typing": "Dynamic", "Reflection": true, "Year": 1991}, {"name": "Ruby", ' \
                '"typing": "Dynamic", "reflection": true, "year": 1995}] '
languages = json.loads(start_string) # Load String = loads
print(languages, type(languages))

for i, language in enumerate(languages):
    languages[i] = ProgrammingLanguage(*languages[0].values())
p = ProgrammingLanguage(*languages[0].values())


# Let's add another language to it
visual_basic = ProgrammingLanguage("visual Basic", "static", False, 1995)
languages.append(visual_basic)

# Convert ("dump") our data in memory to a JSON string
json_string = json.dumps(languages, default=vars)
print("JSON string: ")
print(json_string)

filename = input("Enter filename to write to: ")

# Notice mode is "wb" for write bytes
with open(filename, "wb") as out_file:
    pickle.dump(languages, file=out_file)

# Try loading the file you just saved... what does it look like?

# Now let's load the binary file into a new variable
print("Loading...")
with open(filename, "rb") as in_file:
    data = pickle.load(file=in_file)
print(data, type(data))