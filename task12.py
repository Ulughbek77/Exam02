import json

with open('Input/students.json', 'r', encoding='utf-8') as f:
    students = json.load(f)

names = [student['name'] for student in students]

sorted_names = sorted(names)

output = {"sorted_names": sorted_names}

with open('Output/output12.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
