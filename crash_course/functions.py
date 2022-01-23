# A function is a block of code which only runs when it is called.
# In python, we don not use curly brackets, we sue identation with tabs or spaces


# Create a function
def sayHello(name):
    print(f"Hello {name}")


sayHello("Mutua")


# return values
def getSum(num1, num2):
    total = num1 + num2
    return total


print(getSum(3, 4))

# a lambda function is a small anonymous function. It can take any number of
# arguments, but can only have one expression. Ver similar to JS arrow functions

getSum2 = lambda num1, num2: num1 + num2

print(getSum2(10, 4))