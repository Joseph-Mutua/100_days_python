# JSON is commonly used with data APIs. Here we see how to parse JSONinto a Python dictionary
import json

# Sample JSON
userJSON = '{"first_name": "John", "last_name": "Mutua"}'

# Parse to Dictionary
user = json.loads(userJSON)

print(user)
print(user["last_name"])

# Turn a dictionary into JSON format
car = {"make": "ford", "model": "mustang"}
carJSON = json.dumps(car)
print(carJSON)
