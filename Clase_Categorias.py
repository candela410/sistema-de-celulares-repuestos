from BD import tabla_categorias
from BD import conectar
class Categoria():
    def __init__(self,Id_categoria,nombre):
        self.__Id_categoria=Id_categoria
        self.nombre=nombre
        tabla_categorias()

    @property
    def id_categoria (self):
        return categoria
    
    def agregar_categoria(self):
        conexion=conectar()
        cursor=conexion.cursor()
        nombre=input("Ingrese el nombre de la categoria que desea agregar")
        cursor.execute("""insert into categorias (nombre) values(?)""",nombre)
        print (f"La categoria {nombre} se agregó exitosamente")
        conexion.commit()
        conexion.close()

    def eliminar_categoria(self):
        conexion=conectar()
        cursor=conexion.cursor()
        id=input("Ingrese el id de la categoria que desee eliminar")
        cursor.execute(""" delete from proveedores where id_categoria= ?""", id)
        conexion.commit()
        conexion.close()
        print(f"La categoria {id} fué eliminada correctamente")

    def modificar_categoria(self):
        conexion=conectar()
        cursor=conexion.cursor()
        id_cat=("Ingrese el id de la categoria que desea modficar")
        nombre=("Ingrese el su nuevo nombre")
        cursor.execute(""" update categorias set nombre= ? where id_categoria= ? """, id_cat, nombre)
        conexion.commit()
        conexion.close()
        print(f"La categoria {id_cat} fué modificada correctamente ")

    def mostrar_categorias (self):
        conexion=conectar()
        cursor=conexion.cursor()
        cursor.execute("""select * from categorias""")
        categorias=list(cursor.fetchall())
        for id_categoria, nombre in categorias:
            print (f"Id: {id_categoria} - Nombre:{nombre}")
        conexion.close()
