import csv, re, os
from datetime import datetime
from pathlib import Path

salir = True
prod_dict = {}


def leer_archivo_Empleados():
    """
    Imprime todos los registros de empleados en el archivo empleados.csv
    """
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
     """
     Menú de consultas de los empleados: permite ver todos los registros o filtrar por su cargo
     dentro de la tienda, se solicita la ocupación e imprime todos los que tengan esa ocurrencia.
     """
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
    '''
    Filtra por su cargo a los empleados, solicita una opción e imprime a todos los que tengan 
    una ocurrencia en la columna de cargo y corresponda a lo pedido.
    '''
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
    '''
    Se encarga de registrar a un empleado (escribe su linea en el archivo). Se valida que 
    todos los datos por escribir correspondan a lo solicitado.
    '''
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
    '''
    Método que permite modificar uno de los atributos del empleado, verifica que la nueva entrada 
    corresponda al formato esperado y se vuelve a escribir en el archivo.
    '''
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

def genera_id(nombre_archivo): 
    '''
    Se genera un identificador para el registro del nuevo usuario, si no hay empleados registrados, 
    el id será 1. Caso contrario se toma el último registro, se suma 1 al id y se le asigna al nuevo.
    '''
    with open(nombre_archivo, "r") as archivo:
        lector_csv = csv.reader(archivo, delimiter=";")
        filas = list(lector_csv)
        if not filas[1:]:
            return 1
        else:
            ultimo_id = int(filas[-1][0])
            return ultimo_id + 1

def eliminar_empleado():
    '''
    Mediante el identificador del empleado, se puede eliminar su registro del archivo
    '''
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

def correo_registrado(correo_nuevo):
     existe = False
     with open("empleados.csv", "r") as archivo_csv:
        lector_csv = csv.reader(archivo_csv, delimiter=";")    
        filas = []
        for fila in lector_csv:
            filas.append(fila)
        
        for fila in filas:
            if fila[3] == "correos": # Ignora la primera fila (atributos)
                continue 
            if fila[3].find(correo_nuevo)!= -1:
                existe = True  
                print("Hay un correo repetido")
        
        return existe     
 


       
    

# Definición de capturas

def captura_correos():
    '''
    Se solicita el número de correos que se desea registrar, se piden y concatenan por comas. 
    Cada uno se valida mediante una expresión regular.
    '''
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
        while not re.match(email_regex, correo) : 
            print(" - No es un correo valido")
            correo = input("Ingresa el correo numero {}: ".format(i+1))
        while correo_registrado(correo):
            print(" - Ya hay un usuario con ese correo")
            correo = input("Ingresa el correo numero {}: ".format(i+1))
        
        correos.append(correo)
    correo_registro = ", ".join(correos) # Debemos respetar el ; del .csv
    return correo_registro

def captura_telefonos():
    '''
    Se solicita el número de telefonos que se desea registrar, se piden y concatenan por comas. 
    Para que un número sea valido, debe de tener diez digitos.
    '''
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
    '''
    Se solicita una fecha y verifica que sea valida y respete el formato dd/mm/aaaa
    '''
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
    '''
    Se despliega un mení solicitando uno de los posibles cargos para el registro de un empleado.
    '''
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
    '''
    Menú para cada una de las operaciones que se pueden hacer con los empleados.
    '''
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
            menu_productos()
        elif opcion == 4:
            salir = False
            break

def leer_archivo_productos():
    path = Path(__file__).parent / "productos.csv"
    try:
        with path.open('r') as archivo:
            reader = csv.DictReader(archivo, delimiter=',')
            for row in reader:
                k = row["nombre"]+row["sucursal"]
                prod_dict[k] = row
                #for string in row:
                    #print(string+":", {row[string]})
    except FileNotFoundError:
        try:
            with path.open('w') as archivo:
                escribir_archivo_productos()
        except FileNotFoundError:
            print("No se pudo abrir ni crear el archivo productos.csv")

