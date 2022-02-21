# # For Loop
# fruits = ["Apple", "Peach", "Pear"]

# for fruit in fruits:
#     print(fruit + " Pie")


# # Average height calculator
# student_heights = input("Input a list of student heights\n").split()

# sum_of_heights = 0

# for n in range(0, len(student_heights)):
#     student_heights[n] = int(student_heights[n])
#     sum_of_heights += student_heights[n]

#  # Can also use the sum function
# sum_of_heights = sum(student_heights)

# avg_height = int(sum_of_heights/len(student_heights))
# print(avg_height)

# # Write a program that calculates the highest score from a list of scores
# # Dont use the max/min functions
# student_scores = input("Input a list of student scores\n").split()

# for n in range(0, len(student_scores)):
#     student_scores[n] = int(student_scores[n])

# max_score = 0

# for score in student_scores:
#     if score > max_score:
#         max_score = score

# print(max_score)

# # Write a program that calculates the sum of even numbers from 1 to 100 including 100

# sum_of_nums = 0
# for num in range(1, 101):
#     if num % 2 == 0:
#         sum_of_nums += num

# print(sum_of_nums)


# Write a program that automatically prints the solution tot he FizzBuzz game

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
