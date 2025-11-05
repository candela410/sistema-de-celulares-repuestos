from BD import tabla_detalle_pedidos

class Detalle_pedido():
    def __init__(self,Id_pedido,Id_repuesto,cantidad,precio_total):
        self.Id_pedido=Id_pedido
        self.Id_repuesto=Id_repuesto
        self.cantidad=cantidad
        self.precio_total=precio_total
        self.tabla_detalle_pedidos()
