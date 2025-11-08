from BD import tabla_detalle_pedidos
from BD import conectar
from BD import linea

class Detalle_pedido():
    def __init__(self,id_pedido,id_repuesto,cantidad,precio_total):
        self.id_pedido=id_pedido
        self.id_repuesto=id_repuesto
        self.cantidad=cantidad
        self.precio_total=precio_total
        tabla_detalle_pedidos()


    def agregar_detalle(self, id_pedido):
        try:
            while True:
                id_repuesto = input("Ingrese ID del repuesto: ")
                cantidad = input("Ingrese cantidad: ")
                precio_total=0
                conexion = conectar()
                cursor = conexion.cursor()
                cursor.execute("""
                    INSERT INTO Detalle_Pedido (id_pedido, id_repuesto, cantidad, precio_total)
                    VALUES (?, ?, ?, ?)
                """, (id_pedido, id_repuesto, cantidad, precio_total))
                conexion.commit()
                continuar=int(input("Si desea agregar otro producto ingrese 1 sino 0 "))
                linea()
                if continuar != 1:
                    break
        except Exception as e:
            linea()
            print("Error al agregar el detalle:", e)
            linea()
        finally:
            conexion.close()

    def listar_detalles(self,id_pedido):
        linea()
        print("----DETALLES DEL PEDIDO----")
        linea()
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("""
                SELECT r.nombre, d.cantidad, d.precio_total, 
                INNER JOIN Pedidos p ON d.id_pedido = p.id_pedido
                INNER JOIN Repuestos r ON d.id_rep = r.id_rep
                where id_pedido= ?
            """, (id_pedido))
            detalles =list(cursor.fetchall())
            for nombre, cantidad, precio in detalles:
                print(f"Repuesto: {nombre} | Cantidad: {cantidad} | Total: ${precio} ")
        except Exception as e:
            print("Error al listar los detalles:", e)
        finally:
            conexion.close()

    def eliminar_detalle(self):
        print("\n=== Eliminar Detalle ===")
        id_detalle = input("Ingrese el ID del detalle que desea eliminar: ")

        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM detalle_Pedido WHERE id_detalle = ?", (id_detalle,))
            conexion.commit()
            print("Detalle eliminado correctamente.")
        except Exception as e:
            print("Error al eliminar el detalle:", e)
        finally:
            conexion.close()

    def modificar_detalle(self):
        print("\n=== Modificar Detalle ===")
        id_detalle = input("Ingrese el ID del detalle a modificar: ")
        nuevo_id_pedido = input("Nuevo ID del pedido: ")
        nuevo_id_repuesto = input("Nuevo ID del repuesto: ")
        nueva_cantidad = input("Nueva cantidad: ")
        nuevo_precio_total = input("Nuevo precio total: ")

        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("""
                UPDATE Detalle_Pedido
                SET id_pedido = ?, id_repuesto = ?, cantidad = ?, precio_total = ?
                WHERE id_detalle = ?
            """, (nuevo_id_pedido, nuevo_id_repuesto, nueva_cantidad, nuevo_precio_total, id_detalle))
            conexion.commit()
            print("Detalle modificado correctamente.")
        except Exception as e:
            print("Error al modificar el detalle:", e)
        finally:
            conexion.close()
    


    

