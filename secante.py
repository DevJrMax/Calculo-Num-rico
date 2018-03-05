import math

funcao = "2 * pow(x,4) + 4 * pow(x,3) + 3 * pow(x,2) - 10 * x -15"


def secante(m, x0, x1, funcao):
    x=x0
    fx0 = eval(funcao)
    x=x1
    fx1 = eval(funcao)
    for i in range(m):
        if(fx1-fx0)==0:
            break
        x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0)
        x0, x1 = x1, x2
        x=x2
        fx0, fx1 = fx1, eval(funcao)
        print("X %d = %f" % (i, x2))

secante(100, 1, 3, funcao)