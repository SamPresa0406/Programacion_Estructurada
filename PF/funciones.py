def borrarPantalla():
  import os  
  os.system("cls")

def esperarTecla():
  input("\n\n\t\t\t\t\t ... ⚠️ Oprima cualquier tecla para continuar ⚠️ ...")

def menu_usuarios():
  print("\n\t\t\t.:::🍦 Sistema de Gestión de inventario de la paletería La Auténtica Mich Dgo 🍧:::.  \n\n\n\t\t\t\t\t\t1.-👤 \033[1mRegistrarse\033[0m\n\t\t\t\t\t\t2.-🔐 \033[1mIniciar Sesión\033[0m\n\t\t\t\t\t\t3.-🔚 \033[1mSalir\033[0m ")
  opcion=input("\n\n\t\t\t\t\t .:::👉 Elige una opción : ").upper().strip()
  return opcion
 
def menu_producto_categoria():
  print("\n\t\t\t\t.:::📦 Gestión de Categorías y Productos 📦:::.  \n\n\n\t\t\t\t\t\t1.-🏷️  \033[1mCategorías\033[0m\n\t\t\t\t\t\t2.-🍨  \033[1mProductos\033[0m\n\t\t\t\t\t\t3.-🔚  \033[1mSalir\033[0m  ")
  opcion = input("\n\n\t\t\t\t\t .:::👉 Elige una opción :").upper().strip()
  return opcion 

def menu_productos():
  print("\n\t\t\t\t\t.:::🍨 Menú de opciones en Productos 🍨:::.\n\n\t\t\t\t\t\t1.-➕  \033[1mAgregar producto\033[0m\n\t\t\t\t\t\t2.-👁️  \033[1mMostrar producto\033[0m\n\t\t\t\t\t\t3.-✏️  \033[1mModificar producto\033[0m\n\t\t\t\t\t\t4.-🗑️  \033[1mEliminar producto\033[0m\n\t\t\t\t\t\t5.-🔍  \033[1mBuscar producto\n\t\t\t\t\t\t6.-📤  \033[1mExportar a PDF\033[0m\n\t\t\t\t\t\t7.-🔚 \033[1mSALIR\033[0m")
  opcion=input("\n\t\t\t\t\t .:::👉 Elige una opción : ").upper().strip()  
  return opcion
 
def menu_categoria():
   print("\n\t\t\t\t\t.:::🏷️ Menú de opciones en Categorías 🏷️:::.\n\n\t\t\t\t\t\t1.-➕ \033[1mAgregar categoría\033[0m\n\t\t\t\t\t\t2.-👁️ \033[1mMostrar categoría\033[0m\n\t\t\t\t\t\t3.-✏️ \033[1mModificar categoría\033[0m\n\t\t\t\t\t\t4.-🗑️ \033[1mEliminar categoría\0[0m\n\t\t\t\t\t\t5.-🔍 \033[1mBuscar categoría\n\t\t\t\t\t\t6.-📤 \033[1mExportar a PDF\033[0m\n\t\t\t\t\t\t7.-🔚 \033[1mSALIR\033[0m")
   opcion=input("\n\n\t\t\t\t\t .:::👉 Elige una opción : ").upper().strip()  
   return opcion
