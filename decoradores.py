def funcion_decoradora(funcion):
    def nuevas_funcionalidades(*args,**kwargs):
        print("Antes de multiplicar")
        resultado = funcion(*args,**kwargs)
        print(resultado)
        print("Despues de multiplicar")
    
    return nuevas_funcionalidades


@funcion_decoradora
def multiplicar(num,num2):
    return num * num2

multiplicar(90,8)