import numpy as np

n = int(input("Enter number of students: "))
s = int(input("Enter number of subjects: "))

names = []

for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    names.append(name)

# Store marks
marks = []

for i in range(n):
    student_marks = []
    print(f"\nEnter marks for {names[i]}:")

    for j in range(s):
        mark = float(input(f"Subject {j+1}: "))
        student_marks.append(mark)

    marks.append(student_marks)

marks = np.array(marks)
names = np.array(names)

total_marks = np.sum(marks , axis = 1)
print("Total Marks of each student: " , total_marks)

avg_marks_of_student = np.mean(marks , axis = 1)
print("Average Marks :- ", avg_marks_of_student)

topper_index = np.argmax(total_marks)
print("Class Topper:",names[topper_index])
print("Highest Marks:", total_marks[topper_index])

lowest_index = np.argmin(total_marks)
print("Class Lowest:",names[lowest_index])
print("Lowest Marks: ", total_marks[lowest_index])

avg_marks = np.mean(marks , axis = 0)
print("Average marks of each Subject :- " , avg_marks)

failed = marks < 33
failed_student = np.any(failed , axis =1)
failed_names = np.array(names)[failed_student]
print("Name of student Failed :- " ,failed_names)

rank_index = np.argsort(total_marks)[::-1]
ranked_marks = total_marks[rank_index]
ranked_names = np.array(names)[rank_index]
print("Rank number :- " , np.arange(1,n+1))
print("Name of student Rank wise :- " , ranked_names)
print("Marks according to rank :- " , ranked_marks)

class_avg = np.mean(marks)
print("Class Average :- " , class_avg)

standard_deviation = np.std(total_marks)
print("Standard_deviation :- " , standard_deviation)