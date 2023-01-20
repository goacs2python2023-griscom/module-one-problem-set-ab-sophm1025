import random

def dice():
    d1 = random.randint(1,6);
    d2 = random.randint(1,6);
    if d1 + d2 == 6 or d1 + d2 == 7 or d1 + d2 == 8:
        return "win";
    else:
        return "lose";

print(dice())

