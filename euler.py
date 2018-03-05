import math
def euler(a,b,m,y,funcao):
    x=a
    resultado = 0
    h = (b - a)/m
    for i in range(m+1):
        resultado = eval(funcao)
        print("|", round(i,5), "|", round(x,5), "|", round(y,5), "|", round(resultado,5), "|")
        y = y + h*resultado
        x = round(x + h,5)

euler(0,1,10,1,"x - 2 * y + 1")


