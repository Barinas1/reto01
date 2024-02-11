def validar_longitud(cadena, min_longitud, max_longitud):
    if len(cadena) < min_longitud or len(cadena) > max_longitud:
        print(f"Error: La longitud debe estar entre {min_longitud} y {max_longitud} caracteres.")
        return False
    return True


def validar_telefono(telefono):
    if len(telefono) != 10 or not telefono.isdigit():
        print("Error: El número de teléfono debe tener 10 dígitos numéricos.")
        return False
    return True


while True:
    try:
        cantidad_registros = int(input("Ingrese cuántos registros nuevos desea crear: "))
        break
    except ValueError:
        print("Error: Debe ingresar un número entero válido.")

registros = []
for _ in range(cantidad_registros):
    print(f"\nRegistro {_ + 1}:")
    while True:
        nombres = input("Por favor, ingresa tu nombre(s): ")
        if not validar_longitud(nombres, 5, 50):
            continue
        apellidos = input("Por favor, ingresa tu apellido(s): ")
        if not validar_longitud(apellidos, 5, 50):
            continue
        telefono = input("Por favor, ingresa tu número de teléfono: ")
        if not validar_telefono(telefono):
            continue
        correo_electronico = input("Por favor, ingresa tu correo electrónico: ")
        if not validar_longitud(correo_electronico, 5, 50):
            continue
        break

    registros.append((nombres, apellidos, telefono, correo_electronico))

# Saludar al usuario utilizando los nombres y apellidos ingresados
for i, registro in enumerate(registros):
    nombres, apellidos, telefono, correo_electronico = registro
    print(f"\nRegistro {i + 1}:")
    print("Nombre(s):", nombres)
    print("Apellido(s):", apellidos)
    print("Número de teléfono:", telefono)
    print("Correo electrónico:", correo_electronico)
