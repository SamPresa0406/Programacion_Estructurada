
import agenda

def main():
    agenda_contactos={}
    opcion=True

    while opcion:
        agenda.borrarPantalla()
        opcion=agenda.menu_principal()

        if opcion=="1":
            agenda.agregar_contacto(agenda_contactos)
            agenda.esperarTecla()
            
        elif opcion=="2":
          agenda.mostrar_contactos(agenda_contactos)
          agenda.esperarTecla()   
          
        elif opcion=="3":
          agenda.buscar_contacto(agenda_contactos)
          agenda.esperarTecla()
        elif opcion=="4":
          agenda.borrar_contacto(agenda_contactos)
          agenda.esperarTecla()
        elif opcion=="5":
           agenda.modificar_contacto(agenda_contactos)
           agenda.esperarTecla()
        elif opcion=="6":
          agenda.borrarPantalla()
          print(" Programa finalizado.")
          opcion=False   
        else:
           opcion=True
           print(" Opcion no válida. Intenta de nuevo.")

if __name__=="__main__":
   main()                 
