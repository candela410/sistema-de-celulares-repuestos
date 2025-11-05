from BD import tabla_pedidos
from Clase_Detalle import tabla_detalle_pedidos
from Clase_Proveedores import Proveedor 
from BD import conectar


class Pedido():
    def __init__(self, Id_pedidos,fecha_pedido, fecha_entrega, total,proveedor1):
        self.Id_pedido=Id_pedidos
        self.fecha_pedido=fecha_pedido
        self.fecha_entrega=fecha_entrega
        self.total=total
        self.proveedor1=Proveedor(proveedor1)
        tabla_pedidos()

    def agregar_pedido(self):
        conexion=conectar()
        cursor=conexion.cursor()
        fecha=input("Ingresar la fecha del pedido")
        fecha_entrega=input("Ingresar la fecha de entrega del pedido")
        

