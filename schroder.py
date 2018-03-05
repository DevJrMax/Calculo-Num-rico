funcao = "2 * pow(x,4) + 4 * pow(x,3) + 3 * pow(x,2) - 10 * x -15"
derivada = "8 * pow(x,3) + 12 * pow(x,2) + 6 * x - 10"
def schroder(interacao,m,x,funcao,derivada):
    raiz =[]
    for i in range(interacao):
        x1 = x - m * (eval(funcao)/eval(derivada))
        print(x,x1)
        x= x1
        raiz.append(x1)

schroder(15,1,1,funcao,derivada)