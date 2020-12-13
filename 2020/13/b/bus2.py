from functools import reduce



path = "../input"



def importData(path):
    f = open(path, "r")

    f.readline()
    data = [int(number) if(not(number == "x")) else number for number in f.readline().split(",")]
    #data = [1789,37,47,1889]
    output = [[int(number), data.index(number)] for number in data if(not(number == "x"))]

    f.close()

    return output



def chineseRemainder(timetable):
    modSum = 0
    a = [-item[1]%item[0] for item in timetable]
    n = [item[0] for item in timetable]
    
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        modSum += a_i * mul_inv(p, n_i) * p
    return modSum % prod



def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def main():
    print(chineseRemainder(importData(path)))
    return 0



if __name__ == "__main__":
    main()
