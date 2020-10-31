lista = [1,2,3,4,5,6,7,8,9,10,2,2,2,2,2,2,2]
lista2 = ["Developer.pe","Hola"]
#AGREGAR VALORES A LISTAS
lista.append(15)
lista.insert(2,18)
print(lista)
#ELIMINAR VALORES
#valor = lista.remove(2)
#valor = lista.pop(2)

cantidad = lista.count(2)
nueva_lista = lista.copy()
lista.append("Nuevo valor")
lista2.append(nueva_lista)
print(lista2)