import time

def bisseccao(inicio, fim):
    a = inicio
    b = fim

    c = (a+b)/2
    fc = (pow(c, 3) - 5)
    while(round(fc,6)!=0.000000):

        fa = (pow(a,3) - 5)
        fb = (pow(b,3) - 5)

        print("a=%f b=%f f(a)=%f f(b)=%f c=%f f(c)=%f"%(a, b, fa, fb, c, fc))
        #print(fc)

        #print("a=%f b=%f c=%f" % (a, b, c))

        if(fc<0):
            a=c
        elif(fc>0):
            b=c

        c = (a + b) / 2
        fc = (pow(c, 3) - 5)



bisseccao(1,2)
