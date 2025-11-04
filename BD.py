import sqlite3

def conectar():
    return sqlite3.connect("tecnojuan.db")

def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Proveedores (
        id_prov INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        direccion TEXT,
        telefono TEXT,
        estado TEXT
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Categorias (
        id_categoria INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Marcas (
        id_marca INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Repuestos (
        id_rep INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        id_categoria INTEGER,
        id_marca INTEGER,
        stock INTEGER,
        precio_unitario REAL,
        FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria),
        FOREIGN KEY (id_marca) REFERENCES Marcas(id_marca)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Pedidos (
        id_pedido INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_pedido TEXT,
        fecha_entrega TEXT,
        total REAL,
        id_prov INTEGER,
        FOREIGN KEY (id_prov) REFERENCES Proveedores(id_prov)
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Detalle_Pedido (
        id_detalle INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pedido INTEGER,
        id_rep INTEGER,
        cantidad INTEGER,
        precio_total REAL,
        FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
        FOREIGN KEY (id_rep) REFERENCES Repuestos(id_rep)
    );
    """)

    conn.commit()
    conn.close()
    print("Base y tablas creadas correctamente.")
