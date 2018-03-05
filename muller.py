import math
funcao = "2 * pow(x,4) + 4 * pow(x,3) + 3 * pow(x,2) - 10 * x -15"
def muller(interacao,x0,x1,x2,funcao):
    for i in range(interacao):
        x = x0
        fx0 = eval(funcao)
        x = x1
        fx1 = eval(funcao)
        x = x2
        fx2 = eval(funcao)

        h0 = x1 - x0
        h1 = x2 - x1

        if h1 != 0 and h0 != 0:

            aux0 = (fx1 - fx0)/h0

            aux1 = (fx2 - fx1)/h1

            a = (aux1 - aux0)/(h1 + h0)
            b = a * h1 + aux1
            c = fx2

            x3 = x2 + (-2 * c)/(b + math.sqrt(pow(b,2) - 4 * a * c))

            x0 = x1
            x1 = x2
            x2 = x3

        print(x3)

muller(15,0,1,1.5,funcao)

