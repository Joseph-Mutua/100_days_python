# For Loop
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit + " Pie")
        
        
# Average height calculator  
student_heights = input("Input a list of student heights\n").split()

sum_of_heights = 0

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum_of_heights += student_heights[n]
    
avg_height = int(sum_of_heights/len(student_heights))
print(avg_height)