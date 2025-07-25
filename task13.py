import json

with open('Input/students.json', 'r', encoding='utf-8') as file:
    students = json.load(file)

names = [student['name'] for student in students]

sorted_names = sorted(names)

output = {"sorted_names": sorted_names}

with open('Output/output13.json', 'w', encoding='utf-8') as file:
    json.dump(output, file, ensure_ascii=False, indent=2)
    
names = sorted(set(student['name'] for student in students))
