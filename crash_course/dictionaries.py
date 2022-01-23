# A dicitonary is a collection which is unordered, changeable and indexed. No duplicate members

# Create a dictionary
person = {"first_name": "Joseph", "last_name": "Mutua", "age": "24"}

# Constructor
# person2 = dict("first_name": "Fala", "last_name": "Fulani", "age": "24")

# Add key/value
person["phone"] = "07689998435"

# Get dict keys
print(person.keys())

# get dict items
print(person.items())

# Copy a dictinary
person2 = person.copy()

person2["city"] = "Nairobi"

# Remove item
del(person["age"])
person.pop("phone")

# Clear
person.clear()

# Get Length
print(len(person2))


# List of dictionaries
people = [{"name": "John", "age": 30}, {"name": "Kevin", "age": 30}]

# print(person, type(person))
print(person2)