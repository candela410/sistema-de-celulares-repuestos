import 
class Proveedores:
    def __init__(self, Id_proveedor, prov_nombre, Telefono, Direccion, Estado):
        self.__Id_proveedor=Id_proveedor
        self.prov_nombre=prov_nombre
        self.Telefono=Telefono
        self.Direccion=Direccion
        self.Estado=Estado


    def get_Id_proveedor(self):
        return self.__Id_proveedor
   
class Pedidos:
    def __init__ (self, Id_pedido, Fecha_pedido, Fecha_entrega, Total):
        self.Id_pedido=Id_pedido
        self.Fecha_pedido=Fecha_pedido
        self.Fecha_entrega=Fecha_entrega
        self.Total=Total


class Repuestos:
    def __init__ (self, Id_repuestos, rep_nombre, stock, precio_unitario):
        self.Id_pedido=Id_repuestos
        self.rep_nombre=rep_nombre
        self.stock=stock
        self.precio_unitario=precio_unitario

class Categoria():
    def __init__(self, id_categoria, nombre):
        self.__id_categoria=id_categoria
        self.nombre=nombre

class Marca():
     def __init__(self, id_marca, nombre,repuesto):
         self.id_marca=id_marca
         self.nombre=nombre
         self.repuesto=repuesto
    
    def
    
