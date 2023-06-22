"""
lista = []
for i in range(1,51):
    lista.append(i)
    if i == 50:
        print(f"{i}")
        break
    print(f"{i}",end="-")
"""

### EJERCICIO 1

"""
lista=[]
i=1
while i < 51:
    lista.append(i)
    i+=1
for i in lista:
    if i == 50:
        print(f"{i}")
        break
    print(f"{i}",end="-")

"""

### EJERCICIO 2
"""
lista = (list(range(1,11)))
lista2 = []
n = int(input("Ingrese el valor por el cual multiplicara la lista -> "))
for i in lista:
    lista2.append(i*n)

print(lista2)

## OTRA SOLUCION POSIBLE:::

lista = (list(range(1,11)))
n = int(input("Ingrese el valor por el cual multiplicara la lista -> "))

for indice,i in enumerate(lista):
    lista[indice] *= n

print(lista)

"""

### EJERCICIO 3
"""
lista = []
valor = False

while not valor:
    n= int(input("Digite el valor que quiere insertar a la lista, recuerde que con el valor 0 finalizara el programa..."))
    if n == 0:
        valor = True
    else:    
        lista.append(n)

lista.sort()
print(lista)
"""

### EJERCICIO 4
"""
num1=int(input("Ingrese el primer valor del rango: "))
num2=int(input("Ingrese el segundo valor del rango: "))
valor = 0
lista = range(num1,num2+1)

for i in lista: 
    if i%2==0:
        valor += i
        ## print(valor)

print(valor)
"""

### EJERCICIO 5
"""
n = int(input("Ingrese el numero positivo al cual desea realizarle el factorial: "))
i=1
fac=1

while i <= n:
   fac = i*fac
   i+=1

print(f"El factorial de {n} es: {fac}")

"""

### EJERCICIO 6
"""
lista=[]
num=int(input("Ingrese un numero: "))

for i in range(1,11):
    lista.append(i*num)

print(lista)

"""

### EJERCICIO 7
"""
import random

numero = random.randint(0,100)
## print(numero)
intentos = 0

while True:
    val = int(input("Digite un numero entre 0 y 100\n"))
    intentos+=1
    if val == numero:
        break
    elif val > numero:
        print("El numero ingresado es mayor... Intenrte nuevamente!!")
    else:
        print("El numero ingresado es menor... Intenrte nuevamente!!")
        
print(f"Excelente el numero correcto era {val} y lo conseguiste en el intento numero -> {intentos}")

"""

### EJERCICIO 8
"""
saldo = 1000

while True:

    print("\t.:MENU:.")
    print("1. Ingresar dinero a la cuenta")
    print("2. Retirar dinero de la cuenta")
    print("3. Mostrar dinero disponible")
    print("4. Salir")
    opcion = int(input("Digite una opcion de menu: "))

    print()

    if opcion==1: 
        extra = float(input("Cuanti dinero desea ingresar a la cuenta -> "))
        saldo += extra
        print(f"Dinero en la cuenta: {saldo}")
    elif opcion==2:
        retirar = float(input("Cuanto dinero desea retirar de la cuenta -> "))
        if retirar>saldo:
            print(f"No tiene esa cantidad de dinero")
        else:
            saldo -= retirar
            print(f"Dinero en la cuenta: {saldo}")
    elif opcion==3:
        print(f"Dinero en la cuenta: {saldo}")
    elif opcion==4:
        print(f"Gracias por utilizar su cajero automatico")
        break
    else:
        print("Error, se equivoco de opcion de menu")
        
"""

### EJERCICIO 9
"""
frase = input("Ingrese una frase -> ")
frase2 = ""
for i in frase:
    if i.isspace():
        continue
    frase2+=i
    
print(str(frase2))
print(len(frase2))
"""

###EJERCICIO 10
"""
cadena = input("Ingrese una cadena de caracteres: ")
lista = []

for i in cadena:
    if i not in lista:
        lista.append(i)

print(lista)
"""

### EJERCICIO 11
"""
        """
        
    