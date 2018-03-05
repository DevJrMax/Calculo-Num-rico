import math


def newtonMethod(m, x):
    for i in range(1, m + 1):
        # newX = x - (pow(x,3) - 2 * x - 5)/(3 * pow(x,2) - 2)
        # newX = x - (pow(x, 6) - 2) / (6 * pow(x, 5))
        # newX = x - ((math.cos(x) - x)/(-math.sin(x) - 1))

        # Exemplo a
        # newX = x - (pow(x, 3) - 30)/(3 * pow(x, 2))

        # Exemplo b
        # newX = x - (pow(x, 7) - 1000)/(7 * pow(x, 6))

        # Exemplo c
        # newX = x - (pow(x, 13) - 13)/(13 * pow(x, 12))

        # newX = x - (2 * pow(x, 3) - 6 * pow(x, 2) + 3 * x + 1) / (6 * pow(x, 2) - 12 * x + 3)

        # 15
        # newX = x - (math.sin(x) - pow(x, 2)) / (math.cos(x) - 2 * x)

        # 16
        # newX = x - (2 * math.cos(x) - pow(x, 4)) / (-math.sin(x) - 4 *  pow(x,3))

        # 17
        # newX = x - ((pow(x,4) - x - 1) / (4 * pow(x, 3) - 1))

        # 18
        #newX = x - (math.exp(x) + 2 * x - 3) / (math.exp(x) + 2)

        # 19
        #newX = x - (math.atan(x) + x - 1) / ((1 / (pow(x, 2) + 1)) + 1)

        # 20
        #newX = x - (pow(x,4) - x - 3)/(4 * pow(x,3) - 1)

        # 21
        #newX = x - (math.cos(pow(x,2))-x)/((2 * x * (-math.sin(pow(x,2))))-1)

        # 22
        #newX = x - ( math.tan(pow(x,2)) + pow(x,2) - 1)/(2 * x *pow(1/math.cos(pow(x,2)),2) + 2 * x)

        # 23
        newX = x - (pow(x,5) - pow(x,4) - 5 * pow(x,3) + 4 * x + 3)/(5 * pow(x,4) - 4 * pow(x,3) - 15 * pow(x,2) + 4)

        x = newX

        print("X %d = %.6f" % (i, newX))


newtonMethod(15, 2)