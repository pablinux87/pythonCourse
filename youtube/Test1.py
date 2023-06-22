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

















