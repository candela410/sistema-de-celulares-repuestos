from BD import tabla_proveedores
from BD import conectar
from BD import linea
class Proveedor():
    def __init__(self, id_proveedor=None,nombre="",telefono=None, direccion="", estado="Activo"):
        self.Id_proveedor=id_proveedor
        self.nombre=nombre
        self.telefono=telefono
        self.direccion=direccion
        self.estado=estado
        tabla_proveedores()

    def agregar_proveedor(self):
        linea()
        print("----AGREGAR PROVEEDORES----")
        linea()
        while True:
            nombre=input("Ingresar el nombre del proveedor:  ")
            telefono=input("Ingresar el teléfono:  ")
            direccion=input("Ingrese la dirección:  ")
        
            try:
                conexion=conectar()
                cursor=conexion.cursor()
                cursor.execute("""
                    insert into proveedores (nombre,telefono,direccion,estado) values (?,?,?,"Activo")""",(nombre,telefono, direccion))
                print()
                print(f"El proveedor {nombre} fué agregado correctamente :)")
                linea()
                conexion.commit()
            except Exception as e:
                linea()
                print ("Error al agregar un proveedor:  ",e)
                linea()
            finally:
                conexion.close()
            print()
            continuar=int(input("Si desea agregar otro producto ingrese 1 sino 0 "))
            linea()
            if continuar != 1:
                break
        


    def eliminar_proveedor(self):
        linea()
        print("----ELIMINAR UN PROVEEDOR----")
        linea()
        while True:
            proveedor=input("Ingrese el ID del proveedor que desea Eliminar: ")
       
            try:
                conexion=conectar()
                cursor=conexion.cursor()
                cursor.execute("delete from proveedores where id_proveedor= ?",(proveedor,))
                conexion.commit()
                print()
                print(f"El proveedor fue eliminado correctamente")
                linea()
        
            except Exception as e:
                linea()
                print("Error al eliminar un proveedor",e)
                linea()
            finally:
                conexion.close()
            continuar=int(input("Si desea agregar otro proveedor ingrese 1 sino 0 "))
            linea()
            if continuar != 1:
                break
        
        

    def ejecucion_modificacion_prov(self,nombre_columna,dato,proveedor):
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            cursor.execute(f"""update proveedores set {nombre_columna}= ? where Id_proveedor= ?""",(dato,proveedor))
            conexion.commit()
            print()
            print(f"El atributo{nombre_columna} fue modificado ")
            linea()
        except Exception as e:
            linea()
            print ("Error al modificar: ",e)
            linea()
        finally:
            conexion.close() 

    def modificar_proveedores(self):
        linea()
        print("----MODIFICAR PROVEEDOR----")
        linea()
        while True:
            proveedor=int(input("Ingrese el Id del proveedor el cual desea modificar: "))
            print ("--ATRIBUTOS PARA MODIFICAR--")
            print ("1- Nombre")
            print ("2- Telefono")
            print ("3- Dirección")
            print ("4- Estado")
            opcion=input("Ingrese el numero del atributo que desea modificar:  ")
            dato=input("Ingresar el nuevo valor: ")
            columnas={"1":"Nombre", "2":"Telefono","3":"Direccion","4":"Estado"}
            if opcion in columnas:
                nombre_columna=columnas[opcion]
                self.ejecucion_modificacion_prov(nombre_columna, dato, proveedor)
            else: 
                print("Opcion invalida")
            print()
            continuar=int(input("Si desea modificar otro proveedor ingrese 1 sino 0 "))
            linea()
            if continuar != 1:
                break
        


      

    def mostrar_proveedores(self):
        linea()
        print ("--LISTA DE PROVEEDORES--")
        linea()
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            cursor.execute(""" select * from proveedores""")
            proveedores=list(cursor.fetchall())
            if not proveedores:
                print()
                print ("No hay proveedores registrados")
                print()
            else:
                for id_proveedor, nombre, telefono, direccion,estado in proveedores:
                    print()
                    print (f"Id:{id_proveedor}- Nombre: {nombre}- Telefono:{telefono}- Dirección:{direccion}-Estado:{estado}")
                    linea()
        except Exception as e:
            print("Error al mostrar los proveedores: ",e)
        finally:
            conexion.close()
        linea()