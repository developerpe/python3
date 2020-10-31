diccionario = {
        1:"Hola",
        2:"Como estas",
        3:"Bien"
    }
resultado = diccionario.get(0,"No existe un valor asociado a esta clave o no existe esta clave")
diccionario[4] = "Que bueno"


for clave,valor in diccionario.items():
    pass
    #print("{0} --> {1} ".format(clave,valor))
    

for clave in diccionario:
    resultado = diccionario.get(clave,"No existe un valor asociado a esta clave o no existe esta clave")
    #print(resultado)

for clave in diccionario.keys():
    print(clave)