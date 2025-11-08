from BD import tabla_categorias
from BD import conectar
from BD import linea

class Categoria():
    def __init__(self,id_categoria,nombre):
        self.__id_categoria=id_categoria
        self.nombre=nombre
        tabla_categorias()

    @property
    def categoria (self):
        return self.__id_categoria
    
    @categoria.setter
    def categoria(self, nuevo_id):
        self.__id_categoria=nuevo_id

    def agregar_categoria(self):
        print("----AGREGAR CATEGORIA----")
        while True:
            nombre=input("Ingrese el nombre de la categoria que desea agregar")
            try:
                conexion=conectar()
                cursor=conexion.cursor()
                cursor.execute("""insert into categorias (nombre) values(?)""",(nombre,))
                conexion.commit()
                print()
                print (f"La categoria {nombre} se agregó exitosamente")
                linea()
            except Exception as e:
                linea()
                print("Error al agregar una categoria",e)
                linea()
            finally:
                conexion.close()
            continuar=int(input("Si desea agregar otra categoria ingrese 1 sino 0 "))
            linea()
            if continuar != 1:
                break


    def eliminar_categoria(self):
        linea()
        print("----ELIMINAR CATEGORIA----")
        linea()
        while True:
            id=input("Ingrese el id de la categoria que desee eliminar")
            try:
                conexion=conectar()
                cursor=conexion.cursor()
                cursor.execute(""" delete from proveedores where id_categoria= ?""", (id,))
                conexion.commit()
                print(f"La categoria {id} fué eliminada correctamente")
            except Exception as e:
                print("Error al eliminar la categoria")
            finally:
                conexion.close()
            continuar=int(input("Si desea eliminar otra categoria  ingrese 1 sino 0 "))
            linea()
            if continuar != 1:
                break


    def modificar_categoria(self):
        id_cat=("Ingrese el id de la categoria que desea modficar")
        nombre=("Ingrese el su nuevo nombre")
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            cursor.execute(""" update categorias set nombre= ? where id_categoria= ? """, (id_cat, nombre))
            conexion.commit()
            print(f"La categoria {id_cat} fué modificada correctamente ")
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
                print("No hay categorias registradas")
            else: 
                for id_categoria, nombre in categorias:
                    print (f"Id: {id_categoria} - Nombre:{nombre}")
        except Exception as e:
            print("Error al mostrar las categorias ", e)
        finally:
            conexion.close()





