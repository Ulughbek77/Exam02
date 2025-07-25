import csv

with open('Input/grades.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    students = list(reader)

for student in students:
    student['grade'] = int(student['grade'])

top_student = max(students, key=lambda x: x['grade'])

result = f"Bahosi eng yuqori o'quvchi: {top_student['name']} - {top_student['grade']}"

with open('Output/output15.txt', 'w', encoding='utf-8') as file:
    file.write(result)
