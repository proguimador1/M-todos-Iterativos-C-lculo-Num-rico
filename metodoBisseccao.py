from math import fabs

def f(x):
    return ... #aqui vai a função

M = None

a = ... #início do intervalo
b = ... #fim do intervalo

x0 = None

E = ... #precisão desejada na forma de 10^(-n), 
        #sendo n natural


for k in range(1,10000):
    if fabs(b-a) < E:
        break

    M = f(a)

    x0 = (a+b)/2

    if M*x0 > 0:
        a = x0
    else:
        b = x0

p = ... #precisão de casas decimais a serem impressas

print(f'Qualquer x do intervalo [{a:.{p}f},{b:.{p}f}] é válido.')