from math import fabs, log, tan, sqrt, cos

def F(x):
    return tan(x) - sqrt(x-12)

def f(x):
    return (1/cos(x))**2 - (sqrt(x-12)**(-0.5))/2

def metodo_iterativo(E,x1,x2):
    global x
    
    for k in range(100000000):

        x2 = x1 - F(x1)/f(x1)

        fx2 = F(x2)

        if fabs(fx2) < E or fabs(x2-x1) < E:
            x = x2
            break

        print(f'{x2:.3f}')

        x1 = x2


x = x1 = 13

x2 = None

E = 0.001

if not (fabs(F(x1)) < E):
    metodo_iterativo(E,x1,x2)

print(f'{x:.3f}')