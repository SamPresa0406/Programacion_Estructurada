
#Ejemplo 1 crear una lista de numeros e imprimir el contenido

numeros=[4,36,25,85,148]
print(numeros)

lista=""
for i in numeros:
    lista+=f"{i}"

for i in range(0,len(numeros)):
     lista+=f"{numeros[i]}"   #acumulacion de cadenas
print(f"{lista}")    

lista="["
i=0
while i<len(numeros):
     lista+=f"{numeros[i]}"
     i+=1
print(f"{lista}]")     
#Ejemplo 2 crear una lista de palabras y posteriormente buscar la coincidencia de una palabra

palabras=["sam","papel","michis","lomitos","FALSE"]
print("michis" in palabras)

palabra_buscar=input("Dame la palabra a buscar")
if palabra_buscar in palabras:
     print("SI se encontró la palabra")
else:
     print("NO se encontró la palabra")  


for i in palabras:
    if i==palabra_buscar:
        print("SI se encontró la palabra")
    else:
        print("NO se encontró la palabra")      

cuantas=0
encontro=False
posiciones=[]
for i in palabras:
    if i==palabra_buscar:
        encontro=True
        cuantas+=1
        posicion=palabras.index(i)
if encontro:  #aqui encontro es igual a True
    print("SI se encontró la palabra")
else:
    print("NO se encontró la palabra")    


encontro=False
for i in range(0,len(palabras)):
    if palabras[i]==palabra_buscar:
        encontro=True
if encontro:  #aqui encontro es igual a True
    print("SI se encontró la palabra")
else:
    print("NO se encontró la palabra")       


#variable logica es una bandera

#Ejemplo 3 Añadir  elementos a la lista
numeros=[]

opc="si"
while opc=="si":
    numeros.append(float(input("Dame un numero entero o decimal")))
    opc=input("¿Deseas agregar otro numero?").lower
print(numeros)    




print(numeros)

palabras.append("mango")
print(palabras)

#Ejemplo 4 crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
agenda=[["Celeste","618-123-4567"],
        ["Paolo","618-987-6541"],
        ["Saríah","618-546-2310"]]

print(agenda)