def escribir_archivo_productos():
    prod_attr = ["nombre","precio","cantidad","marca","presentacion","sucursal","stock","refrigeracion","elaboracion","caducidad"]
    path = Path(__file__).parent / "productos.csv"
    if not bool(prod_dict):
        leer_archivo_productos()
    try:
        with path.open('w') as archivo:
            writer = csv.DictWriter(archivo, fieldnames=prod_attr)
            writer.writeheader()
            for k,data in prod_dict.items():
                    writer.writerow(data)
    except FileNotFoundError:
        print(" - El archivo no existe.")
    except:
        print("hubo un problema escribiendo el archivo, sorry")

def agregar_producto():
    if not bool(prod_dict):
        leer_archivo_productos()
    nombre = input("Ingrese el nombre del artículo: ")
    sucursal = validar_numero(1,15,"Ingrese el número de sucursal del producto: ","Verifique el número de sucursal.")
    precio = validar_float(0.01,100000,"Ingrese el precio del producto: ","verifique el precio del articulo.")
    presentacion = input("Ingrese la presentación (lata, caja, bote, etc) del artículo: ")
    cantidad = input("Ingrese la cantidad marcada en el empaque (i.e. 1kg, 1L, pza, etc): ")
    marca = input("Ingrese la marca del artículo: ")
    stock = validar_numero(0,10000,"Ingrese el número productos en inventario: ","Verifique la cantidad en el inventario.")
    refrigeracion = validar_booleano("Ingrese TRUE si el articulo necesita ser refrigerado, en otro caso ingrese FALSE. ","Vuela a intentarlo.")
    elaboracion = validar_fecha("Introduzca fecha de caducidad en formato YYYY-MM-DD: ","Intente de nuevo.")
    caducidad = validar_fecha("Introduzca fecha de caducidad en formato YYYY-MM-DD :","Intente de nuevo.")
    prod_dict[nombre + str(sucursal)] = {"nombre" : nombre,"precio" : precio,"cantidad" : cantidad,"marca" : marca,"presentacion" : presentacion,"sucursal" : sucursal,"stock" : stock,"refrigeracion" : refrigeracion,"elaboracion" : elaboracion,"caducidad":caducidad}

def validar_fecha(mensaje,error):
    while True:
        try:
            fecha = input(mensaje)
            if not re.match("^\d{4}\-(0[1-9]|1[012])\-(0[1-9]|[12][0-9]|3[01])$", fecha):
                raise Exception()
            else:
                return fecha  
        except:
            print(error)

def validar_numero(min,max,mensaje,error):
    while True:
        try:
            i = int(input(mensaje))
            if i >= min and i <= max:
                return i
            else:
                raise Exception()
        except:
            print(error)

def validar_float(min,max,mensaje,error):
    while True:
        try:
            i = float(input(mensaje))
            if i >= min and i <= max:
                return i
            else:
                raise Exception()
        except:
            print(error)

def validar_booleano(mensaje,error):
    while True:
        try:
            val = input(mensaje)
            if val == "TRUE" or val == "FALSE":
                return val
            else:
                raise Exception()
        except:
            print(error)

def menu_productos():
    while True:
        #os.system('clear')
        print("\nMenu Productos - El Gran Abarrotero")
        print("     1. Realizar una consulta")
        print("     2. Registrar a un nuevo producto")
        print("     3. Modificar la informacion de un producto")
        print("     4. Regresar al menu principal")
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            leer_archivo_productos()
            elige_prod = input("Por favor ingrese el nombre del producto que desea consultar: ")
            elige_sucursal = input("Ingrese el número de sucursal: ")
            k = elige_prod+elige_sucursal
            try:
                for y in prod_dict[k]:
                    print(y,':',prod_dict[k][y])
            except KeyError:
                print("No se encuentra el producto solicitado en la sucursal indicada")        
        elif opcion == "2":
            agregar_producto()
            escribir_archivo_productos()
        elif opcion == "3":
            agregar_producto()
            escribir_archivo_productos()
        elif opcion == "4":
            menu_principal()
            break
        else:
            print(" - No es una opcion valida")

        
menu_principal()