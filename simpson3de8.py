import math
def simpson3de8(a,b,m,funcao):
    resultado = 0
    x = a
    h = (b - a)/m
    for i in range(m+1):
        if i==0 or i==m:
            c=1
        elif i%3==0:
            c=2
        else:
            c=3
        y = eval(funcao)
        print("|", i, "|", x, "|", y, "|", c, "|")
        resultado = resultado + y*c
        x = x + h
    print((3*h/8)*resultado)

simpson3de8(1,4,6,"math.log((pow(x,3) + math.sqrt(math.exp(x)+1)),2.71828)")
