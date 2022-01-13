# strings
print("Helloo"[3])

# Integers
print(123 + 435)

print(123_476_98)

# Floats
print(3.256)

# Booleans
# True / False

num_char = len(input("What is your name?"))

print(type(num_char))

print("Your name has " + str(num_char) + " characters")

two_digit_num = input("Type a 2 digit number\n")

print(type(two_digit_num))

first_digit=two_digit_num[0]
second_digit=two_digit_num[1]

print(float(first_digit) + float(second_digit))

print(int(first_digit) + int(second_digit))

# Mathematical operations
# Division always brings floating point results
print(6 / 3)

# Power
print(2**4)

height = input("Enter your height in metres: \n")
weight = input("Enter your weight in kg: \n")



bmi_index = int(((float(weight) / (float(height)**2))))

print("your BMI index is: " + str(bmi_index))