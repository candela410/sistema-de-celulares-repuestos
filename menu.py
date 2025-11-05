from Clase_Proveedores import Proveedor
from Clase_Categorias import Categoria
from Clase_Marcas import Marca
from Clase_Repuestos import Repuesto
from Clase_Pedidos import Pedido
from Clase_Detalle import Detalle_pedido


def menu_principal():
    while True:
        print ("--SISTEMA DE REPARACIÓN--")
        print ("1-Repuestos")
        print ("2-Proveedores")
        print ("3-Estadisticas")
        print ("4-Salir")
        opcion=input("Elegir una opcion:  ")
        if opcion== 1:
            Repuestos()
        else: 
            if opcion==2:
                Proveedores()
            else:
                if opcion==3:
                    Estadisticas()
                else:
                    break



def Repuestos():
    rep=Repuesto()
    while True:
        print ("--REPUESTOS--")
        print ("1-Listar los repuestos")
        print ("2-Agregar un repuesto")
        print ("3-Eliminar un epuesto")
        print ("4-Modificar un repuesto")
        print ("5- Marcas")
        print ("6- Categoria")
        print ("7- Salir")
        opcion=input("Elegir una opción:  ")
        if opcion=="1":
            rep.listar_repuestos()
        else:
            if opcion=="2":
                rep.agregar_repuestos()
            else:
                if opcion=="3":
                    rep.eliminar_repuestos()
                else:
                    if opcion=="4":
                        rep.modificar_repuesto
                    else:
                        if opcion == "5":
                            Marcas()
                        else:
                            if opcion =="6":
                                Categorias()
                            else:
                                if opcion =="7":
                                    break
                                else:
                                    print("opcion invalida ")

def Marcas():
    marca= Marca()
    while True:
        print ("--MARCAS--")
        print ("1- Listar Marcas")
        print ("2- Agregar Marca")
        print ("3- Eliminar Marca")
        print ("4- Modificar Marca")
        print ("5- Salir")
        opcion=input("Elegir una opcion:  ")
        if opcion=="1":
            marca.mostrar_marcas()
        else:
            if opcion=="2":
                marca.agregar_marca()
            else:
                if opcion=="3":
                    marca.eliminar_marca()
                else:
                    if opcion=="4":
                        marca.modificar_marca()
                    else:
                        if opcion=="5":
                            break
                        else: 
                            print("opcion invalida")
        
def Categorias():
    categoria=Categoria()
    while True:
        print ("--CATEGORIAS--")
        print ("1-Agregar Categorias")
        print ("2-Eliminar ")
        print ("3-modificar")
        print ("4-listar categorias")
        print ("5-Salir")
        opcion=input("Elegir una opcion:  ")
        if opcion=="1":
            categoria.agregar_categoria()
        else:
            if opcion=="2":
                categoria.eliminar_categoria()
            else:
                if opcion=="3":
                    categoria.modificar_categoria()
                else:
                    if opcion=="4":
                        categoria.mostrar_categorias()
                    else:
                        if opcion=="5":
                            break
                        else:
                            print("Opcion Invalida")




def Proveedores():
    prov=Proveedor()
    while True:
        print("--PROVEEDORES--")
        print ("1- Listar un roveedor")
        print ("2- Agregar un proveedor")
        print ("3- Realizar un pedido")
        print ("4- Modificar un proveedor")
        print ("5- Salir")
        opcion=input("Elija una opcion: ")
        if opcion=="1":
            prov.mostrar_proveedores()
        else:
            if opcion=="2":
                prov.agregar_proveedor()
            else:
                if opcion=="3":
                    Pedidos()
                else:
                    if opcion=="4":
                        prov.modificar_proveedores()
                    else:
                        if opcion=="5":
                            break
                        else:
                            print("opcion invalida")

def Pedidos():
    while True:
        djee
        

def Estadisticas():
    print ("1- P")