import csv, re, os
from datetime import datetime

salir = True

def leer_archivo_Empleados(): # Podriamos hacer un lector y escritor general para los tres .cvs, pero está de hueva xD
    try:
        with open('empleados.csv', 'r') as archivo:
            reader = csv.DictReader(archivo, delimiter=';')
            for row in reader:
                print(f"Id: {row['id']}, Nombre: {row['nombre']}, Direccion: {row['direccion']}, Correos: {row['correos']}, Telefonos: {row['telefonos']}, Fecha de Nacimiento: {row['fechaNacimiento']}, Cargo: {row['cargo']}, Sucursal: {row['sucursal']}")
    except FileNotFoundError:
        print(" - El archivo no existe.")

def escribir_archivo_Empleados():
    id = genera_id("empleados.csv")  
    nombre = input("Escriba el nombre del empleado: ")
    direccion = input("Escriba su direccion: ")
    correos = captura_correos()
    telefonos = captura_telefonos()
    fechaNacimiento = captura_fecha()
    cargo = captura_cargo()

    sucursal = input("Ingrese la sucursal: ") # Comprobar que el ID de la sucursal se correcto.
    
    with open('empleados.csv', 'a', newline='') as archivo:
        writer = csv.writer(archivo, delimiter=';')
        writer.writerow([id, nombre, direccion, correos, telefonos, fechaNacimiento, cargo, sucursal])
    print("Se ha registrado a "+nombre+" correctamente!\nSu ID es: "+str(id))

def editar_archivo():  
    id_buscar = input("Ingrese el ID del empleado que desea editar: ")
    encontrado = False
    
    with open("empleados.csv", "r") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=";")
        
        filas = []
        for fila in lector_csv:
            filas.append(fila)
        
        for fila in filas:
            if fila[0] == "id":
                continue 
            if fila[0] == id_buscar:
                encontrado = True
                print("   Información del empleado:")
                print(" - Id: ", fila[0])
                print(" - Nombre: ", fila[1])
                print(" - Direccion: ", fila[2])
                print(" - Correos: ", fila[3])
                print(" - Telefonos: ", fila[4])
                print(" - Fecha de nacimiento: ", fila[5])
                print(" - Cargo: ", fila[6])
                print(" - Sucursal donde labora: ", fila[7])
                    
                print("\n¿Que informacion deseas modificar?")
                print("     1. Nombre")
                print("     2. Direccion")
                print("     3. Correos")
                print("     4. Telefonos")
                print("     5. Fecha de Nacimiento")
                print("     6. Cargo")
                print("     7. Sucursal")
                opcion = input("Seleccione una opcion: ")

                if opcion == "1":
                    fila[1] = input("Ingrese el nuevo nombre: ")
                elif opcion == "2":
                    fila[2] = input("Ingrese la nueva direccion: ")
                elif opcion == "3":
                    fila[3] = captura_correos()
                elif opcion == "4":
                    fila[4] = captura_telefonos()
                if opcion == "5":
                    fila[5] = captura_fecha()
                elif opcion == "6":
                    fila[6] = captura_cargo()
                elif opcion == "7":
                    fila[7] = input("Ingrese la nueva sucursal: ")
                
        if encontrado:
            with open("empleados.csv", "w", newline="") as archivo_csv:
                escritor_csv = csv.writer(archivo_csv, delimiter=";")
                escritor_csv.writerows(filas)
                print("La informacion del empleado ha sido actualizada correctamente")
        else:
            print("No se ha encontrado ningun empleado con ese ID.")


def genera_id(nombre_archivo): # Creo que se puede usar para todos mientras su primer atributo sea ''id''
    with open(nombre_archivo, "r") as archivo:
        lector_csv = csv.reader(archivo, delimiter=";")
        filas = list(lector_csv)
        if not filas[1:]:
            return 1
        else:
            ultimo_id = int(filas[-1][0])
            return ultimo_id + 1

# Definición de capturas

def captura_correos():
    email_regex = r"[^@]+@[^@]+\.[^@]+" 
    n = int(input("Ingresa el numero de correos que deseas registrar: "))
    correos = []
    for i in range(n):
        correo = input("Ingresa el correo numero {}: ".format(i+1))
        while not re.match(email_regex, correo): 
            print(" - No es un correo valido")
            correo = input("Ingresa el correo numero {}: ".format(i+1))
        correos.append(correo)
    correo_registro = ", ".join(correos) # Debemos respetar el ; del .csv
    return correo_registro

def captura_telefonos():
    n = int(input("Ingresa el numero de telefonos que deseas registrar: "))
    telefonos = []
    
    for i in range(n):
        telefono = input("Ingresa el telefono numero {}: ".format(i+1))
        while len(telefono) != 10: # Solo verficamos que tenga diez dígitos
            print("- No es un telefono valido")
            telefono = input("Ingresa el teléfono numero {}: ".format(i+1))
        telefonos.append(telefono)
    telefono_registro = ", ".join(telefonos)
    return telefono_registro

def captura_fecha():
    fecha_regex = r"\d{2}/\d{2}/\d{4}" 
    while True:
        fecha = input("Ingresa tu fecha en formato dd/mm/aaaa: ")
        if re.match(fecha_regex, fecha): 
            try:
                fecha_dt = datetime.strptime(fecha, "%d/%m/%Y")
                return fecha_dt.strftime("%d/%m/%Y")
            except ValueError: 
                print("- No es una fecha valida")
        else: 
            print("La fecha no tiene el formato dd/mm/aaaa.")

def captura_cargo():
    opciones = ['Encargado', 'Gerente', 'Cajero']
    while True:
        print(" - Selecciona una opción de cargo:")
        for i, opcion in enumerate(opciones):
            print(f"{i+1}. {opcion}")
        try:
            opcion_elegida = int(input("Opción elegida: "))
            if opcion_elegida not in range(1, len(opciones)+1):
                raise ValueError
            else:
                return opciones[opcion_elegida-1]
        except ValueError:
            print("La opción elegida no es válida. Inténtalo de nuevo.")


# Definición de menús

def menu_empleados():
    while True:
        #os.system('clear')
        print("\nMenu Empleados - El Gran Abarrotero")
        print("     1. Realizar una consulta")
        print("     2. Registrar a un nuevo empleado")
        print("     3. Modificar la informacion de un empleado")
        print("     4. Regresar al menu principal")
        opcion = input("Seleccione una opcion: ")

        if opcion == "1":
            leer_archivo_Empleados()
        elif opcion == "2":
            escribir_archivo_Empleados()
        elif opcion == "3":
            editar_archivo()
        elif opcion == "4":
            menu_principal()
            break
        else:
            print(" - No es una opcion valida")

def menu_principal():
    global salir
    while True and salir:
        #os.system('clear')
        print("\nMenu principal - El Gran Abarrotero")
        print("     1. Empleados")
        print("     2. Sucursales")
        print("     3. Productos")
        print("     4. Salir del programa")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            menu_empleados()
        elif opcion == "2":
            pass
        elif opcion == "3":
            pass
        elif opcion == "4":
            salir = False
            break
        else:
            print(" - No es una opcion valida")

while salir:
    menu_principal()