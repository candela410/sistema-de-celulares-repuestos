from Clase_Detalle import Detalle_pedido
from Clase_Proveedores import Proveedor 
from BD import conectar, linea, tablas, limpiar_pantalla, pausa 
from datetime import datetime

class Pedido():
    def __init__(self, id_pedidos=None,fecha_pedido=None, fecha_entrega=None, total=0,id_proveedor=None):
        self.id_pedido=id_pedidos
        self.fecha_pedido=fecha_pedido
        self.fecha_entrega=fecha_entrega
        self.total=total
        self.proveedor1=Proveedor(id_proveedor)
        tablas()
     

    def agregar_pedido(self):
        limpiar_pantalla()
        linea()
        print("----REALIZAR PEDIDO----")
        linea()
           
        while True:
            
            try:
                conexion=conectar()
                cursor=conexion.cursor()
                cursor.execute("""select id_proveedor, nombre from Proveedores where estado="Activo" """)
                proveedores=cursor.fetchall()
                if not proveedores:
                    print()
                    print("No hay proveedores registrados")
                    print()
                else:
                    print("----PROVEEDORES DISPONIBLES----")
                    for id, nombre in proveedores:
                        print(f"ID: {id} - Nombre: {nombre}")
                    id_prov=int(input("Ingrese el Id del proveedor: "))
                    fecha_pedido=datetime.now().strftime("%Y-%m-%d")
                    cursor.execute("""insert into Pedidos(fecha_pedido,fecha_entrega, total, id_proveedor,estado )
                                values (?,null,0,?,"Pendiente")""",(fecha_pedido,id_prov))
                    id_pedido=cursor.lastrowid
                    conexion.commit()
                    cursor.execute(""" select id_repuesto, nombre from Repuestos""")
                    repuestos=cursor.fetchall()
                    print("----REPUESTOS ----")
                    for id, nombre in repuestos:
                        print (f"ID: {id} - Nombre: {nombre}")
                    det=Detalle_pedido()
                    det.agregar_detalle(id_pedido)
                    print()
                    print("Pedido realizado correctamente....")
            except Exception as e:
                print("Error al realizar el pedido", e)
            finally:
                conexion.close()
            continuar=int(input("Si desea agregar otro pedido ingrese 1 sino 0 "))
            linea()
            if continuar != 1:
                break
        pausa()
            
        

    
    def listar_pedidos(self):
        limpiar_pantalla()
        linea()
        print("----LISTA DE PEDIDOS----")
        linea()
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Pedidos")
            pedidos = list(cursor.fetchall())

            if not pedidos:
                print()
                print("No hay pedidos registrados.")
                print()
            else:
                for p in pedidos:
                    print()
                    print(f"ID: {p[0]} | Fecha Pedido: {p[1]} | Fecha Entrega: {p[2]} | Total: ${p[3]} | ID Proveedor: {p[4]}")
                    linea()
                    det=Detalle_pedido()
                    det.listar_detalles(p[0])
                    print("-" * 50)

        except Exception as e:
            linea()
            print("Error al listar los pedidos:", e)
            linea()
        finally:
            conexion.close()
        pausa()



        



        


    



