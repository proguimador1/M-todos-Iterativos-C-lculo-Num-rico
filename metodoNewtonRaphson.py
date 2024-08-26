from math import fabs 

def F(x):
    return ... #aqui vai a função

def f(x):
    return ... #aqui vai a derivada da função

def metodo_iterativo(E,x1,x2):
    global x
    
    for k in range(100000000):

        x2 = x1 - F(x1)/f(x1)

        fx2 = F(x2)

        if fabs(fx2) < E or fabs(x2-x1) < E:
            x = x2
            break

        x1 = x2


x = x1 = ... #valor inicial

x2 = None

E = ... #precisão desejada

if not (fabs(F(x1)) < E):
    metodo_iterativo(E,x1,x2)

p = ... #precisão de casas decimais a serem impressas

print(f'{x:.{p}f}')