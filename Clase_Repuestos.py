from BD import tabla_repuestos
from Clase_Marcas import Marca
from Clase_Categorias import Categoria
from BD import conectar

class Repuesto():
    def __init__(self,Id_repuesto, nombre, stock,precio_unitario,marca,categoria):
        self.Id_repuesto=Id_repuesto
        self.nombre=nombre
        self.stock=stock
        self.precio_unitario=precio_unitario
        self.marca=marca
        self.categoria=categoria
        tabla_repuestos()
    
    def agregar_repuestos(self):
        conexion=conectar()
        cursor=conexion.cursor()
        nombre=input("Ingrese el nombre del nuevo repuesto")
        stock=int(input("Ingresar su stock"))
        precio_unitario=int(input("Ingresar "))
        marca=input("Ingresar el ID de la marca")
        categoria=int(input("Ingresar el ID de la categoria"))
        cursor.execute(""" insert into repuestos (nombre, stock,precio_unitario,marca,categoria) values (?,?,?,?,?)""", nombre, stock, precio_unitario, marca, categoria)
        conexion.commit()
        conexion.close ()
        print("Se agrego el repuesto a la BD")

    def eliminar_repuestos(self):
        conexion=conectar()
        cursor=conexion.cursor()
        id=int(input("Ingresar el ID del repuesto que desea eliminar: "))
        cursor.execute(""" delete from repuestos where id_repuesto= ?""", id)
        conexion.commit()
        conexion.close()
        print("El producto fue eliminado correctamente")

    def ejecutar_modificacion_repuesto(self,dato, nombre_columna, repuesto):
        conexion=conectar()
        cursor=conexion.cursor()
        cursor.execute(""" update repuestos set {nombre_columna}= ? where id_repuesto= ?""", dato, repuesto)
        conexion.commit()
        conexion.close()
        print("El respuesto se modificó correctamente")

    def modificar_repuesto(self):
        repuesto=int(input("Ingrsar el ID del repuesto que desea modificar. "))
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
        conexion=conectar()
        cursor=conexion.cursor()
        repuestos=list(cursor.fetchall())
        for id_repuesto, nombre, stock, precio_unitario in repuestos:
            print (f"Id: {id_repuesto} - Nombre: {nombre} - Stock: {stock} - Precio Unitario: {precio_unitario}")
        conexion.close()

    

            