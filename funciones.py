"""

    def nombreFuncion(párametro, parametros):
        INSTRUCCIONES QUE SE DESEAN EJECUTAR
        return valor

"""

def sumar(numero,numero2):
    suma = numero + numero2
    return suma
    

for i in range(2):    
    numero = int(input('Ingrese primer número para la suma: '))
    numero2 = int(input('Ingrese segundo número para la suma: '))
    print('El resultado de sumar los números ingresados es: '+str(sumar(numero,numero2)))