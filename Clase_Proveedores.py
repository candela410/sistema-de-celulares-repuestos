from BD import conectar, linea, tablas, limpiar_pantalla, pausa

class Proveedor():
    def __init__(self, id_proveedor=None,nombre="",telefono=None, direccion="", estado=""):
        self.Id_proveedor=id_proveedor
        self.nombre=nombre
        self.telefono=telefono
        self.direccion=direccion
        self.estado=estado
        tablas()
    


    def agregar_proveedor(self):
        limpiar_pantalla()
        linea()
        print("----AGREGAR PROVEEDORES----")
        linea()
        while True:
            limpiar_pantalla
            nombre=input("Ingresar el nombre del proveedor:  ").strip().lower()
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
            continuar=int(input("Si desea agregar otro proveedor ingrese 1 sino 0 "))
            linea()
            if continuar != 1:
                break
            pausa()
        pausa()
        

    def eliminar_proveedor(self):
        limpiar_pantalla()
        while True:
            linea()
            print("----ELIMINAR UN PROVEEDOR----")
            linea()
            proveedor=input("Ingrese el nombre del proveedor que desea Eliminar: ").strip().lower()
            cursor.execute("select id_proveedor from Proveedores where nombre= ?",(proveedor,))
            id=cursor.fetchone()
       
            try:
                conexion=conectar()
                cursor=conexion.cursor()
                cursor.execute("delete from proveedores where id_proveedor= ?",(id,))
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
        pausa()
        
        

    def ejecucion_modificacion_prov(self,nombre_columna,dato,proveedor2):
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            cursor.execute(f"""update Proveedores set {nombre_columna}= ? where id_proveedor= ?""",(dato,proveedor2))
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
        limpiar_pantalla()
        linea()
        print("----MODIFICAR PROVEEDOR----")
        linea()
        while True:
            conexion=conectar()
            cursor=conexion.cursor()
            proveedor=input("Ingrese el nombre del proveedor el cual desea modificar: ").strip().lower()
            cursor.execute("select id_proveedor from Proveedores where nombre =? ",(proveedor,) )
            proveedor1=cursor.fetchone()
            proveedor2=proveedor1[0]
            
            print ("--ATRIBUTOS PARA MODIFICAR--")
            print ("1- Nombre")
            print ("2- Telefono")
            print ("3- Dirección")
            print ("4- Estado")
            opcion=input("Ingrese el numero del atributo que desea modificar:  ")
            dato=input("Ingresar el nuevo valor: ")
            columnas={"1":"nombre", "2":"telefono","3":"direccion","4":"estado"}
            if opcion in columnas:
                nombre_columna=columnas[opcion]
                self.ejecucion_modificacion_prov(nombre_columna, dato, proveedor2)
            else: 
                print("Opcion invalida")
            print()
            continuar=int(input("Si desea modificar otro proveedor ingrese 1 sino 0 "))
            linea()
            if continuar != 1:
                break
        pausa()
        


    def mostrar_proveedores(self):
        limpiar_pantalla()
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
        pausa()
            

    

    

            

    
