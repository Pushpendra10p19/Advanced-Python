# dump() Method is used to save Python dictionary into JSON String file
import json
data = {
    "name": "Pushpendra",
    "age": 20,
    "RollNo": 101,
    "College": "AKTU",
    "Address": {
        "City": "Agra",
        "State": "UP",
        "Country": "India"
        
    }       
}
with open("data.json", "w") as file:
    json.dump(data, file)
print(data)
print(type(data))
