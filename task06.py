def calculate_average(grades):
    return sum(grades.values()) / len(grades)

def above_average_students(students):
    avg = calculate_average(students)
    above = [name for name, grade in students.items() if grade > avg]
    return avg, above

students = {'Ali': 5, 'Vali': 4, 'Hasan': 5, 'Husan': 3}

average, top_students = above_average_students(students)

print("O'rtacha baho:", round(average, 2))
print(f"{round(average, 2)} dan yuqorilar:", ", ".join(top_students))