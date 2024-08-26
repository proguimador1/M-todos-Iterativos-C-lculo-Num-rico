from math import fabs, log

def f(x):
    return x**3

def fi(x):
    return -1*x**2

def metodo_iterativo(E,x1,x2):
    global x
    
    for k in range(1000000000):

        x2 = fi(x1)

        fx2 = f(x2)

        if fabs(fx2) < E or fabs(x2-x1) < E:
            x = x2
            break

        x1 = x2

x = x1 = -0.3

x2 = None

E = 0.0000001

if not (fabs(f(x1)) < E):
    metodo_iterativo(E,x1,x2)

p = -1 * log(E,10)

print(f'{x:.{p}f} é um valor válido.')