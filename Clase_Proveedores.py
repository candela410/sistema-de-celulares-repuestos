from BD import tabla_proveedores
from BD import conectar
class Proveedor():
    def __init__(self, id_proveedor,nombre,telefono, direccion, estado):
        self.Id_proveedor=id_proveedor
        self.nombre=nombre
        self.telefono=telefono
        self.direccion=direccion
        self.estado=estado
        tabla_proveedores()


    def agregar_proveedor(self):
        nombre=input("Ingresar el nombre del proveedor:  ")
        telefono=input("Ingresar el teléfono:  ")
        direccion=input("Ingrese la dirección:  ")
        estado=input("Ingrese el estado del proveedor (Activo-Inactivo):  ")

        try:
            conexion=conectar()
            cursor=conexion.cursor()
            cursor.execute("""
                insert into proveedores (nombre,telefono,direccion,estado) values (?,?,?,?)""",nombre,telefono, direccion,estado)
            print(f"El proveedor {nombre} fué agregado correctamente :)")
            conexion.commit()
        except Exception as e:
            print ("Error al agregar un proveedor",e)
        finally:
            conexion.close()


    def eliminar_proveedor(self):
        proveedor=input("Ingrese el ID del proveedor que desea Eliminar: ")
       
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            cursor.execute("delete from proveedores where id_proveedor= ?",proveedor)
            conexion.commit()
            print(f"El proveedor fue eliminado correctamente")
        
        except Exception as e:
            print("Error al eliminar un proveedor",e)

        finally:
            conexion.close()
        

    def ejecucion_modificacion_prov(self,nombre_columna,dato,proveedor):
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            cursor.execute("""update proveedores set {nombre_columna}= ? where Id_proveedor= ?""",dato,proveedor)
            conexion.commit()
            print(f"El atributo{nombre_columna} fue modificado ")
        except Exception as e:
            print ("Error al modificar: ",e)
        finally:
            conexion.close() 

    def modificar_proveedores(self):
        proveedor=int(input("Ingrese el Id del proveedor el cual desea modificar: "))
        print ("--ATRIBUTOS PARA MODIFICAR--")
        print ("1-Nombre")
        print ("2-Telefono")
        print ("3-Dirección")
        print ("4-Estado")
        opcion=input("Ingrese el numero del atributo que desea modificar:  ")
        dato=input("Ingresar el nuevo valor: ")
        columnas={"1":"Nombre", "2":"Telefono","3":"Direccion","4":"Estado"}
        if opcion in columnas:
            nombre_columna=columnas[opcion]
            self.ejecucion_modificacion_prov(nombre_columna, dato, proveedor)
        else: 
            print("Opcion invalida")


      

    def mostrar_proveedores(self):
        print ("--LISTA DE PROVEEDORES--")
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            cursor.execute(""" select * from proveedores""")
            proveedores=list(cursor.fetchall())
            if not proveedores:
                print ("No hay proveedores registrados")
            else:
                for id_proveedor, nombre, telefono, direccion,estado in proveedores:
                    print (f"Id:{id_proveedor}- Nombre: {nombre}- Telefono:{telefono}- Dirección:{direccion}-Estado:{estado}")
        except Exception as e:
            print("Error al mostrar los proveedores: ",e)
        finally:
            conexion.close()

    