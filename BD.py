import sqlite3
import os
import platform

def conectar():
    return sqlite3.connect("tablas1.db")


def tablas():
    conexion=conectar()
    cursor= conexion.cursor()
    cursor.execute("""
    create table if not exists Proveedores(
        id_proveedor integer primary key AUTOINCREMENT,
        nombre varchar(100) not null,
        telefono integer,
        direccion varchar(100),
        estado varchar(10)
    )""")

    cursor.execute("""
    create table if not exists Categorias(
        id_categoria integer primary key autoincrement,
        nombre varchar(100) not null
    )""")
    

    cursor.execute("""
    create table if not exists Marcas(
        id_marca integer primary key autoincrement, 
        nombre varchar(100)
    )""")


    cursor.execute("""
        create table if not exists Repuestos(
            id_repuesto integer primary key autoincrement,
            nombre varchar(100) not null,
            stock integer,
            precio_unitario real,
            id_marca integer,
            id_categoria integer,
            foreign key (id_categoria) references Categorias (id_categoria),
            foreign key (id_marca) references Marcas (id_marca)
    )""")   


    cursor.execute("""
    create table if not exists Pedidos(
        id_pedido integer primary key autoincrement,
        fecha_pedido datetime,
        fecha_entrega varchar (50),
        total integer not null,
        id_proveedor int,
        estado varchar(100),
        foreign key (id_proveedor) references Proveedores (id_proveedor)
    )""")
   

    cursor.execute("""
    create table if not exists Detalle_pedidos(
        id_pedido integer,
        id_repuesto integer,
        cantidad integer not null,
        precio_total integer,
        primary key (id_pedido,id_repuesto),
        foreign key (id_pedido) references Pedidos (id_pedido),
        foreign key (id_repuesto) references Repuestos (id_repuesto) 
    )""")

    conexion.commit()
    conexion.close()

def linea():
    ancho = os.get_terminal_size().columns
    print("=" * ancho)

def limpiar_pantalla():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def pausa():
    input("\nPresioná Enter para volver al menú...")
    limpiar_pantalla()     
