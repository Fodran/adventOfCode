f = open("../input", "r")

numbers = []

for line in f:
    numbers.append(int(line))

for a in numbers:
    for b in numbers:
        for c in numbers:
            if(a+b+c==2020):
                break
        if(a+b+c==2020):
            break
    if(a+b+c==2020):
        break

print(a*b*c)
