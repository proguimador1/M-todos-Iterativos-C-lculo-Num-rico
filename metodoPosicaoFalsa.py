from math import fabs

def f(x):
    return ... #aqui vai a função

a = ... #menor valor do intervalo
b = ... #mair valor do intervalo

x0 = None

E = 0.00000001

p = ... #precisão de casas decimais a serem impressas

for k in range(1,1000000):
    
    if fabs(b-a) < E:
        print(f'Qualquer valor do intervalo [{a:.{p}f},{b:.{p}f}] é válido.')
        break

    if (fabs(f(a)) < E):
        print(f'{a:.{p}f} é um valor válido.')
        break

    if (fabs(f(b)) < E):
        print(f'{b:.{p}f} é um valor válido.')
        break

    fa, fb = f(a), f(b)

    x0 = (a*fb-b*fa)/(fb-fa)

    if fa*f(x0) > 0:
        a = x0
    else:
        b = x0