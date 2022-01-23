# If/else conditions are used to decide to do something based on sth being true/false

x = 10
y = 10

# Comparison operators (==, !=, >, <, >=, <=) used to compare values
if x > y:
    print(f"{x} is greater than {y}")
elif x == y:
    print(f"{x} is equal to {y}")
else:
    print(f"{y} is greater than {x}")

# Nested if statement
if x > 2:
    if x <= 10:
        print(f"{x} is greater than 2 and less than or equal to 10")

# Logical Operators (and, or, not) - Used to combine conditional statements
# and
if x > 2 and x <= 10:
    print(f"{x} is greater than 2 and less than oor equal to 10")

# or
if x > 2 or x <= 10:
    print(f"{x} is greater than 2 or less than oor equal to 10")

# not
if not (x == y):
    print(f"{x} is not equal to {y}")

# Membership operators (not, not in) - Used to test if a sequence is presented in an object
numbers = [1, 2, 4, 5, 7]

# in
if 2 in numbers:
    print(2 in numbers)

# not in
if 2 not in numbers:
    print(2 not in numbers)

# Identity Operators (is, is not) - Compare the objects, not if they are equal,
# but if they are actually the same object, with the same memory location

# is
if x is y:
    print(x is y)

# is not
if x is not y:
    print(x is y)