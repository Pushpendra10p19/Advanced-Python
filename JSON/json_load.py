# load() Methode is used to read the data from JSON file and Show the data in Dictionary file
import json
with open("data.json", "r") as file:
    data = json.load(file)
print(data)
print(type(data))
