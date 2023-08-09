print("Problem 54")

global p1wins
global p2wins


def convert_cardnum(cardnum):
    cardnumlist = "23456789TJQKA"
    return cardnumlist.find(cardnum)


def convert_cardsuit(cardsuit):
    cardsuitlist = "SHCD"
    return cardsuitlist.find(cardsuit)


file = open("test.txt", "r")
p1wins = 0
p2wins = 0
lines = file.readlines()
for line in lines:
    count = 0
    p1cardnum = [0] * 13
    p1cardsuit = [0] * 4
    p1rating = 0
    p2rating = 0
    for a in range(0, len(line) + 1):
        if count < 5:
            if a % 3 == 0:
                index = convert_cardnum(line[a])
                print(line[a])
                p1cardnum[index] = p1cardnum[index] + 1
            elif a % 3 == 1:
                index = convert_cardsuit(line[a])
                print(line[a])
                p1cardsuit[index] = p1cardsuit[index] + 1
                count = count + 1
    print(p1cardnum)
    print(p1cardsuit)
