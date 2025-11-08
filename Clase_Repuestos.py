

from BD import tabla_repuestos
from BD import conectar
from BD import linea


class Repuesto():
    def __init__(self,id_repuesto=None, nombre="", stock=0,precio_unitario=0.0,id_marca=None,id_categoria=None):
        self.id_repuesto=id_repuesto
        self.nombre=nombre
        self.stock=stock
        self.precio_unitario=precio_unitario
        self.marca=id_marca
        self.categoria=id_categoria
        tabla_repuestos()
    
    def agregar_repuestos(self):
        linea()
        print ("----AGREGAR REPUESTO----")
        linea()
        while True:
            try:
                conexion=conectar()
                cursor=conexion.cursor()
                nombre=input("Ingrese el nombre del nuevo repuesto:  ").strip()
                if " " in nombre or nombre=="":
                    print("Nombre invalido")
                else:
                    print("Nombre válido")
                b=True
                while b==True:
                    stock=int(input("Ingresar su stock:  "))
                    if stock >= 0:
                        b=False
                precio_unitario=float(input("Ingresar el precio unitario:   "))
                marca=input("Ingresar el nombre de la marca:  ").strip()
                cursor.execute("""select id_marca from Marcas where nombre= ?""", (marca,))
                marca1=cursor.fetchone()
                if not marca1:
                    linea()
                    print("La marca no se encuentra registrada")
                    linea()
                categoria=input("Ingresar el ID de la categoria: ").strip()
                cursor.execute("""select id_categoria from Categorias where nombre= ?""",(categoria,))
                categoria1=cursor.fetchone()
                if not categoria1:
                    linea()
                    print("La categoria no se encuentra registrada")
                    linea()
                cursor.execute(""" insert into repuestos ( nombre, stock,precio_unitario,id_marca,id_categoria) values (?,?,?,?,?)""", (nombre, stock, precio_unitario, marca1, categoria1))
                conexion.commit()
                id_repuesto=cursor.lastrowid
                linea()
                print("Se agrego el repuesto  (",id_repuesto,")   a la BD")
                linea()
            except Exception as e:
                linea()
                print("Error al agregar el repuesto:  ",e)
                linea()
            finally:
                conexion.close ()
            linea()
            continuar=int(input("Si desea agregar otro producto ingrese 1 sino 0 "))
            linea()
            if continuar != 1:
                break
        

    def eliminar_repuestos(self):
        linea()
        print("----ELIMINAR REPUESTO----")
        linea()
        while True:
            id=int(input("Ingresar el ID del repuesto que desea eliminar: "))
            try:
                conexion=conectar()
                cursor=conexion.cursor()
                cursor.execute(""" delete from Repuestos where id_repuesto = ?""", (id,))
                conexion.commit()
                linea()
                print("El producto fue eliminado correctamente...")
                linea()
            except Exception as e:
                linea()
                print("Error al eliminar el repuesto:  ", e)
                linea()
            finally:
                conexion.close()
        

    def ejecutar_modificacion_repuesto(self,dato, nombre_columna, repuesto):
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            cursor.execute(f""" update repuestos set {nombre_columna}= ? where id_repuesto= ?""", (dato, repuesto))
            conexion.commit()
            linea()
            print("El respuesto se modificó correctamente...")
            linea()
        except Exception as e:
            linea()
            print(f"Error al modificar la la columna {nombre_columna}",e)
            linea()
        finally:
            conexion.close()
        

    def modificar_repuesto(self):
        linea()
        print("----MODIFICAR REPUESTO----")
        linea()
        while True:
            repuesto=int(input("Ingrsar el ID del repuesto que desea modificar:   "))
            print("--Atributos a modificar--")
            print ("1- Nombre")
            print ("2- Marca")
            print ("3- Stock")
            print ("4- Precio Unitario")
            opcion=int(input("Ingresar el numero del atributo que desea modificar:  "))
            dato=input("Ingresar el nuevo valor: ")
            columnas={"1":"Nombre", "2":"MArca","3":"Stock","4":"Precio Unitario"}
            if opcion in columnas:
                nombre_columna=columnas[opcion]
                self.ejecutar_modificacion_repuesto (dato, nombre_columna ,repuesto)
            else:
                print("opcion invalida")
            
        
    def listar_repuestos(self):
        linea()
        print("----LISTA DE REPUESTOS----")
        linea()
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            cursor.execute("""select * from Repuestos""")
            repuestos=cursor.fetchall()
            if not repuestos:
                print()
                print("No hay repuestos registrados")
                print()
                linea()
            else:
                for id_repuesto, nombre, stock, precio_unitario, marca, categoria in repuestos:
                    print()
                    print (f"Id: {id_repuesto} - Nombre: {nombre} - Stock: {stock} - Precio Unitario: {precio_unitario} - Marca:{marca} - Categoria:{categoria}")
                    linea()
        except Exception as e:
            print("Error al mostrar la lista de Respuestos",e)
        finally:
            conexion.close()

    

            

      

        