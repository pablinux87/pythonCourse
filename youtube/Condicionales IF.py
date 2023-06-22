
## EJERCICIO 1
"""
a=float(input("Asignar un valor de a: "))
b=float(input("Asignar un valor de b: "))
c=float(input("Asignar un valor de c: "))


resultado=(a**3 * (b**2-(2*a*c)))/(2*b)

print(f"El resultado es {resultado}")
"""

## EJERCICIO 2
"""
a=float(input("Asignar un valor de a: "))
b=float(input("Asignar un valor de b: "))
resultado=((3+5*8)<3 and ((-6/3*4)+2<2)) or (a>b)

print(f"El resultado es: {resultado}")
"""

## EJERCICIO 3
"""
a=float(input("ingrese el valor de a: "))
b=float(input("ingrese el valor de b: "))
c=a

print(f"Los valores ingresados son a-> {a} y b-> {b}")
print(f"Los valores intercambiados son a-> {b} y b-> {c}")


## OTRA FORMA EXCELENTE QUE PERMITE PYTHON!!!!
a, b = b, a

print(f"Los valores cambiados realmente en la variable son: a-> {a} y b-> {b}")

print("FORMA DE CAMI:")

a=float(input("ingrese el valor de a: "))
b=float(input("ingrese el valor de b: "))

print(f"Los valores ingresados son a-> {a} y b-> {b}")
c = a
a = b 
b = c


print(f"Los valores cambiados realmente en la variable son: a-> {a} y b-> {b}") 
"""

## EJERCICIO 4
"""
import math


r = float(input("Ingrese el radio de la circunferencia: "))

area = math.pi * r**2
long = 2 * math.pi * r

print(f"Con el radio {r}, el area de la circunferencia es {area:.2f} y la longitud es {long:.2f}")
"""

## EJERCICIO 5
"""
precio = float(input("Ingrese el valor del producto: "))
precio *= 0.85

print(f"El precio final con descuento es: {precio:.2f}")
"""

## EJERCICIO CONDICIONALES

## NUMERO MAYOR

"""

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))

if num3<num1>num2:
    print(f"El numero 1 -> {num1} es el mayor")
elif num3<num2>num1:
    print(f"El numero 2 -> {num2} es el mayor")
elif num1<num3>num2:
    print(f"El numero 3 -> {num3} es el mayor")
else:
    print("Alguno de los numeros eran iguales")

"""

## VOCALES
"""
letra = str(input("Ingrese una letra: ")).lower()

if not(letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u"):
    print(f"Excelente, la letra {letra} no es una vocal!!")
else:
    print(f"La letra {letra} es una vocal...")

"""

## CALCULADORA

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))
operador = str(input("Ingrese el operador de la operacion, respetando la primer linea de la misma, S-s para suma, etc...")).lower()

if operador=="s":
    resultado = num1+num2
elif operador=="r":
    resultado = num1-num2
elif operador=="m" or operador=="p":
    resultado = num1*num2
elif operador=="d":
    resultado = num1/num2
else:
    resultado="Incorrecto, ya que no se ingreso un operador permitido..."

print(f"El resultado de la operacion es: {resultado:.2f}")

















