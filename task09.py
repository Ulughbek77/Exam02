with open("Input/numbers.txt") as file:
    numbers = file.read().split()

numbers = [int(n) for n in numbers]

max_number = max(numbers)

with open("Output/output09.txt", "w") as file:
    file.write(f"Eng katta son: {max_number}")