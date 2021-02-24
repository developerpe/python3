sumar = lambda numero,suma: suma + numero

def calcular_suma_elementos(suma = 0):
    while True:
        try:
            cantidad_elementos = int(input("Ingrese la cantidad de elementos que desea sumar: "))            
        except ValueError:
            print("Por favor, ingrese un número, no una cadena de texto.")
        except Exception as e:
            print(type(e).__name__)
        else:
            break
    
    for indice in range(cantidad_elementos):
        while True:
            try:
                numero = int(input("Ingrese el número que desea agregar a la suma: "))
                break
            except:
                print("Por favor ingrese un número")
        
        suma = sumar(numero,suma)
    print(f"La suma de los elementos ingresados es: {suma}")

#calcular_suma_elementos()

def dividir():
    while True:
        try:
            numero = int(input("Ingrese un numero: "))
            division = 40/numero
            print(division)
            break
        except ValueError:
            print("-------Ingrese un numero, no una cadena de texto!-----------")
        except ZeroDivisionError:
            print("-------No se puede realizar una division entre 0---------")
        except Exception as e:
            print(type(e).__name__)

dividir()