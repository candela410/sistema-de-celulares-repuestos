from BD import conectar
from BD import linea
from BD import tablas

class Categoria():
    def __init__(self,id_categoria=None,nombre=""):
        self.__id_categoria=id_categoria
        self.nombre=nombre
        tablas()
       

    @property
    def categoria (self):
        return self.__id_categoria
    
    @categoria.setter
    def categoria(self, nuevo_id):
        self.__id_categoria=nuevo_id

    def agregar_categoria(self):
        print("----AGREGAR CATEGORIA----")
        linea()
        while True:
            nombre=input("Ingrese el nombre de la categoria que desea agregar:  ").strip().lower()
            try:
                conexion=conectar()
                cursor=conexion.cursor()
                cursor.execute("""insert into categorias (nombre) values(?)""",(nombre,))
                conexion.commit()
                print()
                print (f"La categoria {nombre} se agregó exitosamente...")
                linea()
            except Exception as e:
                linea()
                print("Error al agregar una categoria:  ",e)
                linea()
            finally:
                conexion.close()
            continuar=int(input("Si desea agregar otra categoria ingrese 1 sino 0:   "))
            linea()
            if continuar != 1:
                break


    def eliminar_categoria(self):
        linea()
        print("----ELIMINAR CATEGORIA----")
        linea()
        while True:
            nombre=input("Ingrese el nombre de la categoria que desee eliminar:  ").strip().lower()
            cursor.execute("select id_categoria from Categorias where nombre=?", (nombre,))
            id=cursor.fetchonet()
            try:
                conexion=conectar()
                cursor=conexion.cursor()
                cursor.execute(""" delete from proveedores where id_categoria= ?""", (id,))
                conexion.commit()
                print()
                print(f"La categoria {id} fué eliminada correctamente...")
            except Exception as e:
                print("Error al eliminar la categoria...")
            finally:
                conexion.close()
            continuar=int(input("Si desea eliminar otra categoria  ingrese 1 sino 0:   "))
            linea()
            if continuar != 1:
                break


    def modificar_categoria(self):
        nombre=input("Ingrese el nombre de la categoria que desea modficar").strip().lower()
        cursor.execute("select id_categoria from Categorias where nombre=?", (nombre,))
        id=cursor.fetchone()
        nuevo=("Ingrese el su nuevo nombre")
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            cursor.execute(""" update categorias set nombre= ? where id_categoria= ? """, (nuevo, id))
            conexion.commit()
            print(f"La categoria {id} fué modificada correctamente ")
        except Exception as e:
            print ("Error al modificar una categoria",e)
        finally:
            conexion.close()


    def mostrar_categorias (self):
        linea()
        print("----LISTA DE CATEGORIAS----")
        linea()
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            cursor.execute("""select * from categorias""")
            categorias=list(cursor.fetchall())
            if not categorias:
                print("No hay categorias registradas...")
            else: 
                for id_categoria, nombre in categorias:
                    print (f"Id: {id_categoria} - Nombre:{nombre}")
        except Exception as e:
            print("Error al mostrar las categorias ", e)
        finally:
            conexion.close()






