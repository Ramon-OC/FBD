import csv

def leer_archivo():
    try:
        with open('empleados.csv', 'r') as archivo:
            reader = csv.DictReader(archivo, delimiter=';')
            for row in reader:
                print(f"id: {row['id']}, nombre: {row['nombre']}, direccion: {row['direccion']}, correos: {row['correos']}, telefonos: {row['telefonos']}, fechaNacimiento: {row['fechaNacimiento']}, cargo: {row['cargo']}, sucursal: {row['sucursal']}")
    except FileNotFoundError:
        print("El archivo no existe.")

def escribir_archivo():
    id = input("Ingrese el id: ")
    nombre = input("Ingrese el nombre: ")
    direccion = input("Ingrese la dirección: ")
    correos = input("Ingrese los correos (separados por comas): ")
    telefonos = input("Ingrese los teléfonos (separados por comas): ")
    fechaNacimiento = input("Ingrese la fecha de nacimiento: ")
    cargo = input("Ingrese el cargo: ")
    sucursal = input("Ingrese la sucursal: ")
    with open('empleados.csv', 'a', newline='') as archivo:
        writer = csv.writer(archivo, delimiter=';')
        writer.writerow([id, nombre, direccion, correos, telefonos, fechaNacimiento, cargo, sucursal])
    print("Se ha agregado el registro correctamente.")

def editar_archivo():
    pass

while True:
    print("\nMenú principal")
    print("1. Leer archivo")
    print("2. Escribir archivo")
    print("3. Editar archivo")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        leer_archivo()
    elif opcion == "2":
        escribir_archivo()
    elif opcion == "3":
        editar_archivo()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida.")
