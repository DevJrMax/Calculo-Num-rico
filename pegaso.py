funcao = "2 * pow(x,4) + 4 * pow(x,3) + 3 * pow(x,2) - 10 * x -15"
def pegaso(interacao,x0,x1,funcao):
    raiz =[]
    for i in range(interacao):
        x = x0
        fx0 = eval(funcao)
        x = x1
        fx1 = eval(funcao)
        x2 =  x1 - fx1/(fx1-fx0)*(x1-x0)
        x = x2
        fx2 = eval(funcao)
        x0 = x1
        x1 = x2
        raiz.append(x2)
        print("X %d = %f" % (i, x2))
    return raiz

pegaso(15,1,3,funcao)