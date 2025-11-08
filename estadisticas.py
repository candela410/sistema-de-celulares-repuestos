import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import os
import platform

DB = r"C:\Users\54387\Desktop\Pandas_estadisticas\tablas1.bd" 

def conectar():
    return sqlite3.connect(DB)

class Estadisticas:
    def __init__(self):
        self.conexion = conectar()

# ------------------ FUNCIONES DE INTERFAZ ------------------
    def limpiar_pantalla(self):
        os.system('cls' if platform.system() == 'Windows' else 'clear')

    def pausa(self):
        input("\nPresioná Enter para volver al menú...")
        self.limpiar_pantalla()     

#------------------------------------------------

    def proveedor_con_mas_pedidos(self):
        self.limpiar_pantalla()
        print("\nGenerando gráfico de pedidos por proveedor...")

        df = pd.DataFrame({
            "PROVEEDORES": ["Click Salta", "Tecnonauta", "Saltacelulares", "VmCell", "Mobile Express"],
            "Cantidad_Pedidos": [1.0, 0.8, 0.6, 0.4, 0.4]
        })

        plt.figure(figsize=(7, 5))
        plt.style.use("seaborn-v0_8-whitegrid")
        bars = plt.bar(
            df["PROVEEDORES"],
            df["Cantidad_Pedidos"],
            color="#000e51ff",  
            edgecolor="#33333300",
            alpha=0.9,
            width=0.6
        )

        plt.title("PROVEEDOR CON MAS PEDIDOS", fontsize=16, fontweight="bold", pad=15)
        plt.xlabel("PROVEEDORES", fontsize=12)
        plt.ylabel("Cantidad de pedidos", fontsize=12)
        plt.xticks(rotation=25, fontsize=11)
        plt.yticks(fontsize=11)


        for bar in bars:
            yval = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                yval + 0.03,
                f"{yval:.1f}",
                ha="center",
                va="bottom",
                fontsize=11,
                fontweight="bold"
            )

        plt.tight_layout()
        plt.grid(False)
        plt.show(block=True)
        print("\nGráfico generado correctamente.")
        self.pausa()


#----------------------------------------------------------

    def marcas_mas_pedidas(self):
        print("\nGenerando gráfico de marcas más pedidas...")


        df = pd.DataFrame({
            "MARCAS": ["Samsung", "Xiaomi", "Motorola", "TCL"],
            "Cantidad_Total": [12, 9, 6, 3]
        })
        plt.style.use('default')
        fig, ax = plt.subplots(figsize=(8,5), facecolor='white')
        ax.set_facecolor('white')

        plt.bar(df["MARCAS"], df["Cantidad_Total"], color= "#740202ff", alpha=0.85, edgecolor="black")

        plt.title("MARCAS MAS PEDIDAS", fontsize=16, fontweight="bold")
        plt.xlabel("MARCAS", fontsize=12)
        plt.ylabel("Cantidad pedida", fontsize=12)
        plt.xticks(rotation=10, fontsize=12)



        for i, v in enumerate(df["Cantidad_Total"]):
            plt.text(i, v + 0.3, str(v), ha="center", fontsize=10, fontweight="bold")

        plt.tight_layout()
        plt.show()
        plt.pause(0.1)
        print("\nGráfico generado correctamente.")
        self.pausa()


#-----------------------------------------------
    def proveedores_por_estado(self):
        query = """
        SELECT estado AS Estado, COUNT(*) AS Cantidad
        FROM Proveedores
        GROUP BY estado;
        """
        df = pd.read_sql_query(query, self.conexion)
        if df.empty:
            print("\n No hay datos para mostrar.")
            return
        print(df)
        

        colores = ["#740202ff", "#000e51ff"]  
        explode = [0.005, 0.1]
        labeldistance = 2.2
        wedges, texts, autotexts = plt.pie(
            df["Cantidad"],
            labels=df["Estado"],
            autopct="%1.1f%%",
            startangle = 140,
            colors=colores,
            explode = explode,
            shadow = True,
            wedgeprops = {"linewidth":2, "edgecolor": "black", "alpha": 0.95},
            textprops={"fontsize": 14, "fontweight": "bold", "color": "white"}  
            )
        for t in texts:
            t.set_color("black")
            t.set_fontsize(12)
            t.set_fontweight("bold")
  
        plt.gca().set_aspect(0.7)

        plt.title("ESTADO DE LOS PROVEEDORES", fontsize=16, fontweight="bold", pad = 15)
        plt.tight_layout()
        plt.show(block=False)
        plt.pause(0.1)
        print("\nGráfico generado correctamente.")
        self.pausa()

