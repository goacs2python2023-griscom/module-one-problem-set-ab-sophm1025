topCards = input("3 Top Letters: ");
t1, t2, t3 = map(str, topCards.split());

bottomCards = input("3 Bottom Letters: ");
b1, b2, b3 = map(str, bottomCards.split());

letters = [t1, t2, t3, b1, b2, b3];

countA = 0;
for i in letters:
    if i == "A":
        countA += 1;

countD = 0;
for i in letters:
    if i == "D":
        countD += 1;

if countD >= 2 and countA >= 1:
    print("Yes");
else:
    print("No")