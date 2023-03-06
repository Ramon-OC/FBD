import csv, re, os
from datetime import datetime

salir = True

def leer_archivo_Empleados():
    try:
        with open('empleados.csv', 'r') as archivo:
            reader = csv.DictReader(archivo, delimiter=';')
            for row in reader:
                print(f"Id: {row['id']}, Nombre: {row['nombre']}, Direccion: {row['direccion']}, Correos: {row['correos']}, Telefonos: {row['telefonos']}, Fecha de Nacimiento: {row['fechaNacimiento']}, Cargo: {row['cargo']}, Sucursal: {row['sucursal']}")
    except FileNotFoundError:
        print("- El archivo empleados.csv no existe")
    
    input("\nPresione ENTER para continuar")    
    os.system('clear')

def consultas_Empleados():
     while True:
        os.system('clear')
        print("\nConsultas de empleados")
        print("     1. Mostrar todos los empleados registrados")
        print("     2. Filtrar empleados por su cargo")
        print("     3. Volver al menu de empleados")

        while True:
            try:
                opcion = int(input("Seleccione una opcion: "))
                if opcion < 1 or opcion > 3:
                    raise ValueError
                break
            except ValueError:
                print("- No es una opcion valida ")

        if opcion == 1:
            leer_archivo_Empleados()
        elif opcion == 2:
            filtro_cargo()
        elif opcion == 3:
            menu_empleados()
            break

def filtro_cargo():
    encontrado = False
    os.system('clear')
    print("\nQue cargo te gustaria consultar?")
    print("     1. Encargado")
    print("     2. Gerente")
    print("     3. Cajero")
    print("     4. Regresar al menu de empleados")

    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))
            if opcion < 1 or opcion > 4:
                 raise ValueError
            break
        except ValueError:
            print("- No es una opcion valida")

    if opcion == 1:
        cargo_buscar = "Encargado"
    elif opcion == 2:
        cargo_buscar = "Gerente"
    elif opcion == 3:
        cargo_buscar = "Cajero"
    elif opcion == 4:
        menu_empleados()

    with open("empleados.csv", "r") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=";")    
        filas = []
        for fila in lector_csv:
            filas.append(fila)
        
        for fila in filas:
            if fila[6] == "cargo": # Ignora la primera fila (atributos)
                continue 
            if fila[6] == cargo_buscar:
                encontrado = True
                print(" - Id: ", fila[0], ", Nombre: ", fila[1], ", Direccion: ", fila[2], ", Correos: ", fila[3], ", Telefonos: ", fila[4], ", Fecha de nacimiento: ", fila[5], ", Cargo: ", fila[6], ", Sucursal: ", fila[7])                    
        
        if encontrado == False:
            print("\n - No se encontraron empleados registrados con ese cargo")
    
    input("\nPresione ENTER para continuar")    
    os.system('clear')

def escribir_archivo_Empleados():
    os.system('clear')
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
    
    input("\nPresione ENTER para continuar")    
    os.system('clear')

def editar_archivo_empleado():  
    os.system('clear')

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

                while True:
                    try:
                        opcion = int(input("Seleccione una opcion: "))
                        if opcion < 1 or opcion > 7:
                            raise ValueError
                        break
                    except ValueError:
                        print("- No es una opcion valida ")


                if opcion == 1:
                    fila[1] = input("Ingrese el nuevo nombre: ")
                elif opcion == 2:
                    fila[2] = input("Ingrese la nueva direccion: ")
                elif opcion == 3:
                    fila[3] = captura_correos()
                elif opcion == 4:
                    fila[4] = captura_telefonos()
                if opcion == 5:
                    fila[5] = captura_fecha()
                elif opcion == 6:
                    fila[6] = captura_cargo()
                elif opcion == 7:
                    fila[7] = input("Ingrese la nueva sucursal: ")
                
        if encontrado:
            with open("empleados.csv", "w", newline="") as archivo_csv:
                escritor_csv = csv.writer(archivo_csv, delimiter=";")
                escritor_csv.writerows(filas)
                print("La informacion del empleado ha sido actualizada correctamente")
        else:
            print("No se ha encontrado ningun empleado con ese ID.")

    input("\nPresione ENTER para continuar")    
    os.system('clear')

