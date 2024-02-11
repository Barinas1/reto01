# Función para validar la longitud de una cadena
def validar_longitud(cadena, min_longitud, max_longitud):
    return min_longitud <= len(cadena) <= max_longitud


# Función para validar un número de teléfono
def validar_telefono(telefono):
    return len(telefono) == 10 and telefono.isdigit()


# Función para validar un correo electrónico
def validar_correo(correo):
    return '@' in correo and '.' in correo and 5 <= len(correo) <= 50


# Solicitar al usuario la cantidad de registros a crear
while True:
    try:
        cantidad_registros = int(input("¿Cuántos registros nuevos deseas crear?: "))
        if cantidad_registros <= 0:
            print("Por favor, ingresa un número mayor que cero.")
        else:
            break
    except ValueError:
        print("Por favor, ingresa un número válido.")

# Lista para almacenar los identificadores únicos
identificadores = []

# Iterar para solicitar la información de cada registro
for i in range(cantidad_registros):
    print("\nRegistro #" + str(i + 1))
    while True:
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
            identificador = len(identificadores) + 1
            identificadores.append(identificador)

            # Saludar al usuario
            print("\nRegistro exitoso. ID del usuario:", identificador)
            print("Hola " + nombres + " " + apellidos + " (" + correo_electronico + ")")
            break
        else:
            print("Error: Por favor, asegúrate de que los datos ingresados sean válidos.")

# Imprimir los identificadores únicos
print("\nIdentificadores únicos generados:")
print(identificadores)
