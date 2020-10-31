"""

IF NUMERO > 0:
    NUMERO = NUMERO + 1
ELSE:
    NUMERO = NUMERO - 1



IF CONDICION1:
    ACCION A REALIZAR
ELSE:
    ACCION A REALIZAR 2


"""

num = int(input('Ingrese un numero : \n'))

if num%2 == 0:
    print('El numero es par')
elif num>80:
    print('El numero es impar mayor que 80')
else:
    print('El numero es impar')