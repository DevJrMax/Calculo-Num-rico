import math
def simpson1de3(a,b,m,funcao):
    resultado = 0
    x = a
    h = (b - a)/m
    for i in range(m+1):
        if i==0 or i==m:
            c=1
        elif i%2==0:
            c=2
        else:
            c=4
        y = eval(funcao)
        print("|", i, "|", x, "|", y, "|", c, "|")
        resultado = resultado + y*c
        x = x + h
    print((h/3)*resultado)

simpson1de3(0,1,4,"1/(1 + pow(x,2))")

