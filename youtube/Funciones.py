### EJERCICIO 2

"""
def rectangulo(anc,alt):
    for i in range(alt):
        print("* "*anc)

anc = int(input("Ingrese la anchura del rectangulo: "))
alt = int(input("Ingrese la altura del rectangulo: "))
print()
rectangulo(anc,alt)
print()

"""

### EJERCICIO 3

"""

clientes = [] # Creo un diccionario de clientes...
cliente = {}

def nuevo_cliente(nombre,apellido,dni):
    global clientes,cliente
    err=0
    cliente={"Nombre":nombre,"Apellido":apellido,"DNI":dni}
    if len(clientes)==0:
        clientes.append(cliente)
        return True
    for i in clientes:
        for v in i:
            if i[v]==dni:
                err=1
    if err==1:
        print("El cliente que esta ingreasando ya existe en la base de datos.")
        return False
    else:
        clientes.append(cliente)
        print("Cliente ingresado con exito.")
        return True



def mostrar_clientes():
    for i in clientes:
        for k,v in i.items():
            print(f"{k} : {v}")
        print() 
         

def mostrar_clientes_dni(dni):
    for i in clientes:
        for j in i:
            print(j)
            if i[j]==dni:
                print("entre con el valor ",i[j])
                print(i)
    return True



def eliminar_cliente(dni):
    err=0
    for i in clientes:
        for v in i:
            if i[v]==dni:
                err=1
        if err==1:
            clientes.remove(i)
            print("El Cliente ah sido eliminado con exito.")
    return True




while True:

    print()
    print(f'''\t.: MENU :.
    1. Agregar nuevo cliente.
    2. Mostrar todos los clientes.
    3. Mostrar clientes por DNI.
    4. Eliminar cliente.
    5. Salir.

    ''')

    opcion = int(input("Ingrese su opcion -> "))
    
    if opcion == 1:
        print("\nIngresando nuevo Cliente.")
        print()
        nombre=input("Ingrese el nombre: ")
        apellido=input("Ingrese el apellido: ")
        dni=int(input("Ingrese el dni: "))
        print()
        nuevo_cliente(nombre,apellido,dni)
    elif opcion == 2:
        mostrar_clientes()
    elif opcion == 3:
        print()
        dni=int(input("\nIngresando el DNI que desea seleccionar: "))
        print()
        mostrar_clientes_dni(dni)
    elif opcion == 4:
        dni=int(input("\nIngresando el DNI que desea eliminar: "))
        eliminar_cliente(dni)
    elif opcion == 5:
        print("Muchas gracias por utilizar el sistema!!")
        break
    else:
        print("Opcion incorrecta.")
        
"""

### EJERCICIO FUNCION RECURSIVA

"""

def factorial(num):
    if num>0:
        resultado = num * factorial(num - 1)
    else:
        resultado = 1
    return resultado    
        
n = int(input("Ingrese el numero para aplicar factorial-> "))


print(f"El resultado de {n}! es -> {factorial(n)}")

"""

def sumarDigitos(num):
    if num==0:
        resultado=0
    else:
        resultado = sumarDigitos(int(num/10)) + (num%10)
        
    return resultado

valor = sumarDigitos(1010)
print(valor)