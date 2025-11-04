import sqlite3

def conectar():
    return sqlite3.connect("tecnojuan.db")

def insertar_datos():
    conn = conectar()
    cursor = conn.cursor()

    # --- Proveedores 
    cursor.execute("INSERT INTO Proveedores (nombre, direccion, telefono, estado) VALUES ('Click Salta', 'Av. San Martín 767', '3874870102', 'Activo')")
    cursor.execute("INSERT INTO Proveedores (nombre, direccion, telefono, estado) VALUES ('Tecnonauta', 'Fray A. Güemes 330', '3872261426', 'Activo')")
    cursor.execute("INSERT INTO Proveedores (nombre, direccion, telefono, estado) VALUES ('VmCell', 'Dean Funes 254', '3875027067', 'Inactivo')")
    cursor.execute("INSERT INTO Proveedores (nombre, direccion, telefono, estado) VALUES ('Saltacelulares', 'Av. Jujuy 399', '3875223322', 'Activo')")
    cursor.execute("INSERT INTO Proveedores (nombre, direccion, telefono, estado) VALUES ('Celular Plus', 'Pellegrini 1010', '3875123490', 'Suspendido')")
    cursor.execute("INSERT INTO Proveedores (nombre, direccion, telefono, estado) VALUES ('Mobile Express', 'Caseros 545', '3875012356', 'Inactivo')")


    # --- Categorías 
    cursor.execute("INSERT INTO Categorias (nombre) VALUES ('Pantallas')")
    cursor.execute("INSERT INTO Categorias (nombre) VALUES ('Baterías')")
    cursor.execute("INSERT INTO Categorias (nombre) VALUES ('Cámaras')")
    cursor.execute("INSERT INTO Categorias (nombre) VALUES ('Cargadores')")

    # --- Marcas 
    cursor.execute("INSERT INTO Marcas (nombre) VALUES ('Samsung')")
    cursor.execute("INSERT INTO Marcas (nombre) VALUES ('Xiaomi')")
    cursor.execute("INSERT INTO Marcas (nombre) VALUES ('Motorola')")
    cursor.execute("INSERT INTO Marcas (nombre) VALUES ('TCL')")

    # --- Repuestos 
    cursor.execute("INSERT INTO Repuestos (nombre, id_categoria, id_marca, stock, precio_unitario) VALUES ('Pantalla Samsung Galaxy S23 Ultra', 1, 1, 10, 210000)")
    cursor.execute("INSERT INTO Repuestos (nombre, id_categoria, id_marca, stock, precio_unitario) VALUES ('Batería Xiaomi 14T Pro', 2, 2, 12, 46000)")
    cursor.execute("INSERT INTO Repuestos (nombre, id_categoria, id_marca, stock, precio_unitario) VALUES ('Pantalla Xiaomi Redmi Note 14 Pro', 1, 2, 9, 180000)")
    cursor.execute("INSERT INTO Repuestos (nombre, id_categoria, id_marca, stock, precio_unitario) VALUES ('Cámara Motorola Edge 50 Fusion', 3, 3, 5, 105000)")
    cursor.execute("INSERT INTO Repuestos (nombre, id_categoria, id_marca, stock, precio_unitario) VALUES ('Cargador TCL 50 SE 2024', 4, 4, 20, 11000)")
    cursor.execute("INSERT INTO Repuestos (nombre, id_categoria, id_marca, stock, precio_unitario) VALUES ('Pantalla Samsung Galaxy S24+', 1, 1, 6, 250000)")
    cursor.execute("INSERT INTO Repuestos (nombre, id_categoria, id_marca, stock, precio_unitario) VALUES ('Batería Motorola G85 2025', 2, 3, 14, 35000)")
    cursor.execute("INSERT INTO Repuestos (nombre, id_categoria, id_marca, stock, precio_unitario) VALUES ('Pantalla Xiaomi 15 2025', 1, 2, 7, 165000)")
    cursor.execute("INSERT INTO Repuestos (nombre, id_categoria, id_marca, stock, precio_unitario) VALUES ('Cámara Samsung Galaxy Z Flip6 2024', 3, 1, 4, 195000)")
    cursor.execute("INSERT INTO Repuestos (nombre, id_categoria, id_marca, stock, precio_unitario) VALUES ('Pantalla TCL 50 SE 2023', 1, 4, 10, 78000)")

    conn.commit()
    conn.close()
    print("Datos insertados correctamente.")

insertar_datos()

