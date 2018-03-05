def van(interacao,a,b,funcao):
    x = a
    fa = eval(funcao)
    x = b
    fb = eval(funcao)
    if fa>=0 and fb>=0:
        print("Deu ruim")

    if fa * fb >=0:
        if fa < fb:
            return a
        else:
            return b

    if abs(fa)<abs(fb):
        aux = a
        a = b
        b = a

    c = a
    fc = fa

    flag = True


    print(b)