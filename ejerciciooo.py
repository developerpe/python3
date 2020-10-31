class Sesion():
    def __init__(self, *args, **kwargs):
        # función principal, mas conocida como constructor de la clase
        self.usuarios = {  # definimos diccionario de datos
            'oliver': [
                'yugiho2000',  # contraseña
                13,  # numero de la suerte
                'Piura'  # ciudad de nacimiento
            ],
            'luis': [
                'sandoval',
                31,
                'Lima'
            ]
        }
        self.run() # llamamos al método run que inicia la ejecución
        super(Sesion, self).__init__(*args, **kwargs)

    def validar_numero_suerte_agregado(self): # función que valida el número de la suerte
        try:
            nuevo_numero_de_suerte_validado = int(
                input('Ingrese su número de la suerte: ')) # convertimos a entero el dato ingresado, si es texto repetimos ingreso
            return nuevo_numero_de_suerte_validado
        except ValueError:
            print('DEBE INGRESAR UN NÚMERO!')
            self.validar_numero_suerte_agregado()

    def validar_longitud_password(self):
        nueva_password = input('Ingrese su contraseña(MÍNIMO 6 CARACTERES): ')
        if len(nueva_password) < 6:
            print('DEBE TENER MÍNIMO 6 CARACTERES!') # validamos el tamaño de la contraseña, si es menor a 6 repetimos
            self.validar_longitud_password()
        if len(nueva_password) >= 6:
            return nueva_password

    def agregar_usuario(self):
        try:
            agregar = int(input('¿Desea ser agregado a la lista de usuarios?\n1.- Si\n2.-No\n'))  # convertimos a entero el dato ingresado, si es texto repetimos ingreso

            if agregar == 1:
                datos = [] # lista con nuevos datos a agregar
                nuevo_nombre_usuario = input('Ingrese su nombre de usuario: ') # este es el nombre de usuario que actuará como KEY
                # resto de datos del nuevo usuario
                nueva_password = self.validar_longitud_password()
                nuevo_numero_de_suerte = self.validar_numero_suerte_agregado()
                nueva_ciudad_nacimiento = input(
                    'Ingrese su ciudad de nacimiento: ')
                # agregamos los datos a la lista
                datos.append(nueva_password)
                datos.append(nuevo_numero_de_suerte)
                datos.append(nueva_ciudad_nacimiento)
                
                self.usuarios[nuevo_nombre_usuario] = datos # creamos el nuevo usuario agregando los datos a la lista de usuarios global
                print(f'USUARIO CON NOMBRE {nuevo_nombre_usuario} AGREGADO CORRECTAMENTE!')
                return True

            if agregar == 2:
                return False
        except ValueError:
            print('DEBE INGRESAR UNA OPCIÓN CORRECTA!')
            self.agregar_usuario()

    def buscar_usuario(self, usuario):
        encontrado = False
        for usua in self.usuarios.keys():
            if usuario.replace(' ', '').lower() == usua.replace(' ', '').lower().lower(): # verificamos si existe el usuario, se le quita los espacios y se convierte a minúscula
                return True

    def eliminar_usuario(self, usuario):
        try:
            eliminado = int(
                input('¿Desea ser eliminado de la lista de usuarios?\n1.- Si\n2.-No\n'))  # convertimos a entero el dato ingresado, si es texto repetimos ingreso
            if eliminado == 1:
                del self.usuarios[usuario] # eliminamos el usuario de la lista de usuarios
                print(f'SU USUARIO {usuario} HA SIDO ELIMINADO CORRECTAMENTE!')
                return True
            if eliminado == 2:
                return False
        except ValueError:
            print('DEBE INGRESAR UNA OPCIÓN CORRECTA!')
            self.eliminar_usuario(usuario)

    def actualizar_numero_suerte(self, usuario):
        try:
            actualizar = int(
                input('¿Desea actualizar su número de la suerte?\n1.- Si\n2.-No\n'))  # convertimos a entero el dato ingresado, si es texto repetimos ingreso
            if actualizar == 1:
                try:
                    nuevo_numero_suerte = int(input('Ingrese su nuevo número de la suerte: '))
                    self.usuarios[usuario][1] = nuevo_numero_suerte # cambiamos el número de la suerte del usuario seleccionado
                    print('NÚMERO DE LA SUERTE ACTUALIZADO CORRECTAMENTE!')
                    return True
                except ValueError:
                    self.actualizar_numero_suerte(usuario)
            if actualizar == 2:
                return False
        except ValueError:
            print('DEBE INGRESAR UNA OPCIÓN CORRECTA!')
            self.actualizar_numero_suerte(usuario)

    def run(self):
        nombre_usuario = input('Ingrese el nombre de usuario: ')
        encontrado = self.buscar_usuario(nombre_usuario) # llamamos a la función que buscará al usuario
        if encontrado:
            print(f'Bienvenido {nombre_usuario} !')
            password = input('Ingrese su contraseña: ')
            if self.usuarios[nombre_usuario][0] == password.lower(): # validamos la contraseña ingresada
                print(f'Su número de la suerte es {self.usuarios[nombre_usuario][1]} y su lugar de nacimiento es {self.usuarios[nombre_usuario][2]}.')
                usuario_eliminado = self.eliminar_usuario(nombre_usuario) # preguntamos si desea eliminar sus datos
                if not usuario_eliminado: # si no se ha eliminado
                    numero_suerte_actualizado = self.actualizar_numero_suerte(nombre_usuario) # preguntamos si desea actualizar número suerte
            else:
                print('CONTRASEÑA INVÁLIDA!')
        else:
            print('NO SE HA ENCONTRADO UN USUARIO CON ESOS DATOS!')
            self.agregar_usuario() # preguntamos si desea agregar sus datos


if __name__ == "__main__":
    Sesion()
