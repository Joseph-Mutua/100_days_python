# Lists -  A collection which is ordered and changeable. Allows duplicate memmbers

# Create list
numbers = [1, 2, "str"]

# Using a constructor
numbers2 = list((1, 2, "str"))

fruits = ["Apples", "Oranges", "Grapes", "Pears"]

# Append to List
fruits.append("Mangoes")

# Insert into position
fruits.insert(2, "Strawberries")

# Remove from list
fruits.remove("Apples")

# Remove with pop
fruits.pop(2)

# Reverse List
fruits.reverse()

# Sort list
fruits.sort()

# Reverse sort
fruits.sort(reverse=True)

fruits[0] = "Blueberries"

print(fruits)