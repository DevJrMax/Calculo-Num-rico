import matplotlib.pyplot as plt
import numpy as np
import math

def newtonMethod(interacao, x, funcao, derivada):
    raiz = []
    for i in range(0, interacao):
        newX = x - (eval(funcao))/(eval(derivada))
        x = newX
        raiz.append(x)
        print("Metodo de Newton:",(i+1),"=",x)
    return raiz

def bisseccao(interacao, inicio,fim, funcao):
    raiz = []
    a = inicio
    b = fim
    for i in range(interacao):
        c = (a + b) / 2
        x = c
        fc = eval(funcao)
        x=a
        fa = eval(funcao)
        x=b
        fb = eval(funcao)
        if (fc < 0):
            a = c
        elif (fc > 0):
            b = c
        c = (a + b) / 2
        x=c
        raiz.append(c)
        print("Bissecção:", (i + 1), "=", c)
        fc = eval(funcao)
    return raiz

def secante(interacao, x0, x1, funcao):
    raiz = []
    x=x0
    fx0 = eval(funcao)
    x=x1
    fx1 = eval(funcao)
    for i in range(interacao):
        if(fx1-fx0)!=0:
            x2 = (x0 * fx1 - x1 * fx0) / (fx1 - fx0)
        x0, x1 = x1, x2
        x=x2
        fx0, fx1 = fx1, eval(funcao)
        print("Secante %d = %f" % ((i+1), x2))
        raiz.append(x2)
    return raiz

def posicaoFalsa(interacao, a, b, funcao):
    raiz = []
    for i in range(interacao):
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
        print("Posição falsa %d = %f" % ((i+1), c))
        raiz.append(c)
    return raiz

def pegaso(interacao, x0, x1, funcao):
    raiz =[]
    for i in range(interacao):
        x = x0
        fx0 = eval(funcao)
        x = x1
        fx1 = eval(funcao)
        if((fx1-fx0)*(x1-x0))!=0:
            x2 =  x1 - fx1/(fx1-fx0)*(x1-x0)
        x = x2
        fx2 = eval(funcao)
        x0 = x1
        x1 = x2
        raiz.append(x2)
        print("Pegaso %d = %f" % (i, x2))
    return raiz

def schroder(interacao, m, x, funcao, derivada):
    raiz =[]
    for i in range(interacao):
        x1 = x - m * (eval(funcao)/eval(derivada))
        x= x1
        raiz.append(x1)
        print("Schroder %d = %f" % (i, x1))
    return raiz

def muller(interacao, x0, x1, x2, funcao):
    raiz = []
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
        raiz.append(x3)

        print("Muller %d = %f" % (i, x3))
    return raiz

funcao = "2 * pow(x,4) + 4 * pow(x,3) + 3 * pow(x,2) - 10 * x -15"
derivada = "8 * pow(x,3) + 12 * pow(x,2) + 6 * x - 10"

#Funcao
x_values1 = np.linspace(-4.0, 3.0, 10000)
y_values1 = [ ]
#Funcao

linhaY = np.linspace(0, 0, 10000)

#Interacao
interacao = range(0, 51)
#Interacao

#Funcao
for i in range(len(x_values1)):
    x = x_values1[i]
    y = eval(funcao)
    y_values1.append(y)
#Funcao

#Newton
raizNewton = newtonMethod(len(interacao), 1, funcao, derivada)
#Newton

#Bissecção
raizBisseccao = bisseccao(len(interacao), 0, 3, funcao)
#Bissecção

#Secante
raizSecante = secante(len(interacao), 1, 3, funcao)
#Secante

#Posição falsa
raizFalsaPosicao = posicaoFalsa(len(interacao), 1, 3, funcao)
#Posição falsa

#Pegaso
raizPegaso = pegaso(len(interacao), 1, 3, funcao)
#Pegaso

#Schroder
raizSchroder = schroder(len(interacao), 1, 3, funcao,derivada)
#Schroder

