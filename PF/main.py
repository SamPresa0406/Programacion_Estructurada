import funciones
from paleteria import paleteria
from categoria import categoria
from usuarios import usuario
import getpass
import pandas as pd
from paleteria.paleteria import importacion_a_excel 
from categoria.categoria import importacion_a_excel2
from paleteria.paleteria import categoria_valida
from funciones import validar_vacio
def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usuarios()

        if opcion=="1" or opcion=="registro":
            funciones.borrarPantalla()
            print("\n\t\t\t\t\t\t.:::👤 Registrarse 👤:::. ")
            nombre=validar_vacio(input("\n\n\t\t\t\t\t\t 📝  \033[1mIngrese su nombre:\033[0m ")).upper().strip()
            apellidos=input("\n\t\t\t\t\t\t 📝  \033[1mIngrese sus apellidos:\033[0m ").upper().strip()
            email=input("\n\t\t\t\t\t\t 📝  \033[1mIngrese su e-mail:\033[0m ").lower().strip()
            # password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\n\t\t\t\t\t\t 🧾 \033[1mIngrese su contraseña:\033[0m ").strip()
            resultado=usuario.registrar(nombre,apellidos,email,password)
            if resultado:
                 print(f"\n\n\n\t\t\t\t\t .:::✅ Se registro el usuario {nombre} {apellidos} correctamente :::.")
                
            else:
                print("\n\n\t\t\t\t\t\t .:::❌ No fue posible registrar el usuario en este momento, intentalo mas tarde :::.")      
            funciones.esperarTecla()
         
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n\t\t\t\t\t\t.:::🔐 Iniciar Sesión 🔐:::. ")     
            email=input("\n\n\t\t\t\t\t\t 📝  \033[1mIngrese su e-mail:\033[0m ").lower().strip()
            password=getpass.getpass("\n\t\t\t\t\t\t🧾 \033[1mIngrese su contraseña:\033[0m ").strip()
            lista_usuarios=usuario.inicio_sesion(email,password)
            if lista_usuarios:
              menu_ambos(lista_usuarios[0],lista_usuarios[1],lista_usuarios[2])
            else:
                print("\n\n\t\t\t\t\t\t .:::❌ E-mail y/o contraseña incorrectas, por favor verifique :::.")
            funciones.esperarTecla()    
              
              
        elif opcion=="3" or opcion=="SALIR": 
            print("\n\t\t\t.:::🔚 Saliste del inventario de la paletería La Auténtica Mich Dgo :::.")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("\n\t\t\t.:::🙅‍♀️ Opción no válida, vuelve a intentar:::.")
            opcion=True
            funciones.esperarTecla() 





