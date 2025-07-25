def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "0ga bolish mumkin emas"
    
a = float(input("1-son: "))
amal = input("Amal (+, -, *, /): ")
b = float(input("2-son: "))

if amal == "+":
    result = add(a, b)
elif amal == "-":
    result = subtract(a, b)
elif amal == "*":
    result = multiply(a, b)
elif amal == "/":
    result = divide(a, b)
else:
    result = "Noto'g'ri amal kiritildi!"

print("Natija", result)