#-----------------------------------------------------------------------------------------
    def backup_y_restauracion(self):
        while True:
            os.system('cls')
            print("\n" + "="*50)
            print("      SISTEMA DE BACKUP Y RESTAURACION")
            print("="*50 + "\n")
            print("1- Exportar todas las tablas a CSV (Backup)")
            print("2- Restaurar tablas desde CSV (Recuperar)")
            print("3- Volver al menu principal\n")
            
            opcion = input("Elegí una opcion: ")

            if opcion == "1":
                os.system('cls')
                self.exportar_todas_csv()
            elif opcion == "2":
                os.system('cls')
                self.restaurar_desde_csv()
            elif opcion == "3":
                os.system('cls')
                print("\nVolviendo al menu principal...")
                break
            else:
                print("[!] Opcion invalida. Intente de nuevo.")
                self.pausa()

    # ---------------------- EXPORTAR CSV ----------------------
    def exportar_todas_csv(self):
        carpeta_backup = "backups"

        if not os.path.exists(carpeta_backup):
            os.mkdir(carpeta_backup)
            print("[i] Carpeta 'backups' creada automaticamente.")

        cursor = self.conexion.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = [t[0] for t in cursor.fetchall()]
        tablas = [t for t in tablas if t != "sqlite_sequence"]

        print("\n" + "-"*50)
        print("       INICIANDO BACKUP DE TABLAS...")
        print("-"*50 + "\n")

        tablas_exportadas = []

        for t in tablas:
            print(f"--- Exportando tabla '{t}' ---")
            df = pd.read_sql_query(f"SELECT * FROM {t}", self.conexion)
            if not df.empty:
                ruta_csv = os.path.join(carpeta_backup, f"{t}.csv")
                df.to_csv(ruta_csv, index=False, encoding="utf-8-sig")
                tablas_exportadas.append(t)
                print(f"[✔] Tabla '{t}' exportada correctamente a {ruta_csv}\n")
            else:
                print(f"[!] Tabla '{t}' vacia, no se exporto.\n")

        print("\n" + "="*50)
        print("        REPORTE FINAL DE BACKUP")
        print("="*50)
        for t in tablas_exportadas:
            print(f"   - {t}")
        print("[✔] Backup completado con exito")
        print("="*50 + "\n")
        self.pausa()
  

    # ---------------------- RESTAURAR CSV ----------------------
    def restaurar_desde_csv(self):
        carpeta_backup = "backups"

        if not os.path.exists(carpeta_backup):
            print("[✖] No existe la carpeta de backups. Exporta primero.")
            return

        cursor = self.conexion.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = [t[0] for t in cursor.fetchall() if t[0] != "sqlite_sequence"]

        print("\n" + "-"*50)
        print("       INICIANDO RESTAURACION DE TABLAS...")
        print("-"*50 + "\n")

        tablas_restauradas = []

        for t in tablas:
            print(f"--- Restaurando tabla '{t}' ---")
            archivo = os.path.join(carpeta_backup, f"{t}.csv")
            if os.path.exists(archivo):
                df = pd.read_csv(archivo)
                df.to_sql(t, self.conexion, if_exists="replace", index=False)
                tablas_restauradas.append(t)
                print(f"[✔] Tabla '{t}' restaurada correctamente\n")
            else:
                print(f"[!] No se encontro el archivo '{t}.csv'. Se omitira\n")

        self.conexion.commit()
        print("\n" + "="*50)
        print("       REPORTE FINAL DE RESTAURACION")
        print("="*50)
        for t in tablas_restauradas:
            print(f"   - {t}")
        print("[✔] Restauracion completada con exito")
        print("="*50 + "\n")
        self.pausa()

    # --------------------------------------------------------
    def estadisticas(self):
        while True:
            self.limpiar_pantalla()
            print("\n=== ESTADÍSTICAS DEL CONTROL DE STOCK ===")
            print("1- Proveedor con más pedidos")
            print("2- Marcas más pedidas")
            print("3- Estados de  los proveedores")
            print("4- Backup y Restauración")
            print("5- Salir")
            opcion = input("Elegí una opción: ")

            if opcion == "1":
                self.proveedor_con_mas_pedidos()
            elif opcion == "2":
                self.marcas_mas_pedidas()
            elif opcion == "3":
                self.proveedores_por_estado()
            elif opcion == "4":
                self.backup_y_restauracion()
            elif opcion == "5":
                self.cerrar_conexion()
                break
            else:
                print("Opción inválida.")
                self.pausa()

    def cerrar_conexion(self):
        self.conexion.close()


if __name__ == "__main__":
    est = Estadisticas()
    est.estadisticas()
