import json

with open('Input/students.json', 'r', encoding='utf-8') as f:
    students = json.load(f)

a_names = [student['name'] for student in students if student['name'].startswith('A')]

a_names = sorted(a_names)

output = {"a_names": a_names}

with open('Output/output14.json', 'w', encoding='utf-8') as f:
    json.dump(output, f, ensure_ascii=False, indent=2)
