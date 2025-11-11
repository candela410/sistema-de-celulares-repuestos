import pandas as pd
import matplotlib.pyplot as plt
import os

from BD import conectar, limpiar_pantalla, pausa 


class Estadisticas1:
    def __init__(self):
        self.conexion = conectar()

    def cerrar_conexion(self):
        self.conexion.close()


    def proveedor_con_mas_pedidos(self):
        limpiar_pantalla()
        print("\nGenerando gráfico de pedidos por proveedor (DINÁMICO)...")

        query = """
            SELECT pr.nombre AS PROVEEDORES, COUNT(p.id_pedido) AS Cantidad_Pedidos
            FROM Proveedores pr
            LEFT JOIN Pedidos p ON pr.id_proveedor = p.id_proveedor
            GROUP BY pr.nombre
            ORDER BY Cantidad_Pedidos DESC
        """
        df = pd.read_sql_query(query, self.conexion)

        if df.empty or df['Cantidad_Pedidos'].sum() == 0:
            print("\n[i] No hay pedidos cargados aún. Agregá uno para ver las estadísticas.")
            pausa()
            return

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

        plt.title("PROVEEDOR CON MÁS PEDIDOS", fontsize=16, fontweight="bold", pad=15)
        plt.xlabel("PROVEEDORES", fontsize=12)
        plt.ylabel("Cantidad de pedidos", fontsize=12)
        plt.xticks(rotation=25, fontsize=11)
        plt.yticks(fontsize=11)

        for bar in bars:
            yval = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2,
                yval + max(df["Cantidad_Pedidos"].max() * 0.03, 0.05),
                f"{yval:.0f}",
                ha="center",
                va="bottom",
                fontsize=11,
                fontweight="bold"
            )

        plt.tight_layout()
        plt.grid(False)
        plt.show(block=True)
        print("\nGráfico generado correctamente.")
        pausa()


    def marcas_mas_pedidas(self):
        limpiar_pantalla()
        print("\nGenerando gráfico de marcas más pedidas (DINÁMICO)...")

        query = """
        SELECT m.nombre AS MARCAS, SUM(dp.cantidad) AS Cantidad_Total
        FROM Detalle_pedidos dp
        JOIN Repuestos r ON dp.id_repuesto = r.id_repuesto
        JOIN Marcas m ON r.id_marca = m.id_marca
        GROUP BY m.nombre
        ORDER BY Cantidad_Total DESC
        """
        df = pd.read_sql_query(query, self.conexion)

        if df.empty or df['Cantidad_Total'].sum() == 0:
            print("\n[i] No hay ítems de pedidos registrados aún. Cargá un pedido para ver las marcas más pedidas.")
            pausa()
            return

        plt.style.use('default')
        fig, ax = plt.subplots(figsize=(8,5), facecolor='white')
        ax.set_facecolor('white')

        plt.bar(df["MARCAS"], df["Cantidad_Total"], color= "#740202ff", alpha=0.85, edgecolor="black")

        plt.title("MARCAS MÁS PEDIDAS", fontsize=16, fontweight="bold")
        plt.xlabel("MARCAS", fontsize=12)
        plt.ylabel("Cantidad pedida", fontsize=12)
        plt.xticks(rotation=10, fontsize=12)

        for i, v in enumerate(df["Cantidad_Total"]):
            plt.text(i, v + 0.3, str(v), ha="center", fontsize=10, fontweight="bold")

        plt.tight_layout()
        plt.show(block=True)
        print("\nGráfico generado correctamente.")
        pausa()


    def proveedores_por_estado(self):
        limpiar_pantalla()
        print("\nGenerando gráfico de estado de proveedores (DINÁMICO)...")
        
        query = """
        SELECT estado AS Estado, COUNT(*) AS Cantidad
        FROM Proveedores
        GROUP BY estado;
        """
        df = pd.read_sql_query(query, self.conexion)
        
        if df.empty:
            print("\n[i] No hay proveedores cargados aún. Agregá alguno para ver el gráfico de estados.")
            pausa()
            return
        
        colores = ["#740202ff", "#000e51ff"]  
        explode = [0.005, 0.1]
        
        num_estados = len(df)
        colores_finales = colores[:num_estados]
        explode_final = explode[:num_estados]
        
        plt.figure(figsize=(7, 7))
        
        wedges, texts, autotexts = plt.pie(
            df["Cantidad"],
            labels=df["Estado"],
            autopct="%1.1f%%",
            startangle=140,
            colors=colores_finales,
            explode=explode_final,
            shadow=True,
            wedgeprops={"linewidth":2, "edgecolor":"black", "alpha":0.95},
            textprops={"fontsize":14, "fontweight":"bold", "color":"white"}  
        )
            
        for t in texts:
            t.set_color("black")
            t.set_fontsize(12)
            t.set_fontweight("bold")
  
        plt.gca().set_aspect(0.7)
        plt.title("ESTADO DE LOS PROVEEDORES", fontsize=16, fontweight="bold", pad=15)
        plt.tight_layout()
        plt.show(block=True)
        print("\nGráfico generado correctamente.")
        pausa()



    def exportar_todas_csv(self):
        carpeta_backup = "backups"
        if not os.path.exists(carpeta_backup):
            os.mkdir(carpeta_backup)
            print("[i] Carpeta 'backups' creada automáticamente.")

        cursor = self.conexion.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = [t[0] for t in cursor.fetchall() if t[0] != "sqlite_sequence"]

        print("\n" + "-"*50)
        print("       INICIANDO BACKUP DE TABLAS...")
        print("-"*50 + "\n")

        for t in tablas:
            print(f"--- Exportando tabla '{t}' ---")
            df = pd.read_sql_query(f"SELECT * FROM {t}", self.conexion)
            if not df.empty:
                ruta_csv = os.path.join(carpeta_backup, f"{t}.csv")
                df.to_csv(ruta_csv, index=False, encoding="utf-8-sig")
                print(f"[✔] Tabla '{t}' exportada correctamente a {ruta_csv}\n")
            else:
                print(f"[!] Tabla '{t}' vacía, no se exportó.\n")

        print("[✔] Backup completado con éxito.")
        pausa()

    def restaurar_desde_csv(self):
        carpeta_backup = "backups"
        if not os.path.exists(carpeta_backup):
            print("[✖] No existe la carpeta de backups. Exportá primero.")
            return

        cursor = self.conexion.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tablas = [t[0] for t in cursor.fetchall() if t[0] != "sqlite_sequence"]

        print("\n" + "-"*50)
        print("       INICIANDO RESTAURACION DE TABLAS...")
        print("-"*50 + "\n")

        for t in tablas:
            print(f"--- Restaurando tabla '{t}' ---")
            archivo = os.path.join(carpeta_backup, f"{t}.csv")
            if os.path.exists(archivo):
                try:
                    df = pd.read_csv(archivo)
                    df.to_sql(t, self.conexion, if_exists="replace", index=False)
                    print(f"[✔] Tabla '{t}' restaurada correctamente\n")
                except Exception as e:
                    print(f"[✖] ERROR al leer/restaurar '{t}.csv': {e}\n")
            else:
                print(f"[!] No se encontró '{t}.csv'. Se omite.\n")

        self.conexion.commit()
        print("[✔] Restauración completada con éxito.")
        pausa()

