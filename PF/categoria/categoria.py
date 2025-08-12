from conexionBD import *
import pandas as pd

def agregar_categoria(usuario_id,nombre,descripcion):
    try:
        cursor.execute("insert into categoria (usuario_id,nombre, descripcion) values (%s,%s,%s)",(usuario_id,nombre,descripcion))
        conexion.commit()
        return True            
    except:
        return False
       
def mostrar_categoria(usuario_id):
    try:
        cursor.execute("select * from categoria where usuario_id=%s",(usuario_id,))
        return cursor.fetchall()
    except:       
        return []
        
def cambiar_categoria(id,nombre,descripcion):
    try:
        
        cursor.execute("update categoria set nombre=%s, descripcion=%s where categoria.id=%s;",(nombre,descripcion,id))
        conexion.commit()
        return True
    except:
        return False  
        
def borrar_categoria(id):
    try:
        cursor.execute("delete from categoria where id=%s",(id,))
        conexion.commit()
        return True
    except:
        return False 
    
def buscar_categoria(id):
    try:
        cursor.execute("select * from categoria where id=%s",(id,))
        return cursor.fetchone()
    except:
        return []         
         
def importacion_a_excel2():
    df = pd.read_sql("SELECT * FROM categoria", conexion)

    df.to_excel("categorias_exportadas.xlsx", index=False)        