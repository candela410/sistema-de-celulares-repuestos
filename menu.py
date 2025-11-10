from Clase_Proveedores import Proveedor
from Clase_Categorias import Categoria
from Clase_Marcas import Marca
from Clase_Repuestos import Repuesto
from Clase_Pedidos import Pedido
from BD import linea, tablas, limpiar_pantalla, pausa 
from estadisticas123 import Estadisticas1
import os 


tablas()


def menu_principal():
    while True:
        limpiar_pantalla()
        linea()
        print ("----SISTEMA DE REPARACIÓN----")
        linea()
        print ("1- Repuestos")
        print ("2- Proveedores")
        print ("3- Estadisticas")
        print ("4- Backup y Restauración")
        print ("5- Salir")
        print()
        opcion=int(input("Elegir una opcion:  "))
        linea()
        if opcion== 1:
            Repuestos()
        elif opcion==2:
            Proveedores()
        elif opcion==3:     
            estadisticas()
        elif opcion==4:
            menu_backup_restauracion()
        elif opcion==5:
            print("Adios...")
            break
        else:
            print("Opcion invalida")
            pausa()

def Repuestos():
    rep=Repuesto()
    while True:
        limpiar_pantalla()
        limpiar_pantalla()
        print ("----REPUESTOS----")
        linea()
        print ("1- Listar los repuestos")
        print ("2- Agregar un repuesto")
        print ("3- Eliminar un repuesto")
        print ("4- Modificar un repuesto")
        print ("5- Marcas")
        print ("6- Categoria")
        print ("7- Salir")
        print()
        opcion=int(input("Elegir una opción:  "))
        linea()
        if opcion==1:
            limpiar_pantalla()
            rep.listar_repuestos()
            pausa()
        elif opcion==2:
            rep.agregar_repuestos()
        elif opcion==3:
            rep.eliminar_repuestos()
        elif opcion==4:
            rep.modificar_repuesto()
        elif opcion==5:
            Marcas()
        elif opcion==6:
            Categorias()
        elif opcion==7:
                break
        else:
            print("Opcion invalida...")
            pausa()

def Marcas():
    marca= Marca()
    while True:
        limpiar_pantalla()
        print ("----MARCAS----")
        linea()
        print ("1- Listar Marcas")
        print ("2- Agregar Marca")
        print ("3- Eliminar Marca")
        print ("4- Modificar Marca")
        print ("5- Salir")
        print()
        opcion=int(input("Elegir una opcion:  "))
        linea()
        if opcion==1:
            marca.listar_marca()
        elif opcion==2:
            marca.agregar_marca()
        elif opcion==3:
            marca.eliminar_marca()
        elif opcion==4:
            marca.modificar_marca()
        elif opcion==5:
            break
        else:
            print("Opción Invalida...")
            pausa()

                  
def Categorias():
    categoria=Categoria()
    while True:
        limpiar_pantalla()
        print ("----CATEGORIAS----")
        linea()
        print ("1- Agregar Categorias")
        print ("2- Eliminar ")
        print ("3- Modificar")
        print ("4- Listar categorias")
        print ("5- Salir")
        print()
        opcion=int(input("Elegir una opcion:  "))
        linea()
        if opcion==1:
            categoria.agregar_categoria()
        elif opcion==2:
            categoria.eliminar_categoria()
        elif opcion==3:
            categoria.modificar_categoria()
        elif opcion==4:
            categoria.mostrar_categorias()
        elif opcion==5:
            break
        else:
            print("Opcion Inavalida...")
            pausa()
            
def Proveedores():
    prov=Proveedor()
    while True:
        limpiar_pantalla()
        print("----PROVEEDORES----")
        linea()
        print ("1- Listar un proveedor")
        print ("2- Agregar un proveedor")
        print ("3- Realizar un pedido")
        print ("4- Modificar un proveedor")
        print ("5- Salir")
        print()
        opcion=int(input("Elija una opcion: "))
        linea()
        if opcion==1:
            prov.mostrar_proveedores()
        elif opcion==2:
            prov.agregar_proveedor()
        elif opcion==3:
            Pedidos()
        elif opcion==4:
            prov.modificar_proveedores()
        elif opcion==5:
            break
        else:
            print("Opción Invalida...")
            pausa()
           
def Pedidos():
    ped=Pedido()
    while True:
        limpiar_pantalla()
        print("----PEDIDOS----")
        linea()
        print("1- Realizar un pedido")
        print("2- Listar pedidos")
        print("3- Salir")
        print()
        opcion=int(input("Elija una opcion: "))
        linea()
        if opcion==1:
            ped.agregar_pedido()
        elif opcion==2:
            ped.listar_pedidos()
        elif opcion==3:
            break
        else:
            print("Opción Invalida...")
            pausa()
          

def estadisticas():
        est=Estadisticas1()
        while True:
            limpiar_pantalla()
            print("\n=== ESTADÍSTICAS DEL CONTROL DE STOCK ===")
            print("1- Proveedor con más pedidos")
            print("2- Marcas más pedidas")
            print("3- Estados de  los proveedores")
            print("4- Salir")
            opcion = int(input("Elegí una opción: "))

            if opcion == 1:
                est.proveedor_con_mas_pedidos()
            elif opcion == 2:
                est.marcas_mas_pedidas()
            elif opcion == 3:
                est.proveedores_por_estado()
            elif opcion == 4:
                est.cerrar_conexion()
                break
            else:
                print("Opción inválida.")
                pausa()


def menu_backup_restauracion():
        est1=Estadisticas1()
        while True:
            limpiar_pantalla()
            os.system('cls')
            print("\n" + "="*50)
            print("      SISTEMA DE BACKUP Y RESTAURACION   ")
            print("="*50 + "\n")
            print("1- Exportar todas las tablas a CSV (Backup)")
            print("2- Restaurar tablas desde CSV (Recuperar)")
            print("3- Volver al menú principal\n")
            
            opcion = int(input("Elegí una opción: "))

            if opcion == 1:
                os.system('cls')
                est1.exportar_todas_csv()
            elif opcion == 2:
                os.system('cls')
                est1.restaurar_desde_csv()
            elif opcion == 3:
                print("\nVolviendo al menú principal...")
                break
            else:
                print("Opción inválida. Intente de nuevo.")
                pausa()

if __name__=="__main__":

    menu_principal()
