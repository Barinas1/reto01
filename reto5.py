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
def new_user():
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


# Función para mostrar la información de un usuario por su ID
def show_user(user_id):
    if user_id in usuarios:
        usuario = usuarios[user_id]
        print("\nInformación del usuario con ID", user_id)
        print("Nombres:", usuario['nombres'])
        print("Apellidos:", usuario['apellidos'])
        print("Teléfono:", usuario['telefono'])
        print("Correo electrónico:", usuario['correo_electronico'])
    else:
        print("No se encontró ningún usuario con ese ID.")


# Función para editar la información de un usuario por su ID
def edit_user(user_id):
    if user_id in usuarios:
        print("\nEditando información del usuario con ID", user_id)
        usuario = usuarios[user_id]
        nombres = input("Por favor, ingresa tu nuevo nombre(s) (anterior: {}): ".format(usuario['nombres']))
        apellidos = input("Por favor, ingresa tu nuevo apellido(s) (anterior: {}): ".format(usuario['apellidos']))
        telefono = input("Por favor, ingresa tu nuevo número de teléfono (anterior: {}): ".format(usuario['telefono']))
        correo_electronico = input("Por favor, ingresa tu nuevo correo electrónico (anterior: {}): ".format(usuario['correo_electronico']))

        # Validar la entrada del usuario
        if (validar_longitud(nombres, 5, 50) and
                validar_longitud(apellidos, 5, 50) and
                validar_telefono(telefono) and
                validar_correo(correo_electronico)):
            usuarios[user_id] = {
                'nombres': nombres,
                'apellidos': apellidos,
                'telefono': telefono,
                'correo_electronico': correo_electronico
            }
            print("La información del usuario con ID {} ha sido actualizada.".format(user_id))
        else:
            print("Error: Por favor, asegúrate de que los datos ingresados sean válidos.")
    else:
        print("No se encontró ningún usuario con ese ID.")


# Función para eliminar un usuario por su ID
def delete_user(user_id):
    if user_id in usuarios:
        del usuarios[user_id]
        print("El usuario con ID {} ha sido eliminado.".format(user_id))
    else:
        print("No se encontró ningún usuario con ese ID.")


# Función para listar todos los usuarios
def list_users():
    print("\nLista de usuarios:")
    for user_id, usuario in usuarios.items():
        print("ID:", user_id)
        print("Nombres:", usuario['nombres'])
        print("Apellidos:", usuario['apellidos'])
        print("Teléfono:", usuario['telefono'])
        print("Correo electrónico:", usuario['correo_electronico'])
        print()


# Inicializar diccionario para almacenar usuarios
usuarios = {}

# Diccionario de funciones
acciones = {
    'A': new_user,
    'B': list_users,
    'C': show_user,
    'D': edit_user,
    'E': delete_user
}

# Menú principal
while True:
    print("\nMenú:")
    print("A.-) Registrar nuevos usuarios")
    print("B.-) Listar usuarios")
    print("C.-) Ver información de un usuario")
    print("D.-) Editar información de un usuario")
    print("E.-) Eliminar usuario")
    print("F.-) Finalizar programa")

    opcion = input("Por favor, selecciona una opción (A/B/C/D/E/F): ").upper()

    if opcion == 'A':
        new_user()
    elif opcion == 'B':
        list_users()
    elif opcion == 'C':
        try:
            user_id = int(input("Por favor, ingresa el ID del usuario: "))
            show_user(user_id)
        except ValueError:
            print("Error: El ID del usuario debe ser un número entero.")
    elif opcion == 'D':
        try:
            user_id = int(input("Por favor, ingresa el ID del usuario: "))
            edit_user(user_id)
        except ValueError:
            print("Error: El ID del usuario debe ser un número entero.")
    elif opcion == 'E':
        try:
            user_id = int(input("Por favor, ingresa el ID del usuario: "))
            delete_user(user_id)
        except ValueError:
            print("Error: El ID del usuario debe ser un número entero.")
    elif opcion == 'F':
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")