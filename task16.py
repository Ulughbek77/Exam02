import csv

with open('Input/grades.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    students = list(reader)

count_5 = sum(1 for student in students if int(student['grade']) == 5)

result = f"5 baho olganlar soni: {count_5}"

with open('Output/output16.txt', 'w', encoding='utf-8') as file:
    file.write(result)
