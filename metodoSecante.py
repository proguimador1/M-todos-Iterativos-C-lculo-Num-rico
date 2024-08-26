from math import fabs

def f(x):
    
    return ... #aqui vai a função

def metodo_iterativo(E,x1,x2):
    global x
    
    for k in range(100000000):

        x3 = x2 - f(x2)/(f(x2) - f(x1)) * (x2-x1)

        if fabs(f(x3)) < E or fabs(x3-x2) < E:
            x = x3
            break

        x1 = x2
        x2 = x3


x = None

x1 = ... #aproximação à esquerda

x2 = ... #aproximação à direita

E = ... #precisão desejada na forma de 10^(-n), 
        #sendo n natural

condicao1 = fabs(f(x1)) < E

condicao2 = fabs(f(x2)) < E or fabs(x2-x1) < E

if condicao1:
    x = x1

elif condicao2:
    x = x2

else:
    metodo_iterativo(E,x1,x2)

p = ... #precisão de casas decimais a serem impressas

print(f'{x:.{p}f} é um valor válido.')