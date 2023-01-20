def tip(a, t):
    return a * (1 + (t/100))

total = int(input("Bill: "))
percent = int(input("Percent Tip: "))

print("Your total is " + str(tip(total, percent)));