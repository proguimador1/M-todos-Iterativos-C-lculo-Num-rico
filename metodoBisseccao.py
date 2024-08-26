from math import log, fabs, floor

def f(x):
    return ... #aqui vai a função

M = None

a = ... #início do intervalo
b = ... #fim do intervalo

x0 = None

E = ... #precisão desejada na forma de 10^(-n), 
        #sendo n natural

MAX_ITERACOES = floor((log(b-a,10)-log(E,10))/log(2,10)) + 1

for k in range(1,MAX_ITERACOES):
    if fabs(b-a) < E:
        break

    M = f(a)

    x0 = (a+b)/2

    if M*x0 > 0:
        a = x0
    else:
        b = x0

p = -1 * log(E,10)

print(f'Qualquer x do intervalo [{a:.{p}f},{b:.{p}f}] é válido.')