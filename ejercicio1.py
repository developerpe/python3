"""

Averiguar si un numero ingresado por consola es par o impar y ademas averiguar si es negativo o positivo

"""


print('\t\t\t\tEJERCICIO 1')
numero = int(input('Ingrese un número:\n'))

if numero%2 == 0:
    if numero > 0:
        print('El número ingresado es un número par y además es positivo')
    else:
        print('El número ingresado es un número par y además es negativo')
else:
    print('El número ingresado es un número impar')
    if numero > 0:
        print('El número ingresado es un número impar y además es positivo')
    else:
        print('El número ingresado es un número impar y además es negativo')