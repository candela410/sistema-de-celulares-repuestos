import sqlite3
from datetime import datetime

def conectar():
    return sqlite3.connect(r"C:\Users\cande\OneDrive\Documentos\tablas1.bd")


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
    create table if not exists Categoria(
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
        id_marca integer,
        foreign key (Id_marca) references marcas(Id_marca),
        stock integer,
        precio_unitario integer
    )""")   

    conexion.commit()
    conexion.close()



def tabla_pedidos():
    conexion=conectar()
    cursor=conexion.cursor
    cursor.execute("""
    create table if not exists Pedidos(
        id_pedido integer primary key autoincrement,
        fecha_pedido datetime,
        fecha_entrega varchar (50),
        total integer not null
    )""")
    fecha_pedido =datetime.now()
    conexion.commit()
    conexion.close()
    
def tabla_detalle_pedidos():
    conexion=conectar()
    cursor=conexion.cursor()
    cursor.execute("""
    create table if not exists Detalle_pedidos(
        id_pedidos integer,
        id_repuestos integer,
        primary key (Id_pedidos,Id_repuestos),
        foreign key (Id_pedidos) references pedidos (Id_pedidos),
        foreign key (Id_repuestos) references repuestos (Id_repuestos),
        cantidad integer not null,
        precio_total integer not null
    )""")

    conexion.commit()
    conexion.close()