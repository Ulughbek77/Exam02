with open("input/numbers.txt") as file:
    numbers = file.read().split()

numbers = [int(n) for n in numbers]
total = sum(numbers)

with open("Output/output08.txt", "w") as file:
    file.write(f"Yig'indi: {total}")