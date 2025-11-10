from BD import conectar, linea, tablas, limpiar_pantalla, pausa

class Repuesto():
    def __init__(self,id_repuesto=None, nombre="", stock=0,precio_unitario=0.0,id_marca=None,id_categoria=None):
        self.id_repuesto=id_repuesto
        self.nombre=nombre
        self.stock=stock
        self.precio_unitario=precio_unitario
        self.marca=id_marca
        self.categoria=id_categoria
        tablas()
       
    
    def agregar_repuestos(self):
        limpiar_pantalla()
        while True:
            linea()
            print ("----AGREGAR REPUESTO----")
            linea()
            try:
                conexion=conectar()
                cursor=conexion.cursor()
                nombre=input("Ingrese el nombre del nuevo repuesto:  ").strip().lower()
                b=True
                while b==True:
                    stock=int(input("Ingresar su stock:  "))
                    if stock >= 0:
                        b=False
                    else: 
                        print("Stock incorrecto....")
                precio_unitario=float(input("Ingresar el precio unitario:   "))
                marca=input("Ingresar el nombre de la marca:  ").strip().lower()
                cursor.execute("select id_marca from Marcas where nombre= ?", (marca,))
                marca1=cursor.fetchone()
                id_marca=marca1[0]
                if not marca1:
                    linea()
                    print("La marca no se encuentra registrada")
                    linea()
                    break
                categoria=input("Ingresar el nombre de la categoria: ").strip().lower()
                cursor.execute("select id_categoria from Categorias where nombre= ?",(categoria,))
                categoria1=cursor.fetchone()
                id_categoria=categoria1[0]
                if not categoria1:
                    linea()
                    print("La categoria no se encuentra registrada")
                    linea()
                    break
                cursor.execute(""" insert into repuestos ( nombre, stock,precio_unitario,id_marca,id_categoria) values (?,?,?,?,?)""", (nombre, stock, precio_unitario, id_marca, id_categoria))
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
            pausa()
        

    def eliminar_repuestos(self):
        limpiar_pantalla()
        while True:
            linea()
            print("----ELIMINAR REPUESTO----")
            linea()
            try:
                nombre=input("Ingresar el nombre del repuesto que desea eliminar:  ").strip().lower()
                cursor.execute("select id_repuesto from Repuestos where nombre= ?",(nombre,))
                id=cursor.fetchone()
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
            linea()
            continuar=input("Si desea eliminar otro repuesto ingrese 1 sino 0:  ")
            linea()
            if continuar != '1':
                break
        pausa()
        

    

    def modificar_repuesto(self):
        limpiar_pantalla()
        linea()
        print("----MODIFICAR REPUESTO----")
        linea()
        while True:
            try:
                
                conexion=conectar()
                cursor=conexion.cursor()
                repuesto=input("Ingrsar el nombre del repuesto que desea modificar:  ").strip().lower()
                print("--Atributos a modificar--")
                print ("1- Nombre")
                print ("2- Marca")
                print ("3- Stock")
                print ("4- Precio Unitario")
                opcion=input("Ingresar el numero del atributo que desea modificar:  ")
                dato=input("Ingresar el nuevo valor: ")
                columnas={"1":"nombre", "2":"marca","3":"stock","4":"precio_unitario"}
                if opcion in columnas:
                    nombre_columna=columnas[opcion]
                    cursor.execute(f""" update repuestos set {nombre_columna}= ? where nombre= ?""", (dato, repuesto))
                    conexion.commit()
                    linea()
                    print("El respuesto se modificó correctamente...")
                    linea()
                else:
                    print("opcion invalida")
                linea()
                continuar=input("Si desea modificar otro repuesto ingrese 1 sino 0:  ")
                linea()
                if continuar != '1':
                    break
                pausa()
            except Exception as e:
                linea()
                print(f"Error al modificar la la columna {nombre_columna}",e)
                linea()
            finally:
                conexion.close()
            
        
    def listar_repuestos(self):
        limpiar_pantalla()
        try:
            linea()
            print("----LISTA DE REPUESTOS----")
            linea()
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
                    cursor.execute ("select nombre from Marcas where id_marca= ?",(marca,))
                    marca1=cursor.fetchone()
                    cursor.execute("select nombre from Categorias where id_categoria= ?", (categoria,))
                    categoria1=cursor.fetchone()
                    print()
                    print (f"Id: {id_repuesto} - Nombre: {nombre} - Stock: {stock} - Precio Unitario: {precio_unitario} - Marca:{marca1} - Categoria:{categoria1}")
                    linea()
        except Exception as e:
            print("Error al mostrar la lista de Respuestos",e)
        finally:
            conexion.close()
        pausa()

    

            
            

      

        