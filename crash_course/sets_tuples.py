# A tuple is a collection which is ordered and unchangeable. Allows duplicate members

# Create tuple
fruits = ("Apples", "Oranges", "Grapes")
fruits2 = tuple(("Apples", "Oranges", "Grapes"))

# single value needs trailing comma
fruits3 = ("Mangoes",)

# Get a value
print(fruits[1])

# Cant change value
# fruits[0] = "Pears"

# Delete tuple
del fruits3

# Get Length
print(len(fruits))


print(fruits)



# A Set is a collection which is unordered and unindexed. No duplicate members

# Create a set
fruits_set = {"Apples", "Oranges", "Mango"}

# Check if in set
print("Apples" in fruits_set)

# Add to set
fruits_set.add("GRape")

# Remove from set
fruits_set.remove("Oranges")

# Clear set
fruits_set.clear()

# Delete set
del fruits_set

print(fruits_set)