def menu_ambos(usuario_id,nombre,apellidos):
    op=True
    while op:
        funciones.borrarPantalla()
        op=funciones.menu_producto_categoria()
    
        if op=="1" or op=="categoria":
                funciones.borrarPantalla()
                def menu_categoria(usuario_id,nombre,apellidos):
                    while True:
                        funciones.borrarPantalla()
                        print(f"\n\t\t\t\t👋 Bienvenid@ {nombre} {apellidos}, acabas de iniciar sesión 🍡")
                        opcion=funciones.menu_categoria()
                    

                        if opcion == '1' or opcion=="agregar":
                            funciones.borrarPantalla()
                            print("\n\t\t\t\t\t\t.:::➕ Agregar categoría al inventario ➕:::. ")
                            inventario={}
                            inventario["nombre"]=input("\n\n\t\t\t\t\t\t 🖊️  \033[1mIngresa el nombre de la categoría:\033[0m ").upper().strip()
                            inventario["descripcion"]=input("\n\t\t\t\t\t\t 🖊️  \033[1mIngresa la descripción de la categoría:\033[0m ").upper().strip()
                            respuesta=categoria.agregar_categoria(usuario_id,inventario["nombre"],inventario["descripcion"])
                            if respuesta:
                                 print("\n\n\n\t\t\t\t\t\t .:::✅ La categoría se agregó con éxito :::.")
                            else:
                                print("\n\n\t\t\t\t\t\t .:::🚫 No se puedo agregar la categoría, intenta más tarde :::.")    
                            funciones.esperarTecla() 
                            
                        elif opcion == '2' or opcion=="mostrar":
                            funciones.borrarPantalla() 
                            lista_categoria=categoria.mostrar_categoria(usuario_id)
                            if len(lista_categoria)>0:
                                print("\n\t\t\t\t\t\t.:::✨ Categorías del inventario ✨:::.") 
                                print(f"{'\n\t\t\t\t\t🆔 ID':<10}{'\t\t\t👤 Nombre':<15}{'\t\t\t📝 Descripción':<15}")
                                print(f"-"*150)
                                for fila in lista_categoria:
                                    print(f"\t\t\t\t\t{fila[0]:<10}\t\t{fila[2]:<10}\t\t\t{fila[3]:<10}")
                            else:
                                print("\n\n\t\t\t\t\t\t .:::❌ No hay categorías en el inventario, intenta más tarde :::.")   
                            funciones.esperarTecla()
                            
                        elif opcion == '3' or opcion=="modificar":
                            funciones.borrarPantalla()
                            lista_categoria=categoria.mostrar_categoria(usuario_id)
                            if len(lista_categoria)>0:
                                print("\n\t\t\t\t\t\t.:::✨ Categorías del inventario ✨:::.") 
                                print(f"{'\n\t\t\t\t\t🆔 ID':<10}{'\t\t\t👤 Nombre':<15}{'\t\t\t📝 Descripción':<15}")
                                print(f"-"*150)
                                for fila in lista_categoria:
                                    print(f"\t\t\t\t\t{fila[0]:<10}\t\t{fila[2]:<10}\t\t{fila[3]:<10}")
                                resp=input("\n\n\t\t\t\t\t\t.:::🤔 \033[1m¿Deseas modificar alguna categoría?\033[0m (Si/No): ").lower().strip()
                                if resp=="si":
                                    funciones.borrarPantalla()
                                    print(f"\n\n\t\t\t\t\t📣.:::  {nombre} {apellidos}, vamos a modificar una categoría 📣:::.")
                                    id = input("\n\n\t\t\t\t\t\t.::: 🆔 \033[1mID de la categoría a modificar: \033[0m")
                                    inventario={}
                                    inventario["nombre"]=input("\n\n\t\t\t\t\t\t🖊️  \033[1mIngresa el nuevo nombre de la categoría:\033[0m ").upper().strip()
                                    inventario["descripcion"]=input("\n\t\t\t\t\t\t🖊️  \033[1mIngresa la nueva descripción de la categoría:\033[0m ").upper().strip()
                                    respuesta=categoria.cambiar_categoria(id, inventario["nombre"], inventario["descripcion"])
                                    if respuesta:
                                        print("\n\n\n\t\t\t\t\t\t.:::✅ La categoría se modificó con éxito:::.")
                                    else:
                                        print("\n\t\t\t\t\t\t.:::🚫 No fue posible modificar la categoría, intenta más tarde :::.")     
                            else:
                                print("\n\n\t\t\t\t\t\t .:::❌ No hay categorías en el inventario, intenta más tarde :::.")   
                            funciones.esperarTecla()            
                        elif opcion == '4' or opcion=="eliminar":
                            funciones.borrarPantalla()
                            lista_categoria=categoria.mostrar_categoria(usuario_id)
                            if len(lista_categoria)>0:
                                print("\n\t\t\t\t\t\t.:::✨ Categorías del inventario ✨:::.") 
                                print(f"{'\n\t\t\t\t\t🆔 ID':<10}{'\t\t\t👤 Nombre':<15}{'\t\t\t📝 Descripción':<15}")
                                print(f"-"*180)
                                for fila in lista_categoria:
                                    print(f"\t\t\t\t\t{fila[0]:<10}\t\t{fila[2]:<10}\t\t\t{fila[3]:<10}")
                                resp=input(f"\n\n\t\t\t\t\t\t.:::🤔 \033[1m¿Deseas borrar alguna categoría? (Si/No)\033[0m ").lower().strip()
                                if resp=="si":
                                    funciones.borrarPantalla()
                                    print(f"\n\n\t\t\t\t\t.:::⛔  {nombre} {apellidos}, vamos a borrar una categoría ⛔:::.")
                                    id = input("\n\n\t\t\t\t\t\t.::: 🆔 \033[1mID de la categoría a borrar:\033[0m ")
                                    respuesta=categoria.borrar_categoria(id)
                                    if respuesta:
                                        print("\n\n\t\t\t\t\t\t.:::✅ La categoría se borró con éxito:::.")
                                    else:
                                        print("\n\t\t\t\t\t\t.:::🚫 No fue posible borrar la categoría, intenta más tarde :::.")     
                            else:
                                print("\n\n\t\t\t\t\t\t .:::❌ No hay categorías en el inventario, intenta más tarde :::.")   
                            funciones.esperarTecla()  
                    
                        elif opcion == '5' or opcion=="buscar":
                            funciones.borrarPantalla()
                            print("\n\t\t\t\t\t\t.:::🔍 Buscar categorías del inventario 🔍:::.")
                            resp=input(f"\n\n\t\t\t\t\t\t.:::🤔 \033[1m¿Deseas buscar alguna categoría? (Si/No)\033[0m ").lower().strip()
                            if resp=="si":
                                funciones.borrarPantalla()
                                id=input(f"\n\n\t\t\t\t\t\t.::: 🆔 \033[1mID de la categoría a buscar:\033[0m ")
                                respuesta=categoria.buscar_categoria(id)
                                if respuesta:
                                    print(f"\n\n\t\t\t\t\t\t.::: 👀 Esta es la categoría {id}: ")
                                    print(f"-"*150)
                                    print(f"{'\n\t\t\t\t\t🆔 ID':<10}{'\t\t\t👤 Nombre':<15}{'\t\t📝 Descripción':<15}")
                                    print(f"-"*150)
                                    print(f"\t\t\t\t\t{respuesta[0]:<10}\t\t{respuesta[2]:<15}\t\t{respuesta[3]:<15}")
                                    print("\n\n\t\t\t\t\t\t.:::✅ La categoría se buscó con éxito:::.")
                                else:
                                        print("\n\t\t\t\t\t\t.:::🚫 No fue posible buscar la categoría, intenta más tarde :::.")     
                            else:
                                print("\n\n\t\t\t\t\t\t .:::❌ No hay búsquedas de categorías en el inventario, intenta más tarde :::.")   
                            funciones.esperarTecla()        
                        

                        elif opcion == '6':
                             funciones.borrarPantalla()
                             resp=input(f"\n\n\t\t\t\t\t\t.:::🤔 ¿Deseas importar una tabla a excel? (Si/No) ").lower().strip()
                             if resp=="si":
                                importacion_a_excel2()
                                print("\n\n\n\t\t\t\t\t\t .:::✅ Se exportó con éxito :::.")
                                funciones.esperarTecla
                             
                                
                        elif opcion == '7' or opcion=="SALIR":
                            break
                        
                        else:
                            print("\n\t\t\t.:::🚫 Opción no válida, intenta de nuevo 🚫:::.")
                            funciones.esperarTecla()

                menu_categoria(usuario_id, nombre, apellidos)
               
        elif op=="2" or op=="Productos":
                funciones.borrarPantalla()

                def menu_productos(usuario_id,nombre,apellidos):
                    while True:
                        funciones.borrarPantalla()
                        print(f"\n\t\t\t\t\t👋 Bienvenid@ {nombre} {apellidos}, acabas de iniciar sesión 🍡")
                        
                        opcion=funciones.menu_productos()

                        if opcion == '1' or opcion=="agregar":
                            funciones.borrarPantalla()
                            print("\n\t\t\t\t\t\t.:::➕ Agregar productos al inventario ➕:::. ")
                            inventario={}
                            inventario["nombre"]=input("\n\n\t\t\t\t\t\t 🖊️  \033[1mIngresa el nombre del producto:\033[0m ").upper().strip()
                            while True:
                                try:
                                    inventario["cantidad"] = int(input("\n\n\t\t\t\t\t\t 🖊️  \033[1mIngresa la cantidad del producto:\033[0m "))
                                    break
                                except ValueError:
                                    print("\n\n\t\t\t\t❌.::: Por favor, ingresa un número entero válido para la cantidad :::.")
                            while True:
                                try:
                                    inventario["precio_unitario"] = float(input("\n\t\t\t\t\t\t 🖊️  \033[1mIngresa el precio unitario del producto:\033[0m "))
                                    break
                                except ValueError:
                                    print("\n\n\t\t\t\t❌.::: Por favor, ingresa un número válido para la cantidad (puede ser con decimales) :::.")
                            
                            while True:
                                        try:
                                            codigo = int(input("\n\n\t\t\t\t\t\t🏷️ \033[1mCódigo de la categoría del producto:\033[0m "))
                                            if categoria_valida(codigo):
                                                inventario["codigo"] = codigo
                                                break
                                            else:
                                                 print("\n\n\t\t\t\t❌ Ese código no corresponde a ninguna categoría registrada.")
                                        except ValueError:
                                                print("\n\n\t\t\t\t❌ El código debe ser un número entero.")
                            respuesta=paleteria.agregar_producto(usuario_id,inventario["nombre"],inventario["cantidad"],inventario["precio_unitario"],inventario["codigo"])
                            if respuesta==True:
                                print("\n\n\n\t\t\t\t\t\t .:::✅ El producto se agregó con éxito :::.")
                            else:
                                print("\n\n\t\t\t\t\t\t .:::🚫 No se puedo agregar el producto, intenta más tarde :::.")    
                            funciones.esperarTecla() 
                            
             
                        elif opcion == '2' or opcion=="mostrar":
                            funciones.borrarPantalla()
                            #Agregar codigo  
                            lista_productos=paleteria.mostrar_producto(usuario_id)
                            if len(lista_productos)>0:
                                print("\n\t\t\t\t\t\t.:::✨ Productos del inventario ✨:::.") 
                                print(f"{'\n\t\t🆔 ID':<10}{'\t\t👤 Nombre':<15}{'\t\t📝 Cantidad':<10}{'\t\t📝 Precio unitario':<10}{'\t\t📝 Código':<10}")
                                print(f"-"*176)
                                for fila in lista_productos:
                                    print(f"\t\t{fila[0]:<10}\t\t{fila[2]:<15}\t\t{fila[3]:<10}\t\t\t{fila[4]:<10}\t\t\t{fila[5]:<10}")
                            else:
                                print("\n\n\t\t\t\t\t\t .:::❌ No hay productos en el inventario, intenta más tarde :::.")   
                            funciones.esperarTecla()
                       
                            
                        elif opcion == '3' or opcion=="modificar":
                            funciones.borrarPantalla()
                            lista_paleteria=paleteria.mostrar_producto(usuario_id)
                            if len(lista_paleteria)>0:
                                print("\n\t\t\t\t\t\t.:::✨ Productos del inventario ✨:::.") 
                                print(f"{'\n\t\t🆔 ID':<10}{'\t\t👤 Nombre':<15}{'\t\t📝 Cantidad':<10}{'\t\t📝 Precio unitario':<10}{'\t\t📝 Código':<10}")
                                print(f"-"*176)
                                for fila in lista_productos:
                                    print(f"\t\t{fila[0]:<10}\t\t{fila[2]:<15}\t\t{fila[3]:<10}\t\t\t{fila[4]:<10}\t\t\t{fila[5]:<10}")
                                print(f"-"*176)
                                resp=input("\n\n\t\t\t\t\t\t.:::🤔 ¿Deseas modificar algún producto? (Si/No) ").lower().strip()
                                if resp=="si":
                                    funciones.borrarPantalla()
                                    print(f"\n\n\t\t\t\t\t.:::✨  {nombre} {apellidos}, vamos a modificar una categoría ✨:::.")
                                    id = input("\n\n\t\t\t\t\t\t.::: 🆔 \033[1mID del producto a modificar:\033[0m  ")
                                    inventario={}
                                    while True:
                                        
                                        inventario["nombre"]=input("\n\t\t\t\t\t 🖊️  \033[1mIngresa el nombre nuevo del producto:\033[0m ").upper().strip()
                                    while True:
                                        try:
                                            inventario["cantidad"]=int(input("\n\t\t\t\t\t 🖊️  \033[1mIngresa la cantidad nueva del producto:\033[0m "))
                                            break
                                        except ValueError:
                                            print("\n\n\t\t\t\t❌.::: Por favor, ingresa un número entero válido para la cantidad :::.")
                                    while True:
                                        try:
                                           inventario["precio_unitario"]=float(input("\n\t\t\t\t\t 🖊️  \033[1mIngresa el precio unitario nuevo del producto:\033[0m "))
                                           break
                                        except ValueError:
                                            print("\n\n\t\t\t\t❌.::: Por favor, ingresa un número válido para la cantidad (puede ser con decimales) :::.")
                                    while True:
                                        try:
                                            codigo = int(input("\n\n\t\t\t\t\t\t🏷️ \033[1mCódigo de la categoría del producto:\033[0m "))
                                            if categoria_valida(codigo):
                                                inventario["codigo"] = codigo
                                                break
                                            else:
                                                 print("\n\n\t\t\t\t❌ Ese código no corresponde a ninguna categoría registrada.")
                                        except ValueError:
                                                print("\n\n\t\t\t\t❌ El código debe ser un número entero.")
                                    respuesta=paleteria.cambiar_producto(id, inventario["nombre"], inventario["cantidad"], inventario["precio_unitario"],inventario["codigo"])
                                    if respuesta==True:
                                        print("\n\n\n\t\t\t\t\t\t .:::✅ El producto se modificó con éxito :::.")
                                    else:
                                        print("\n\n\t\t\t\t\t\t .:::🚫 No se puedo modificar el producto, intenta más tarde :::.")    
                                        funciones.esperarTecla()           
                            else:
                                print("\n\n\t\t\t\t\t\t .:::❌ No hay productos en el inventario, intenta más tarde :::.")   
                            funciones.esperarTecla()
                        
                        
                        elif opcion == '4' or opcion=="eliminar":
                            funciones.borrarPantalla()
                            lista_categoria=paleteria.mostrar_producto(usuario_id)
                            if len(lista_categoria)>0:
                                print("\n\t\t\t\t\t\t.:::✨ Productos del inventario ✨:::.") 
                                print(f"{'\n\t\t🆔 ID':<10}{'\t\t👤 Nombre':<15}{'\t\t📝 Cantidad':<10}{'\t\t📝 Precio unitario':<10}{'\t\t📝 Código':<10}")
                                print(f"-"*176)
                                for fila in lista_productos:
                                    print(f"\t\t{fila[0]:<10}\t\t{fila[2]:<15}\t\t{fila[3]:<10}\t\t\t{fila[4]:<10}\t\t\t{fila[5]:<10}")
                                print(f"-"*176)
                                resp=input(f"\n\n\t\t\t\t\t\t.:::🤔 ¿Deseas borrar un producto? (Si/No)\033[0m ").lower().strip()
                                if resp=="si":
                                    print(f"\n\n\t\t\t\t\t.:::⛔  {nombre} {apellidos}, vamos a borrar un producto ⛔:::.")
                                    id = input("\n\n\t\t\t\t\t\t.::: 🆔 \033[1mID del producto a borrar:\033[0m ")
                                    respuesta=paleteria.borrar_producto(id)
                                    if respuesta:
                                        print("\n\n\t\t\t\t\t\t.:::✅ El producto se borró con éxito:::.")
                                    else:
                                        print("\n\t\t\t\t\t\t.:::🚫 No fue posible borrar el producto, intenta más tarde :::.")     
                            else:
                                print("\n\n\t\t\t\t\t\t .:::❌ No hay productos en el inventario, intenta más tarde :::.")   
                            funciones.esperarTecla()  
                                
                        elif opcion == '5' or opcion=="buscar":
                            funciones.borrarPantalla()
                            print("\n\t\t\t\t\t\t.:::🔍 Buscar productos del inventario 🔍:::.")
                            resp=input(f"\n\n\t\t\t\t\t\t.:::🤔 ¿Deseas buscar algún producto? (Si/No) ").lower().strip()
                            if resp=="si":
                                # funciones.borrarPantalla()
                                id=input(f"\n\n\t\t\t\t\t\t.::: 🆔 \033[1mID del producto a buscar:\033[0m ")
                                respuesta=paleteria.buscar_producto(id)
                                if respuesta:
                                    print(f"\n\n\t\t\t\t\t\t.::: 👀 Esta es el producto {id}: ")
                                    print(f"-"*150)
                                    print(f"{'\n\t\t🆔 ID':<10}{'\t\t👤 Nombre':<15}{'\t\t📝 Cantidad':<10}{'\t\t📝 Precio unitario':<10}{'\t\t📝 Código':<10}")
                                    print(f"-"*150)
                                    print(f"\t\t{respuesta[0]:<10}\t\t{respuesta[2]:<15}\t\t{respuesta[3]:<10}\t\t\t{respuesta[4]:<10}\t\t\t{respuesta[5]:<10}")
                                    print("\n\n\t\t\t\t\t\t.:::✅ La categoría se buscó con éxito:::.")
                                else:
                                        print("\n\t\t\t\t\t\t.:::🚫 No fue posible buscar el producto, intenta más tarde :::.")     
                            else:
                                print("\n\n\t\t\t\t\t\t .:::❌ No hay productos en el inventario, intenta más tarde :::.")   
                            funciones.esperarTecla()       
                                
                         
                        elif opcion == '6':
                             funciones.borrarPantalla()
                             resp=input(f"\n\n\t\t\t\t\t\t.:::🤔 ¿Deseas importar una tabla a excel? (Si/No) ").lower().strip()
                             if resp=="si":
                                importacion_a_excel()
                                print("\n\n\n\t\t\t\t\t\t .:::✅ Se exportó con éxito :::.")
                                funciones.esperarTecla
                        
                                
                        elif opcion == '7' or opcion=="SALIR":
                            break
                        else:
                            print("\n\t\t\t.:::🚫 Opción no válida, intenta de nuevo 🚫:::.")
                            funciones.esperarTecla()

                            
                menu_productos(usuario_id,nombre,apellidos)         
                
        elif op == "3" or op == "SALIR":
            op=False
            print("\n\t\t\t\t\t\t.:::✔️ Redirigiendo al login ✔️:::.")
            
            funciones.esperarTecla()
            break           
                    
if __name__ == "__main__":
    main()    