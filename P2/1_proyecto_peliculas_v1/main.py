
'''
Crear un proyecto que permita gestionar (administrar) peliculas
Colocar un menu de opciones para agregar, borrar, modificar, mostrar, buscar, limpiar una lista de peliculas

notas: 
1.- Utilizar funciones y mandar llamar desde otro archivo (modulo)
2.- Utilizar listas para almacenar los nombres de peliculas
'''

import peliculas

opcion=True

#por si el usuario ingresa algo que no da, pues que el programa no se salga, por eso un while, siempre regresa a su inicio
while opcion:
    peliculas.borrarPantalla()
    print("\n\t\t\t .:::GESTION DE PELICULAS:::.\n\t 1.-Agregar \n\t2.- Borrar\n\t3.- Modificar\n\t4.-Mostrar\n\t5.-Buscar\n\t6.-Limpiar\n\t7.- Salir")
    opcion=input("\n\t\t Elige una opción: ").upper()

    match opcion: #puede seer string o int
        case "1":
            peliculas.agregarPeliculas()
            peliculas.esperarTecla()
        case "2":
            peliculas.borrarPeliculas()
            #peliculas.esperarTecla()
            
        case "3":
            peliculas.modificarPeliculas()
            peliculas.esperarTecla()
        case "4":
            peliculas.mostrarPeliculas()
            peliculas.esperarTecla()
        case "5":
            peliculas.buscarPeliculas()
            peliculas.esperarTecla()
        case "6":
            peliculas.limpiarPeliculas()
            peliculas.esperarTecla()
        case "7":
            opcion=False
            peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecución del Sistema...Gracias")
        case _:
            opcion=True
            peliculas.esperarTecla()
            print("\n\tOpción Inválida vuelva a intentarlo")
                                          

            #limpiar que se vacie la lista, que pregunte quieres limpiar la lista, si permite vaciar y la no pues no hace nada
            #mostrar muestran peliculas una por una, listado de las peliculas, que empiece a ver las peliculas del 1 al 4