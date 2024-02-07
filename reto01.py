# Solicitar al usuario que ingrese nombres, apellidos, número de teléfono
# y correo electrónico

nombres = input("Por favor, ingresa tu nombre(s): ")
apellidos = input("Por favor, ingresa tu apellido(s): ")
telefono = input("Por favor, ingresa tu número de teléfono: ")
correo_electrónico = input("Por favor, ingresa tu correo electrónico: ")

# Saludar al usuario utilizando los nombres y apellidos ingresados
print("\nHola " + nombres + " " + apellidos + " (" + correo_electrónico + ")")
