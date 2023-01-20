def fast(t1,t2,t3,t4):
    total = 1;
    if t2 < t1:
        total+=1;
    if t3 < t1:
        total+=1;
    if t4 < t1:
        total+=1;
    
    if (total == 1):
        return "gold";
    elif (total == 2):
        return "silver";
    elif (total == 3):
        return "bronze";
    else:
        return "no medal";25

yourTime = int(input("Your time: "));
time1 = int(input("Opponent time: "));
time2 = int(input("Opponent time: "));
time3 = int(input("Opponent time: "));

print("You got " + fast(yourTime, time1, time2, time3))