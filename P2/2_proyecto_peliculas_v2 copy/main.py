
'''
Crear un proyecto que permita gestionar (administrar) peliculas
Colocar un menu de opciones para agregar, borrar, modificar, mostrar, buscar, limpiar una lista de peliculas

notas: 
1.- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar dict para almacenar los atributos (nombre,categoria,clasificacion,genero,idioma) de peliculas
'''

import peliculas

opcion=True

#por si el usuario ingresa algo que no da, pues que el programa no se salga, por eso un while, siempre regresa a su inicio
while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t .:::GESTION DE PELICULAS:::.\n\t 1.-Crear \n\t2.- Borrar\n\t3.- Mostrar\n\t4.-Agregar caracteristica\n\t5.-Modificar Caracteristica\n\t6.-Borrar Caracteristica\n\t7.- Salir")
    opcion=input("\n\t\t Elige una opción: ").upper()

    match opcion: #puede seer string o int
        case "1":
            peliculas.crearPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            #peliculas.esperarTecla()
            
        case "3":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.agregarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.modificarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "6":
            peliculas.borrarCaracteristicaPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion=False
            peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecución del Sistema...Gracias")
        case _:
            opcion=True
            peliculas.esperarTecla()
            print("\n\tOpción Inválida vuelva a intentarlo")
                                          

