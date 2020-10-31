def multiplicar(inicio,*args,**kwargs):
    print(kwargs)
    for i in args:
        inicio *= i
    return inicio

print(multiplicar(20,12,4,56,5,3,resultante = 200,cancelacion = 50))