#Schroder
raizMuller = muller(len(interacao),0,1,1.5,funcao)
#Schroder

fig=plt.figure()

#Funcao
ax=fig.add_subplot(111, label="1")
#Funcao

#Metodo Newton
ax2=fig.add_subplot(111, label="2", frame_on=False)
#Metodo Newton

#Metodo Bissecção
ax3=fig.add_subplot(111, label="3", frame_on=False)
#Metodo Bissecção

#Metodo Secante
ax4=fig.add_subplot(111, label="4", frame_on=False)
#Metodo Secante

#Metodo Posição falsa
ax5=fig.add_subplot(111, label="5", frame_on=False)
#Metodo Posição falsa

#Metodo Pegaso
ax6=fig.add_subplot(111, label="6", frame_on=False)
#Metodo Pegaso

#Metodo Schroder
ax7=fig.add_subplot(111, label="7", frame_on=False)
#Metodo Schroder

#Metodo Muller
ax8=fig.add_subplot(111, label="8", frame_on=False)
#Metodo Muller

#Funcao
ax.plot(x_values1, y_values1, color="C0", label="Função")
ax.set_xlabel("X", color="C0")
ax.set_ylabel("FUNÇÃO", color="C0")
ax.tick_params(axis='x', colors="C0")
ax.tick_params(axis='y', colors="C0")
#Funcao

#Geral
ax2.xaxis.tick_top()
ax2.yaxis.tick_right()
ax2.set_xlabel('INTERAÇÃO', color="RED")
ax2.set_ylabel('RAIZ', color="RED")
ax2.xaxis.set_label_position('top')
ax2.yaxis.set_label_position('right')
ax2.tick_params(axis='x', colors="RED")
ax2.tick_params(axis='y', colors="RED")
#Geral

#Metodo Newton
ax2.set_ylim([-3,6])
ax2.plot(interacao, raizNewton, color="GREEN", marker="o", label="Newton")
#Metodo Newton

#Metodo Bissecção
ax3.set_ylim([-3,6])
ax3.set_xticks([])
ax3.set_yticks([])
ax3.plot(interacao, raizBisseccao, color="PINK", marker="*", label="Bissecção")
#Metodo Bissecção

#Metodo Secante
ax4.set_ylim([-3,6])
ax4.set_xticks([])
ax4.set_yticks([])
ax4.plot(interacao, raizSecante, color="BLACK", marker="x", label="Secante")
#Metodo Secante

#Metodo Posição falsa
ax5.set_ylim([-3,6])
ax5.set_xticks([])
ax5.set_yticks([])
ax5.plot(interacao, raizFalsaPosicao, color="YELLOW", marker="d", label="Pos. Falsa")
#Metodo Posição falsa

#Metodo Pegaso
ax6.set_ylim([-3,6])
ax6.set_xticks([])
ax6.set_yticks([])
ax6.plot(interacao, raizPegaso, color="ORANGE", marker="+", label="Pegaso")
#Metodo Pegaso

#Schroder
ax7.set_ylim([-3,6])
ax7.set_xticks([])
ax7.set_yticks([])
ax7.plot(interacao, raizSchroder, color="GRAY", marker="h", label="Schroder")
#Schroder

#Muller
ax8.set_ylim([-3,6])
ax8.set_xticks([])
ax8.set_yticks([])
ax8.plot(interacao, raizMuller, color="PURPLE", marker="^", label="Muller")
#Muller


ax.legend(bbox_to_anchor=(1, 1))
ax2.legend(bbox_to_anchor=(1, 0.93))
ax3.legend(bbox_to_anchor=(1, 0.86))
ax4.legend(bbox_to_anchor=(1, 0.79))
ax5.legend(bbox_to_anchor=(1, 0.72))
ax6.legend(bbox_to_anchor=(1, 0.65))
ax7.legend(bbox_to_anchor=(1, 0.58))
ax8.legend(bbox_to_anchor=(1, 0.51))

plt.show()