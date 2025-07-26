'''
Dict u objeto que permita almacenar los siguientes atributos:
(nombre,categoria,clasificacion,genero,idioma) de peliculas
'''
#pelicula={
    #"nombre":"",
    #"categoria":"",
    #"clasificacion":"",
    #"genero":"",
    #"idioma":""
#}

pelicula={}


def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("\n\t...Oprima cualquier tecla para continuar...") 

def crearPeliculas():
    borrarPantalla()
    print("\n\t.::Agregar películas::.")
    #pelicula.update({"nombre":input("Ingresa el nombre: ").upper().strip()})
    pelicula["nombre"]=input("Ingresa el nombre: ").upper().strip()
    pelicula.update({f"\u2705 categoria":input("Ingresa la categoria: ").upper().strip()})
    pelicula.update({"clasificacion":input("Ingresa la clasificacion: ").upper().strip()})
    pelicula.update({"genero":input("Ingresa el genero: ").upper().strip()})
    pelicula.update({"idioma":input("Ingresa el idioma: ").upper().strip()})
    print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON ÉXITO!:::") 

def mostrarPeliculas():
    borrarPantalla()
    input("\n\t.::Mostrar las características de las películas::.")
    if len(pelicula)>0:
       for i in pelicula:
            print(f"{i} : {pelicula[i]}") #print nombre : lo que hay en la posicion nombre
    else:
        input("\n\t::..No hay películas en el Sistema..::")    

def borrarPeliculas():
    borrarPantalla()
    input("::.Borrar peliculas::.") 
    
    if len(pelicula)>0:
        op=input("¿Desear borrar la película?").upper().strip()
        if op=="SI":
            pelicula.clear()
            print("La operacion se hizo con éxito")
            esperarTecla()
    else:
        print("\n\t::..No hay películas en el Sistema..::")    

def agregarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.::Agregar una característica de Película::.\n")
    atributo=input("Ingresa el nombre de la nueva característica que deseas agregar: ").lower().strip()
    valor_atributo=input("Ingresa el valor de la nueva característica que deseas agregar: ").lower().strip()
    pelicula.update({atributo:valor_atributo})  
    print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON ÉXITO!:::") 

def modificarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.::Modificar una característica de Película::.\n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"{i} : {pelicula[i]}")
            op=input(f"¿Deseas modificar el valor del atributo {i}? (Si/No) ").lower().strip()
            if op=="si":
                pelicula[i]=input(".::Introduce el nuevo valor de la característica: ").lower().strip()
                print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON ÉXITO!:::")
                esperarTecla()
    else:
        print("\n\t::..No hay películas en el Sistema..::")
        


def borrarCaracteristicaPeliculas():
    borrarPantalla()
    print("\n\t.::Borrar una característica de Película::.\n")
    if len(pelicula)>0:
        print("\n\tValores actuales:")
        print(pelicula)
        for i in pelicula:
            op=input("¿Deseas borrar alguna característica? (Si/No)").lower().strip()
            if op=="si":
                borrar=input(".::Ingresa la característica a borrar: ").lower().strip()
                if borrar==pelicula[i]:
                    
                




                #if borrar!=pelicula:
                    #print("Ingrese una de las caracteristicas mostradas")
                #print("\n\t\t :::¡LA OPERACION SE REALIZÓ CON ÉXITO!:::")
            #else:
                #print("")      

    # else:
    #     print("\n\t::..No hay películas en el Sistema..::")     


    # else:
    #     esperarTecla()
    #     borrarPantalla()    

    
