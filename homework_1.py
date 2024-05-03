# 1. Python List Transformation
# Objective: The aim of this assignment is to practice advanced list operations and transformations.
# Problem Statement: You've been given a list of numerical grades from a class exam. You need to process and analyze these grades.
# Task 1: Given the list of grades:
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
# Sort the grades in descending order and display the sorted list.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort(reverse=True)
print("grades", grades)

# Task 2: Calculate the average grade and display it.
grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
total=0
for grades in grades:
    total+=grades    
print(total/10)

# 2. Advanced List Methods and Identity Operators
# Objective: The aim of this assignment is to delve deeper into list methods and understand the nuances of identity operators.
# Problem Statement: You have two lists of student names. One list contains the names of students who have submitted their assignments, and the other list contains the names of students who attended the last class.
# Task 1: Given the two lists:
# Find out which students both submitted their assignments and attended the class.

submitted = ["Alice", "Bob", "Charlie", "David"]

attended = ["Charlie", "Eve", "Alice", "Frank"]

if submitted[0] in attended:
    print("this person attended and submitted their work", submitted[0])
    if submitted[1] in attended:
        print("this person attended and submitted their work", submitted[1])
    if submitted[2] in attended:
        print("this person attended and submitted their work", submitted[2])
    if submitted[3] in attended:
         print("this person attended and submitted their work", submitted[3])

# 3. Advanced Slicing Techniques
# Objective: The aim of this assignment is to master the art of slicing in Python lists.

# Problem Statement: You have a list of daily temperatures for a month, and you'd like to extract specific data from it.

# Task 1: Given the list of temperatures:

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
print(temperatures[7:14])

# Extract the temperatures for the second week (7 days) of the month (index 7 to index 14). Expected Outcome:
# 83, 85, 86, 87, 88, 89, 90,
# Task 2: Extract all the temperatures above 100. **hint** add the temperatures over 100 to a new list.

temperature = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]
new_list=[]
for temp in temperature:
    if temp >=100:
        new_list.append(temp)
print(new_list)

# while i<len(temp):
#     if temp[] > 100:
#         print("the numbers above 100:"[i])


