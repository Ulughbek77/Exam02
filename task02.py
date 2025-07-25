def deposit(balance, amount): 
    return balance + amount

def withdraw(balance, amount):
    if amount > balance:
        return "Balansda yetarli mablag' yo'q!"
    else:
        return balance - amount

def check_balance(balance): 
    return balance

balance = 100000

print("Amallar: deposit, withdraw, check")
action = input("Amalni Tanlang: ")

if action == "deposit":
    amount = int(input("Miqdor: "))
    balance = deposit(balance, amount)
    print("Balansda qoldi:", balance)

elif action == "withdraw":
    amount = int(input("Miqdor: "))
    result = withdraw(balance, amount)
    if isinstance(result, str):
        print(result)
    else:
        balance = result    
        print("Yangi balans", balance)

elif action == "check":
    print("Balans", check_balance(balance))

else: 
    print("Noto'g'ri amal kiritildi")


