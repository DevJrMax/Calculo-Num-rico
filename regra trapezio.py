import math
def trapezio(a,b,m,funcao):
    resultado = 0
    x = a
    h = (b - a)/m
    for i in range(m+1):
        if i==0 or i==m:
            c=1
        else:
            c=2
        y = eval(funcao)
        print("|", i, "|", x, "|", y, "|", c, "|")
        resultado = resultado + y*c
        x = x + h
    print((h/2)*resultado)

trapezio(1,3,4,"pow(x,3) * math.log(x,2.71828)")

