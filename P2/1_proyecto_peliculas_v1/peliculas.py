
peliculas=[]

def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t...Oprima cualquier tecla para continuar...") 

def agregarPeliculas():
    borrarPantalla()
    print("\n\t.::Agregar películas::.")
    peliculas.append(input("Ingresa el nombre: ").upper().strip())#strip es pàra espacios investigar capital
    print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON ÉXITO!:::") 

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t.::Mostrar TODAS las películas::.")
    #print(peliculas)
    if len(peliculas)>0:#saca el tamaño de una lista, set y así
        for i in range(0,len(peliculas)):
            print(f"{i+1} : {peliculas[i]}")      
    else:
        print(".::No hay peliculas en el sistema::.")

yes=""
def limpiarPeliculas():
   borrarPantalla()
   print("\n\t.::Limpiar o borrar TODAS las películas::.")
   yes=input("¿Realmente deseas vaciar la lista?").upper().strip()
   if yes=="SI": 
        peliculas.clear() 
        print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON ÉXITO!:::")
        esperarTecla()   
        
   else: 
      borrarPantalla()

    #peliculas.remove(input("Ingresa el nombre de la película a eliminar: "))
     


#Eliminar, borrar, suprimir, un elemento de una lista
#1er forma
#paises.pop(4)   #se utliza con posicion
#print(paises)


#2da forma
#paises.remove("Honduras")
#print(paises)    

def buscarPeliculas():
    borrarPantalla()
    print("\n\t.::Buscar Peliculas::.\n")
    pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
    if not(pelicula_buscar in peliculas):
        print("\n\t.::Esta pelicula a buscar no esta en el sistema::.")
    else:
         encontro=0
         for i in range(0,len(peliculas)):
             if pelicula_buscar==peliculas[i]:
                 print(f"\n\tLa pelicula {pelicula_buscar} se encontró en el casillero {i+1}") #porque sino esta en el cero
                 encontro+=1
         print(f"\n Tenemos {encontro} peliculas con ese titulo")
         print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON ÉXITO!:::")        


def modificarPeliculas():
    borrarPantalla()
    print("\n\t.::Modificar Peliculas::.\n")
    pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
    if not(pelicula_buscar in peliculas):
        print("\n\t.::Esta pelicula a buscar no esta en el sistema::.")
    else:
         encontro=0
         for i in range(0,len(peliculas)):
             if pelicula_buscar==peliculas[i]:
                 resp=input("¿Deseas actualizar la pelicula? Si/No").lower()
                 if resp=="si":
                    peliculas[i]=input("\Introduce el nuevo nombre de la pelicula: ").upper().strip()
                    encontro+=1
                    print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON ÉXITO!:::")
         print(f"\n\t\t :::Se modifico {encontro} peliculas con ese titulo:::")    


def borrarPeliculas():
    borrarPantalla()
    print("\n\t ::.Borrar peliculas.::") 
    pelicula_buscar=input("Ingrese el nombre de la pelicula a buscar: ").upper().strip()
    if not(pelicula_buscar in peliculas):
        print("\n\t.::Esta pelicula a buscar no esta en el sistema::.") 
    else:
        encontro=0
        for i in range(0,len(peliculas)):
            if pelicula_buscar==peliculas[i]:
                op=input("¿deseas quitar o borrar la pelicula del sistema (Si/No)").lower()
                if op=="si":
                    
                    encontro+=1
                    print(f"La pelicula que se borró es: {pelicula_buscar} y estaba en el casillero {encontro}")
                    print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON ÉXITO!:::")
        print(f"\n\t\t :::Se borro {encontro} peliculas con ese titulo:::")
