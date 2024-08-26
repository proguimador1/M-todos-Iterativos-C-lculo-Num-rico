from math import fabs

def f(x):
    return ... #aqui vai a função principal

def fi(x):
    return ... #aqui vai a função φ(x)=x

def metodo_iterativo(E,x1,x2):
    global x
    
    for k in range(1000000000):

        x2 = fi(x1)

        fx2 = f(x2)

        if fabs(fx2) < E or fabs(x2-x1) < E:
            x = x2
            break

        x1 = x2

x = x1 = ... #valor inicial

x2 = None

E = ... #precisão desejada

if not (fabs(f(x1)) < E):
    metodo_iterativo(E,x1,x2)

p = ... #precisão de casas decimais a serem impressas

print(f'{x:.{p}f} é um valor válido.')