import sqlite3

def conectar():
    return sqlite3.connect("tecnojuan.db")

# JOIN entre pedidos y proveedores
def consulta_1():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT Pedidos.id_pedido, Proveedores.nombre, Pedidos.total
    FROM Pedidos
    JOIN Proveedores ON Pedidos.id_prov = Proveedores.id_prov
    """)
    for fila in cursor.fetchall():
        print(fila)
    conn.close()

# GROUP BY: cantidad de repuestos por categoría
def consulta_2():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT Categorias.nombre, COUNT(Repuestos.id_rep) AS total_repuestos
    FROM Repuestos
    JOIN Categorias ON Repuestos.id_categoria = Categorias.id_categoria
    GROUP BY Categorias.nombre
    """)
    for fila in cursor.fetchall():
        print(fila)
    conn.close()

# Sumar el total de stock
def consulta_3():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(stock) FROM Repuestos")
    print("Stock total:", cursor.fetchone()[0])
    conn.close()

# Subconsulta: el repuesto más caro
def consulta_4():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT nombre, precio_unitario
    FROM Repuestos
    WHERE precio_unitario = (SELECT MAX(precio_unitario) FROM Repuestos)
    """)
    for fila in cursor.fetchall():
        print(fila)
    conn.close()
    