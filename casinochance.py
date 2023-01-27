wantedNum = input("Pick 2 numbers you want to roll: ");
w1, w2 = map(int, wantedNum.split());

value = input("Pick 6 values for the dice faces: ");
v1, v2, v3, v4, v5, v6 = map(int, value.split());

list = [v1, v2, v3, v4, v5, v6];

def prob(w):
    count = 0;

    for i in list:
        if i == w:
            count += 1;

    return count;

print (prob(w1)/6 * prob(w2)/6);

