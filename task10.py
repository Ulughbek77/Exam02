with open("Input/numbers.txt") as file:
    numbers = file.read().split()

numbers = sorted({int(n) for n in numbers})

with open("Output/output10.txt", "w") as file:
    for num in numbers:
        file.write(f"{num}\n")