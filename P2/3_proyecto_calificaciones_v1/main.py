'''
Menu para calificaciones
'''
import calificaciones

def main():

    datos=[]

    opcion=True
    while opcion:
        calificaciones.borrarPantalla()
        calificaciones.menu_principal()
        

        match opcion: 
            case "1":
                calificaiones.agregar_calificaciones(datos) #envio de argumentos, alla son parametros en calificacio es
                calificaciones.esperarTecla()

            case "2":
                calificaiones.mostrar_calificaciones(datos) 
                calificaciones.esperarTecla()

            case "3":
                calificaiones.calcular_promedios(datos) 
                calificaciones.esperarTecla()

            case "4":
                opcion=False
                calificaciones.borrarPantalla()
                print("\n\t\t\t .:::Saliste del sistema:::.")

            case _:
                opcion=True
                calificaciones.esperarTecla()
                print("\n\t\t\t .:::Terminaste:::.")                      


if __name__=="__main__":
    main()