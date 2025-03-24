from spy_parser import JsonParsingModel
import json

print("Parsing JSON")

json_string = json.dumps({
    "user": {
        "name": "Marcuth",
        "age": 19,
        "contact": {
            "email": "example@gmail.com"
        }
    }
})

root_parsing_model = JsonParsingModel({
    "name": {
        "query": "user.name"
    },
    "age": {
        "query": "user.age"
    },
    "email": {
        "query": "user.contact.email"
    }
})

data = root_parsing_model.parse(json_string)

print(data)