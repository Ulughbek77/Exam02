def convert_fish(fish):
    abs = fish.split()
    if len(abs) == 3:
        familiya, ism, sharif = abs
        return f"{ism} {sharif}, {familiya}"
    else:
        return "Format noto'g'ri! Familiya Ism"

fish = input("FISH kiriting (Familiya ism sharif): ")

print("Natija:", convert_fish(fish))