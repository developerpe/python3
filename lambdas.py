"""
def potencia(numero,exponente):
    return pow(numero, exponente)
"""


# funcion = lambda parametro_1,parametro_2,etc : logica
multiplicar_por_10 = lambda numero: numero * 10
potencia = lambda numero,exponente : pow(multiplicar_por_10(numero),exponente)

print(potencia(10,2))
