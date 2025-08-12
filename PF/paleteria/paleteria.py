from conexionBD import *
import pandas as pd
import categoria

def agregar_producto(usuario_id,nombre,cantidad,precio,codigo):
    try:
        cursor.execute("insert into productos (usuario_id, nombre, cantidad, precio,codigo) values (%s,%s,%s,%s,%s)",(usuario_id,nombre,cantidad,precio,codigo))
        conexion.commit()
        return True           
    
    except Exception as e:
        print("Error al agregar producto:", e)
        return False

def categoria_valida(codigo):
    cursor.execute("select id from categoria where id = %s", (codigo,))
    return cursor.fetchone()       
        
def mostrar_producto(usuario_id):
    try:
        cursor.execute("select * from productos where usuario_id=%s",(usuario_id,))
        return cursor.fetchall()
    except:       
        return []  
    
def cambiar_producto(id,nombre,cantidad,precio,codigo):
    try:
        
        cursor.execute("update productos set nombre=%s, cantidad=%s, precio=%s, codigo=%s where productos.id=%s;",(nombre,cantidad,precio,codigo,id))
        conexion.commit()
        return True
    except:
        return False  
        
def borrar_producto(id):
    try:
        cursor.execute("delete from productos where id=%s",(id,))
        conexion.commit()
        return True
    except:
        return False 
    
def buscar_producto(id):
    try:
        cursor.execute("select * from productos where id=%s",(id,))
        return cursor.fetchone()
    except:
        return []         
         
def importacion_a_excel():
    df = pd.read_sql("SELECT * FROM productos", conexion)

    df.to_excel("productos_exportados.xlsx", index=False)     