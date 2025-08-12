
def borrarPantalla():
    import os
    os.system("cls")

def esperarTecla():
    input("Oprime tecla")   

def menu_principal():
    print("\n\t\t\t.::: Sistema de Gestión de Agenda de Contactos :::.\n\n\t\t\t\t\t\t1️⃣ Agregar contacto\n\t\t\t\t\t\t2️⃣ Mostrar todos los contactos\n\t\t\t\t\t\t3️⃣ Buscar contacto por nombre\n\t\t\t\t\t\t4️⃣ Borrar contacto\n\t\t\t\t\t\t3️5 Modificar contacto por nombre\n\t\t\t\t\t\t36. SALIR")
    opcion=input("\n\t\t\t 👉 Elige una opción (1-4): ").upper().strip()
    return opcion


def agregar_contacto(agenda):
    borrarPantalla()
    print("Agregar contactos")
    nombre=input("Nombre: ").upper().strip()
    if nombre in agenda:
        print("Este contacto ya existe")
    else:
        tel=input("Telefono: ").strip()
        email=input("E-mail: ").lower().strip()
        agenda[nombre]=[tel,email]
        print("Accion Realizada con éxito")

def mostrar_contactos(agenda):
    borrarPantalla()
    print("Mostrar Contactos")
    if not agenda:
        print("No hay contactos")
    else:
        print(f"{'Nombre':<15} {'Telefono':<15} {'Email':<10}")
        print(f"-"*60)
        for nombre,datos in agenda.items(): #trae todo lo de los diccionarios, propia de ellos
            print(f"{nombre:<15} {datos[0]:<15} {datos[1]:<10}")    
        print(f"-"*60)

def buscar_contacto(agenda):
    borrarPantalla()
    print("Mostrar contactos")
    if not agenda:
        print("No hay contactos a mostrar")

    else:
        nombre=input("Ingresa el nombre a buscar: ").upper().strip()
        if nombre in agenda:
            # for nombres,datos in agenda.items():
            # print(f"{nombre:<15} {datos[0]:<15} {datos[1]:<10}") 
            print(f"{'Nombre':<15} {'Telefono':<15} {'Email':<10}")
            print(f"{nombre:<15} {agenda[nombre][0]:<15} {agenda[nombre][1]:<10}")#accede al diccionario, se trae los valores pero en la posicion que quiera
        else: 
            print("Contacto no existe")

def borrar_contacto(agenda):
    borrarPantalla()
    print("Borrar atributos")
    if not agenda:
        print("No hay contactos a mostrar")

    else:
        nombre=input("Ingresa el nombre a borrar: ").upper().strip()
        if nombre in agenda:
               yes=input("Deseas eliminar el contacto (Si/No): ").lower().strip()
               if yes=="si":
            # for nombres,datos in agenda.items(): #trae todo lo de los diccionarios, propia de ellos
                    agenda.pop(nombre)    
                    print("Accion realizada con exito")
               else: 
                   print("No existe ese contacto")   

def modificar_contacto(agenda):
    borrarPantalla()
    print("Modificar contactos")
    if not agenda:
        print("No hay contactos a modificar")

    else:
        nombre=input("Ingresa el nombre a modificar: ").upper().strip()
        if nombre in agenda:
            print("Valores actuales")
            print(f"Nombre: {nombre}\nTeléfono:{agenda[nombre][0]}\nE-mail:{agenda[nombre][1]}")
            resp=input("Deseas modificar los valores (Si/No): ").lower().strip()
            if resp=="si":
                tele=input("Ingresa el telefono a modificar: ").upper().strip()
                mail=input("Ingresa el mail a modificar: ").upper().strip()
                #for nombres,datos in agenda.items(): #trae todo lo de los diccionarios, propia de ellos
                agenda[nombre]=[tele,mail]
                print("Accion realizada con exito")
                #print(f"{nombres:<15} {datos[0]:<15} {datos[1]:<10}")            
            else:
                print("Este contacto no existe :()")    