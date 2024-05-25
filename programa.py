import json

Suma = 0
ucs = 0

with open("The-Boys-1.json", "r") as Cedula:
    data_cedula = json.load(Cedula)

with open("The-Dogs-2.json", "r") as Nombre:
    data_nombre = json.load(Nombre)

with open("The-Dragons-3.json", "r") as Codigo:
    data_codigo = json.load(Codigo)


def nombre_del_alumno(Valor):
    for item in data_nombre:
        if item["dni"] == Valor:
            print(f"Encontrado: {Valor}")
            return item["nombre"] + " " + item["apellido"]


def calculo(item):
    for row in data_codigo:
        global Suma
        global ucs
        if row["Codigo"] == item["Codigo"]:
            Suma += item["nota"] * row["UC"]
            ucs += row["UC"]


def mostrar_menu():
    print("1. Nombre del alumno")
    print("2. Promedio ponderado")
    print("3. Agregar nota")
    print("4. Borrar nota")
    print("5. Salir")


def menu_opcion(opcion):
    if opcion == '1':
        buscar = input("Ingrese la cedula para buscar: ")
        vnombre = nombre_del_alumno(buscar)
        print(f"El nombre del alumno es: {vnombre}")

    elif opcion == '2':
        buscar = input("Ingrese cedula: ")
        for item in data_cedula:
            if item["dni"] == buscar:
                calculo(item)
                prom = Suma / ucs
                vnombre = nombre_del_alumno(buscar)
                print(f"El promedio ponderado de {vnombre} es: {prom:.2f}")
                
    elif opcion == '3':
        cedula = input("Ingrese cedula del alumno: ")
        codigo = input("Ingrese el código de la materia: ")
        nota = float(input("Ingrese la nota: "))
        
        nueva_nota = {
            "dni": cedula,
            "Codigo": codigo,
            "nota": nota
        }
        
        data_cedula.append(nueva_nota)
        
        with open("The-Boys-1.json", "w") as file:
            json.dump(data_cedula, file, indent=4)
            
        print("Nota agregada exitosamente.")

    elif opcion == '4':
        cedula = input("Ingrese cedula del alumno: ")
        codigo = input("Ingrese el código de la materia a borrar: ")
        
        for i, item in enumerate(data_cedula):
            if item["dni"] == cedula and item["Codigo"] == codigo:
                del data_cedula[i]
                with open("The-Boys-1.json", "w") as file:
                    json.dump(data_cedula, file, indent=4)
                print("Nota borrada exitosamente.")
                break
        else:
            print("No se encontró la nota a borrar.")

    elif opcion == '5':
        print("Cerrando Programa...")

    else:
        print("Error de Opcion. Por favor, elija una opción válida.")


mostrar_menu()
opcion = input("Ingrese la opcion que desea utilizar: ")
menu_opcion(opcion)
