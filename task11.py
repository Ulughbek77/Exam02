import json

with open("Input/students.json", "r", encoding="utf-8") as file:
    students = json.load(file)

count = len(students)

result = {"count": count}
with open("Output/output11.json", "w", encoding="utf-8") as outfile:
    json.dump(result, outfile, indent=2)
