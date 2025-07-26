"""
Es un tipo de datos que se utiliza para almacenar datos de diferente tipo de datos pero en lugar de 
tener como las listas indices numericos tiene alfanumericos. Es decir a algo parecido como los objetos

Arreglo asosiativo u Objeto JSON

Es una coleccion de datos ordenada y modificable 
No duplicados

clave-valor
"""
import os
os.system("cls")

paises=["Mexico","España","Brasil","Canada"]#un valor en concreto de una particularidad
#los objetos buena practica es que su nombre sea singular
pais1={"nombre":"Mexico",
        "capital":"CDMX",
        "poblacion":120000000,
        "idioma":"español",
        "status":True,
        }#atributo nombre y valor del atributo Mexico

pais2={"nombre":"Brasil",
        "capital":"Brasilia",
        "poblacion":14000000,
        "idioma":"portugues",
        "status":True,
        }

#objetos describir los valores de una caracteristica
pais3={"nombre":"Canada",
        "capital":"Otawa",
        "poblacion":10000000,
        "idioma":["ingles","frances"],
        "idioma":{"1":"ingles","2":"frances"},
        "status":True,
        }

for i in pais1:
    print(f"{i}={pais1[i]}")



#Agregar un atributo a un objeto
pais1["altitud"]=3000    

for i in pais1:
    print(f"{i}={pais1[i]}")


#Modificar un valor de un item, vbalor, atributo que ya existe
pais1.update({"altitud":2500})  
for i in pais1:
    print(f"{i}={pais1[i]}")

#quitar el ultimo atributo de un objeto
pais1.popitem()
for i in pais1:
    print(f"{i}={pais1[i]}")

#quitar atributo en especifico de un objeto
pais1.pop("status")   
for i in pais1:
    print(f"{i}={pais1[i]}")