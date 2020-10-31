def cuenta_atras(numero):
    numero -= 1
    if numero > 0:
        print(numero)
        cuenta_atras(numero)
    else:
        print("Holaaaaaaaa!")
    print(f"Orden de liberacion {numero}")

#cuenta_atras(10)

def calcular_factorial(numero):
    if numero > 1: numero *= calcular_factorial(numero - 1)
    return numero

print(calcular_factorial(5))