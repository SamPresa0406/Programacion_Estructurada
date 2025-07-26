#los sets son inmutables, no permite valores duplicados

import os
os.system("cls")

paises={"México","Brasil","España","Canada"}
print(paises)#cuando lo ejecutas varias veces, el orden cambia, ya que estan desordenados

varios={True, "UTD",33,3.14}
print(varios)

#Funciones u operaciones
paises.add("Mexico")
print(paises)

paises.pop()
print(paises)

paises.remove("Mexico")
print(paises)

#Crear un programa que solicite los email de los alumnos de la UTD almacenar en una lista 
#y posteriormente mostar en pantalla los email sin duplicados

#solucion1
correos={""}
opc="si"
while opc=="si":
    mail=input("Ingresa tu correo de la UTD")
    correos.add(mail)
    opc=input("¿Deseas agregar otro correo?").lower
print(correos) 

#solucion 2
correos=[]
opc="si"
while opc=="si":
    
    correos.append(input("Ingresa tu correo de la UTD"))
    opc=input("¿Deseas agregar otro correo?").lower
    
correos_set=set(correos)#quito los duplicados
correos=list(correos_set)
print(correos)