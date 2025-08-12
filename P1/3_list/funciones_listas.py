
'''
List(Array)
Son colleciones o conjunto de datos/valores bajo un mismo nombre, para acceder a los valores se hace con un indice numerico

Nota: Sus valores si son modificables

La lista es una colección ordenada y modificable. Permite miembros duplicados.

'''


import os
os.system("cls")

#Funciones más comunes en las listas
paises=["Mexico", "España", "Brasil", "Canada"]

numeros=[23,45,8,24]

varios=["hola",3.1416,True]

#Imprimir el contenido de una lista
print(paises)
print(numeros)
print(varios)

#Recorrer la lista
#1er forma      #trabaja con valores
for i in paises:
    print(i)

#2da forma

listas=""
for i in range(0,len(paises)):        #porque sabemos las posiciones, si ponemos print(i), se imprime la posicion, no el valor. TRbaja con posiciones
    print(paises[i])
    #lista+=f"[{paises[i]}]"

#ordenar elementos de una lista
paises.sort()
print(paises)
numeros.sort()
print(numeros)
#varios no se puede porque no se puede comparar varios datos

#darle la vuelte a una lista
paises.reverse()
print(paises)

varios.reverse()        #aqui si se puede porque solo da la vuelta a los valores
print(varios)

#agregar, insertar, Añadir un elemento a una lista
#1er forma
paises.append("Honduras")   #append agrega al final de la lista
print(paises)

#2da forma
paises.insert(1,"Honduras")     #en la posicion que quieras
print(paises)

paises.sort()
print(paises)

#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
paises.pop(4)   #se utliza con posicion
print(paises)


#2da forma
paises.remove("Honduras")
print(paises)

#buscar un elemento dentro de la lista
resp="Brasil" in paises   #TRUE OR FALSE
print(resp)

print("Brasil" in paises )

#contar el numero de veces que aparece un elemento dentro de una lista
print(numeros)
cuantos=numeros.count(23)   #es una funcion que recibe valores y regresa valor, paradigma declarativo, recibe paramentro que es el 23
print(cuantos)

numeros.append(23)
cuantos=numeros.count(23)   #es una funcion que recibe valores y regresa valor, paradigma declarativo, recibe paramentro que es el 23
print(cuantos)

#conocer la posicion o indice en el que se encuentra un elemento de la lista
paises.reverse()
paises.append("Canada")

print(paises)
posicion=paises.index("Canada")   #el valor que quiere buscar se pone, regresa un valor, las funciones van con parentesis 
print(f"El valor de Canada lo encontró en la posición: {posicion}")

#unir el contenido de una lista dentro de otra
print(numeros)
numeros2=[100,200]

#crear a partir de las listas de numeros 1 y 2 un resultante y mostrar el contenido ordenado descendentemente
#os.system("cls")
numeros.extend(numeros2)  #unir, llevarse una cosa a otra cosa, una extensión
print(numeros)

numeros.sort()
print(numeros)

numeros.reverse()
print(numeros)