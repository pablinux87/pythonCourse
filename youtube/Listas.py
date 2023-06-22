## LISTA
'''
lista = [0,1,2,3,4,5]

lista.append(6)

lista.extend([7,8,9,1,2,3,4])

lista.remove(1)

print(f"\n {lista}")
print(len(lista))
'''

## TUPLA
'''
tupla=(1,2,3,4)

tupla.count(1)

print(type("Pablo"))

print(tupla)

'''

## CONJUNTOS
'''
conjunto = set()
conjunto = {1,2,3}

conjunto.add(5)

print(conjunto)


a={1,2,3}
b={3,4,5}

union=a|b
interseccion=a&b
diferencia=a-b
diferencia_simetrica=a^b

print(union)
print(interseccion)
print(diferencia)
print(diferencia_simetrica)
'''

## DICCIONARIOS

'''
diccionario = {"azul":"blue","rojo":"red","verde":"green"}

diccionario["amarillo"]="yellow"

del(diccionario["verde"])

print(diccionario)

diccionario2 = {"Pablo":{"edad":35,"estatura":1.78}, "Camila":[27,1.59], "Juan":[22,1.85]}

print(diccionario2)

'''

## EJERCICIO 1
'''
lista = [1,2,3,4,5,6,1,2,3]
lista=list(set(lista))
##lista2 = set(lista)
##lista = list(lista2)
print(lista)
'''

##EJERCICIO 2
'''
lista1 = ["Pablo","Cami","Lucas","Juan","Pedro"]
lista2 = ["Orne","Liber","Juan","Lucas","Jaqui"]

print(f"La lista 1 tiene los siguientes nombres: \n{lista1}")
print(f"La lista 2 tiene los siguientes nombres: \n{lista2}")

lista1=set(lista1)
lista2=set(lista2)


print("\nLas palabras que aparecen las dos listas...")
print("\t",list(lista1|lista2))

print("\nLas palabras que aparecen en la primera y no en la segunda...")
print("\t",list(lista1-lista2))

print("\nLas palabras que aparecen en la segunda y no en la primera...")
print("\t",list(lista2-lista1))

print("\nLas palabras que aparecen repetidos...")
print("\t",list(lista2&lista1))

'''
## EJERCICIO 3

personajes = []

p = {"nombre":"Aragon","clase":"Guerrero","raza":"Dunadan dek Norte"}

personajes.append(p)

p = {"nombre":"Gandalf","clase":"Mago","raza":"Istal"}

personajes.append(p)

p = {"nombre":"Legolas","clase":"Arquero","raza":"Elfo Sindar"}

personajes.append(p)

print(personajes)
pr