def genera_id(nombre_archivo): # Creo que se puede usar para todos mientras su primer atributo sea ''id''
    with open(nombre_archivo, "r") as archivo:
        lector_csv = csv.reader(archivo, delimiter=";")
        filas = list(lector_csv)
        if not filas[1:]:
            return 1
        else:
            ultimo_id = int(filas[-1][0])
            return ultimo_id + 1

def eliminar_empleado():

    id_empleado = input("Escriba el ID del empleado que busca eliminar: ")
    
    with open("empleados.csv", 'r', newline='') as archivo:
        lector = csv.reader(archivo, delimiter=';')
        
        filas_csv = [fila for fila in lector][1:]
        
    filas_filtradas = []
    
    for fila in filas_csv:
        if fila[0] == id_empleado:
            print("\n El empleado con ID {id_empleado} se encontro")
        else:
            filas_filtradas.append(fila)
    
    if len(filas_filtradas) < len(filas_csv):
        with open("empleados.csv", 'w', newline='') as archivo:
            escritor = csv.writer(archivo, delimiter=';')
            
            escritor.writerow(['id', 'nombre', 'direccion', 'correos', 'telefonos', 'fechaNacimiento', 'cargo', 'sucursal']) # Debe escribir nuevamenete
            
            for fila in filas_filtradas:
                escritor.writerow(fila)
                
        print("Se ha eliminado correctamente al empleado con el ID: {id_empleado}")
    else:
        print("\n El empleado con ID {id_empleado} no se encontro")
    
    input("\nPresione ENTER para continuar")    
    os.system('clear')

# Definición de capturas

def captura_correos():
    email_regex = r"[^@]+@[^@]+\.[^@]+" 
    while True:
        try:
            n = int(input("Ingresa el numero de correos que deseas registrar: "))
            break
        except ValueError:
            print("- No es una opcion valida")

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
    while True:
        try:
            n =  int(input("Ingresa el numero de telefonos que deseas registrar: "))
            break
        except ValueError:
            print("- No es una opcion valida")

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
    estatus_menu_empleados = True
    while estatus_menu_empleados and salir:
        os.system('clear')
        print("\nMenu Empleados - El Gran Abarrotero")
        print("     1. Realizar una consulta")
        print("     2. Registrar a un nuevo empleado")
        print("     3. Modificar la informacion de un empleado")
        print("     4. Eliminar el registro de un empleado")
        print("     5. Regresar al menu principal")

        while True:
            try:
                opcion = int(input("Seleccione una opcion: "))
                if opcion < 1 or opcion > 5:
                    raise ValueError
                break
            except ValueError:
                print("- No es una opcion valida ")

        if opcion == 1:
            consultas_Empleados()
        elif opcion == 2:
            escribir_archivo_Empleados()
        elif opcion == 3:
            editar_archivo_empleado()
        elif opcion == 4:
            eliminar_empleado()
        elif opcion == 5:
            estatus_menu_empleados = False
            menu_principal()
            break
        else:
            print(" - No es una opcion valida")

def menu_principal():
    global salir 
    while salir:
        os.system('clear')
        print("\nMenu principal - El Gran Abarrotero")
        print("     1. Empleados")
        print("     2. Sucursales")
        print("     3. Productos")
        print("     4. Salir del programa")

        while True:
            try:
                opcion = int(input("Seleccione una opcion: "))
                if opcion < 1 or opcion > 4:
                    raise ValueError
                break
            except ValueError:
                print("- No es una opcion validas ")
        if opcion == 1:
            menu_empleados()
        elif opcion == 2:
            pass
        elif opcion == 3:
            pass
        elif opcion == 4:
            salir = False
            break
        
menu_principal()