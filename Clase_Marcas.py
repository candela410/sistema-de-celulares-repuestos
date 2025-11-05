from BD import tabla_marcas
from BD import conectar

class Marca():  
    def __init__(self,Id_marca, nombre):
        self.__Id_marca=Id_marca
        self.nombre=nombre
        tabla_marcas()

    def agregar_marca(self):
        conexion=conectar()
        cursor=conexion.cursor()
        nombre=input("Ingresar el nombre de la nueva marca")
        cursor.execute("""inser into marcas(nombre) values (?)""", nombre)
        conexion.commit()
        conexion.close()
        print("La nueva fue agregada correctamente ")

    def eliminar_marca(self):
        conexion=conectar()
        cursor=conexion.cursor()
        id=input("Ingresar el ID de la marca que desea eliminar")
        cursor.execute("""delete from categorias where id_categoria= ?""", id)
        conexion.commit()
        conexion.close()
        print("La marca se eliminó correctamente")
    
    def modificar_marca(self):
        conexion=conectar()
        cursor=conexion.cursor()
        id=input("Ingresar el ID de a marca que desea modificar.")
        nombre=input("Ingresar su nuevo nombre")
        cursor.execute(""" update marcas set nombre= ? where id_marca= ?""", nombre, id)
        conexion.commit()
        conexion.close()
        print("Se modificó correctamente. ")

    
