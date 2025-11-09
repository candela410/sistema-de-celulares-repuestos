from BD import conectar
from BD import linea
from BD import tablas
class Marca():  
    def __init__(self,id_marca=None, nombre=""):
        self.__id_marca=id_marca
        self.nombre=nombre
        tablas()
       
    
    @property
    def marca (self):
        return self.__id_marca
    
    @marca.setter
    def marca(self, nueva_marca):
        self.__id_marca=nueva_marca


    def agregar_marca(self):
        while True:
            nombre=input("Ingresar el nombre de la nueva marca:  ").strip().lower()
            try:
                conexion=conectar()
                cursor=conexion.cursor()
                cursor.execute("""insert into marcas(nombre) values (?)""", (nombre,))
                conexion.commit()
                print()
                print("La nueva marca fué agregada correctamente")
            except Exception as e:
                print("Error al agregar la marca",e)
            finally:
                conexion.close()
            linea()
            continuar=int(input("Si desea agregar otra marca ingrese 1 sino 0 "))
            linea()
            if continuar != 1:
                break
        

    def eliminar_marca(self):
        while True:
            nombre=input("Ingresar el nombre de la marca que desea eliminar:  ").strip().lower()
            cursor.execute("select id_marca from Marcas where nombre= ?",(nombre,))
            id=cursor.fetchone()
            try:
                conexion=conectar()
                cursor=conexion.cursor()
                cursor.execute("""delete from categorias where id_categoria= ?""", (id,))
                conexion.commit()
                print()
                print("La marca se eliminó correctamente")
            except Exception as e:
                print ("Error al eliminar la marca", e)
            finally:
                conexion.close()
            continuar=int(input("Si desea eliminar otra marca ingrese 1 sino 0 "))
            linea()
            if continuar != 1:
                break
        
        
    
    def modificar_marca(self):
        while True:
            nombre=input("Ingresar el nombre de a marca que desea modificar:  ").strip().lower()
            cursor.execute("select id_marca from Marcas where nombre=?", (nombre,))
            id=cursor.fetchone()
            nuevo=input("Ingresar su nuevo nombre:  ").strip().lower()
            try:
                conexion=conectar()
                cursor=conexion.cursor()
                cursor.execute(""" update marcas set nombre= ? where id_marca= ?""",(nuevo, id))
                conexion.commit()
                print("Se modificó correctamente....")
            except Exception as e:
                print("Error al modificar la marca...",e)
            finally:
                conexion.close()
            linea()
            continuar=int(input("Si desea modificar otra marcaingrese 1 sino 0 "))
            linea()
            if continuar != 1:
                break

        
      
    def listar_marca(self):
        linea()
        print("----LISTA DE MARCAS----")
        linea()
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            cursor.execute("""select * from marcas""")
            marcas=list(cursor.fetchall())
            if not marcas:
                print()
                print("No hay marcas registradas...")
                print()
            else:
                for id_marca, nombre in marcas:
                    print()
                    print(f"ID: {id_marca} - Nombre:{nombre}")
                    print()
        except Exception as e:
            print("Error al listas las marcas",e)
        finally:
            conexion.close()