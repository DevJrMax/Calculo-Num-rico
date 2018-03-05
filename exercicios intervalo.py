import matplotlib.pyplot as plt
import math

eixoX = []
eixoM = []

def newtonMethod(inicio, fim, passo, casas):

    while(inicio!=fim):
        x=inicio
        #13
        #x = x - (2 * pow(x,3) - 6 * pow(x, 2) + 3 * x + 1) / (6 * pow(x,2) - 12 * x + 3)

        #14
        #x = x - (pow(x,4) + x - 4)/(4 * pow(x, 3) + 1)

        #15 1-2
        #x = x - (math.sin(x) - pow(x,2))/ (math.cos(x) - 2 * x)

        #16 0.5-1.5
        #x = x - (2 * math.cos(x) - pow(x, 4)) / (-math.sin(x) - 4 *  pow(x,3))

        #17 0.5-1.5
        #x = x - (pow(x,4) - x - 1) / (4 * pow(x, 3) - 1)

        #18 0-1
        #x = x - (math.exp(x) + 2 * x - 3) / (math.exp(x) + 2)

        #19 0-1
        #x = x - (math.atan(x) + x - 1) / ((1 / (pow(x, 2) + 1)) + 1)

        #20 1-2
        #x = x - (pow(x,4) - x - 3)/(4 * pow(x,3) - 1)

        #21 0-1
        #x = x - (math.cos(pow(x, 2)) - x) / ((2 * x * (-math.sin(pow(x, 2)))) - 1)

        #22 1-2
        #x= x - ( math.tan(pow(x,2)) + pow(x,2) - 1)/(2 * x *pow(1/math.cos(pow(x,2)),2) + 2 * x)

        #23 -2.0- -1.0
        #x = x - (pow(x,5) - pow(x,4) - 5 * pow(x,3) + 4 * x + 3)/(5 * pow(x,4) - 4 * pow(x,3) - 15 * pow(x,2) + 4)

        print("Inicio",inicio,"=",round(x/passo,casas))
        eixoX.append(inicio)
        eixoM.append(x)
        inicio = inicio + 0.01
        inicio = round(inicio, 2)

#13
#newtonMethod(2.0,3.0,1000,6)

#14
#newtonMethod(1.0,2.0,1000,6)

#15
#newtonMethod(0.0,1.0,1000,6)

#16
#newtonMethod(0.5,1.5,1000,6)

#17
#newtonMethod(0.5,1.5,1000,6)

#18
#newtonMethod(0.0,1.0,1000,6)

#19
#newtonMethod(0.0,1.0,1000,6)

#20
#newtonMethod(1.0,2.0,1000,6)

#21
#newtonMethod(0.0,1.0,1000,6)

#22
#newtonMethod(1.0,2.0,1000,6)

#23
#newtonMethod(-3.0,3.0,1000,8)

plt.plot(eixoM, eixoX)
plt.show()