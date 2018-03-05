import math
import time
funcao = "2 * pow(x,4) + 4 * pow(x,3) + 3 * pow(x,2) - 10 * x -15"
def posicaofalsa(a, b, funcao):
    while(1):
        x = a
        fa = eval(funcao)
        x = b
        fb = eval(funcao)

        c = (a * fb - fa * b)/(fb-fa)

        x = c

        fc = eval(funcao)

        if(fc<0):
            a = c
        else:
            b = c
        print("a = %f, b = %f, c = %f | fa = %f, fb = %f, fc = %f" % (a, b, c, fa, fb, fc))
        if(round(a,11)==round(b,11)):
            break
posicaofalsa(1,3,funcao)