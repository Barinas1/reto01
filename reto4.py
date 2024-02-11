# Función para validar la longitud de una cadena
def validar_longitud(cadena, min_longitud, max_longitud):
    return min_longitud <= len(cadena) <= max_longitud


# Función para validar un número de teléfono
def validar_telefono(telefono):
    return len(telefono) == 10 and telefono.isdigit()


# Función para validar un correo electrónico
def validar_correo(correo):
    return '@' in correo and '.' in correo and 5 <= len(correo) <= 50


# Función para registrar un nuevo usuario
def registrar_usuario():
    nombres = input("Por favor, ingresa tu nombre(s): ")
    apellidos = input("Por favor, ingresa tu apellido(s): ")
    telefono = input("Por favor, ingresa tu número de teléfono: ")
    correo_electronico = input("Por favor, ingresa tu correo electrónico: ")

    # Validar la entrada del usuario
    if (validar_longitud(nombres, 5, 50) and
            validar_longitud(apellidos, 5, 50) and
            validar_telefono(telefono) and
            validar_correo(correo_electronico)):
        # Generar un identificador único
        identificador = len(usuarios) + 1
        usuarios[identificador] = {
            'nombres': nombres,
            'apellidos': apellidos,
            'telefono': telefono,
            'correo_electronico': correo_electronico
        }
        print("\nRegistro exitoso. ID del usuario:", identificador)
        print("Hola " + nombres + " " + apellidos + " (" + correo_electronico + ")")
    else:
        print("Error: Por favor, asegúrate de que los datos ingresados sean válidos.")


# Función para listar los IDs de todos los usuarios
def listar_usuarios():
    print("\nLista de IDs de usuarios registrados:")
    for usuario_id in usuarios:
        print(usuario_id)


# Función para ver la información de un usuario por su ID
def ver_usuario():
    usuario_id = int(input("Por favor, ingresa el ID del usuario que deseas ver: "))
    if usuario_id in usuarios:
        usuario = usuarios[usuario_id]
        print("\nInformación del usuario con ID", usuario_id)
        print("Nombres:", usuario['nombres'])
        print("Apellidos:", usuario['apellidos'])
        print("Teléfono:", usuario['telefono'])
        print("Correo electrónico:", usuario['correo_electronico'])
    else:
        print("No se encontró ningún usuario con ese ID.")


# Función para editar la información de un usuario por su ID
def editar_usuario():
    usuario_id = int(input("Por favor, ingresa el ID del usuario que deseas editar: "))
    if usuario_id in usuarios:
        print("\nEditando información del usuario con ID", usuario_id)
        usuario = usuarios[usuario_id]
        nombres = input("Por favor, ingresa tu nuevo nombre(s) (anterior: {}): ".format(usuario['nombres']))
        apellidos = input("Por favor, ingresa tu nuevo apellido(s) (anterior: {}): ".format(usuario['apellidos']))
        telefono = input("Por favor, ingresa tu nuevo número de teléfono (anterior: {}): ".format(usuario['telefono']))
        correo_electronico = input("Por favor, ingresa tu nuevo correo electrónico (anterior: {}): ".format(usuario['correo_electronico']))

        # Validar la entrada del usuario
        if (validar_longitud(nombres, 5, 50) and
                validar_longitud(apellidos, 5, 50) and
                validar_telefono(telefono) and
                validar_correo(correo_electronico)):
            usuarios[usuario_id] = {
                'nombres': nombres,
                'apellidos': apellidos,
                'telefono': telefono,
                'correo_electronico': correo_electronico
            }
            print("La información del usuario con ID {} ha sido actualizada.".format(usuario_id))
        else:
            print("Error: Por favor, asegúrate de que los datos ingresados sean válidos.")
    else:
        print("No se encontró ningún usuario con ese ID.")


# Inicializar diccionario para almacenar usuarios
usuarios = {}

# Menú principal
while True:
    print("\nMenú:")
    print("A.-) Registrar nuevos usuarios")
    print("B.-) Listar usuarios")
    print("C.-) Ver información de un usuario")
    print("D.-) Editar información de un usuario")
    print("E.-) Finalizar programa")

    opcion = input("Por favor, selecciona una opción (A/B/C/D/E): ").upper()

    if opcion == 'A':
        registrar_usuario()
    elif opcion == 'B':
        listar_usuarios()
    elif opcion == 'C':
        ver_usuario()
    elif opcion == 'D':
        editar_usuario()
    elif opcion == 'E':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")