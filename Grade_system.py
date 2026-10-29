# Dictionary of marks of students

student_marks = {
    "Saniya" : 78,
    "Ajay" : 67,
    "Diksha" : 89,
    "Sahil" : 65,
    "Nikhil" : 56,
    "Ratisha" : 72,
    "Tanuja" : 43,
    "Tanuj" : 34,
    "Simran" : 98
}
print(student_marks)
print("\n")
student_grade = {}

for i in student_marks:
    marks = student_marks[i]
    
    if marks > 90:
        student_grade[i] = "A+"
    elif marks > 80:
        student_grade[i] = "A"
    elif marks > 70:
        student_grade[i] = "B+"
    elif marks > 60:
        student_grade[i] = "B"
    elif marks > 50:
        student_grade[i] = "C"
    elif marks >= 41:
        student_grade[i] = "D"
    else:
        student_grade[i] = "F"

print(student_grade)
