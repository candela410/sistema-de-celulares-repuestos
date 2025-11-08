import sqlite3
from datetime import datetime
import os

def conectar():
    return sqlite3.connect(r"C:\Users\cande\OneDrive\Documentos\tablas1.db")


def tabla_proveedores():
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

    conexion.commit()
    conexion.close()

def tabla_categorias():
    conexion=conectar()
    cursor= conexion.cursor()
    cursor.execute("""
    create table if not exists Categorias(
        id_categoria integer primary key autoincrement,
        nombre varchar(100) not null
    )""")
    
    conexion.commit()
    conexion.close()

def tabla_marcas():
    conexion=conectar()
    cursor=conexion.cursor()
    cursor.execute("""
    create table if not exists Marcas(
        id_marca integer primary key autoincrement, 
        nombre varchar(100)
    )""")

    conexion.commit()
    conexion.close()

def tabla_repuestos():
    conexion=conectar()
    cursor=conexion.cursor()
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

    conexion.commit()
    conexion.close()



def tabla_pedidos():
    conexion=conectar()
    cursor=conexion.cursor()
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
    fecha_pedido =datetime.now()
    conexion.commit()
    conexion.close()
    
def tabla_detalle_pedidos():
    conexion=conectar()
    cursor=conexion.cursor()
    cursor.execute("""
    create table if not exists Detalle_pedidos(
        id_pedido integer,
        id_repuesto integer,
        primary key (id_pedido,id_repuesto),
        foreign key (id_pedido) references Pedidos (id_pedidos),
        foreign key (id_repuesto) references Repuestos (id_repuesto),
        cantidad integer not null,
        precio_total integer not null
    )""")

    conexion.commit()
    conexion.close()

def linea():
    ancho = os.get_terminal_size().columns
    print("=" * ancho)