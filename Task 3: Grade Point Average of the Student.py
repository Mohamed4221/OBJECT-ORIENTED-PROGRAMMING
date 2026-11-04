# Task 3: Student Grade Average

number_of_grades = int(input("How many grades will you enter? "))

total = 0

for i in range(number_of_grades):
    grade = float(input("Enter grade: "))
    total = total + grade

average = total / number_of_grades

print("Average: {:.2f}".format(average))

if average >= 3.0:
    print("Student passed.")
else:
    print("Student failed.")
