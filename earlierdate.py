def earlier(day1, month1, year1, day2, month2, year2):
    if (year1 < year2):
        return "before";
    elif (year1 > year2):
        return "after";
    else:
        if (month1 < month2):
            return "before";
        elif (month1 > month2):
            return "after";
        else:
            if (day1 < day2):
                return "before";
            elif (day1 > day2):
                return "after";
            else:
                "same";

first = input("Please enter the first date in number format (day month year): ");
d1, m1, y1 = map(str, first.split());
second = input("Please enter the first date in number format (day month year): ");
d2, m2, y2 = map(str, second.split());
        
print("The first date comes " + earlier(d1,m1,y1,d2,m2,y2) + " the second date")