import math
def euler(a,b,m,y,funcao,exata):
    print("-------------------------------------------")
    print("EULER")
    print("| i | x | y | eulerY-exataY(x) |")
    x=a
    resultado = 0
    h = (b - a)/m
    for i in range(m+1):
        resultado = eval(funcao)
        exataR = eval(exata)
        print("|", round(i,8), "|", round(x,8), "|",round(y,8),"|", abs(y - exataR),"|")
        y = y + h*resultado
        x = round(x + h,5)
    print("-------------------------------------------")

def eulerModificado(a,b,m,y,funcao,exata):
    print("-------------------------------------------")
    print("EULER MODIFICADO")
    print("| i | x | y | eulerModificadoY-exataY(x) |")
    x=a
    h = (b - a)/m
    for i in range(m+1):
        resultado = eval(funcao)
        auxX = x + h/2
        auxY = y + h/2 * resultado
        xBak = x
        yBak = y
        x=auxX
        y=auxY
        resultado = eval(funcao)
        yProx = yBak + h * resultado
        x = xBak
        exataR = eval(exata)
        y = yBak
        print("|", round(i, 8), "|", round(x, 8), "|", round(y, 8), "|", abs(y - exataR), "|")
        x = round(x + h, 5)
        y = yProx
    print("-------------------------------------------")
def eulerMelhorado(a,b,m,y,funcao,exata):
    print("-------------------------------------------")
    print("EULER MELHORADO")
    print("| i | x | y | eulerMelhoradoY-exataY(x) |")
    x=a
    h = (b - a)/m
    for i in range(m+1):
        resultado = eval(funcao)
        auxX = x + h
        auxY = y + h* resultado
        xBak = x
        yBak = y
        x=auxX
        y=auxY
        resultado2 = eval(funcao)
        yProx = yBak + h/2*(resultado + resultado2)
        x = xBak
        exataR = eval(exata)
        y = yBak
        print("|", round(i, 8), "|", round(x, 8), "|", round(y, 8), "|", abs(y - exataR), "|")
        x = round(x+ + h, 5)
        y = yProx
    print("-------------------------------------------")

def RK4(a,b,m,y,funcao):
    print("-------------------------------------------")
    print("RUNGE-KUTTA - ordem 4")
    print("| i | x | y |")
    x = a
    h = (b - a) / m
    for i in range(m+1):
        print("|", round(i, 8), "|", round(x, 8), "|", round(y, 8), "|")
        xBak = x
        yBak = y
        k1 = eval(funcao)
        x = xBak + h/2
        y = yBak + k1*h/2
        k2 = eval(funcao)
        x = xBak + h/2
        y = yBak + k2*h/2
        k3 = eval(funcao)
        x = xBak + h
        y = yBak + k3*h
        k4 = eval(funcao)
        y = yBak + h/6 * (k1 + 2 * k2 + 2 * k3 + k4)
        x = round(xBak + h, 5)
    print("-------------------------------------------")

euler(0,1,10,0.5,"-2 * x * pow(y,2)","1/(pow(x,2)+2)")
eulerModificado(0,1,10,0.5,"-2 * x * pow(y,2)","1/(pow(x,2)+2)")
eulerMelhorado(0,1,10,0.5,"-2 * x * pow(y,2)","1/(pow(x,2)+2)")
RK4(0,1,10,1,"x - 2*y + 1")




