import sqlite3

def conectar():
    return sqlite3.connect("tecnojuan.db")

# Create
def agregar_proveedor():
    nombre = input("Nombre: ")
    direccion = input("Dirección: ")
    telefono = input("Teléfono: ")
    estado = input("Estado: ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Proveedores (nombre, direccion, telefono, estado) VALUES (?, ?, ?, ?)",
                   (nombre, direccion, telefono, estado))
    conn.commit()
    conn.close()
    print("Proveedor agregado correctamente.")

# Read
def mostrar_proveedores():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Proveedores")
    proveedores = cursor.fetchall()
    conn.close()

    for p in proveedores:
        print(p)

# Update
def actualizar_proveedor():
    id_prov = int(input("ID del proveedor a actualizar: "))
    nuevo_estado = input("Nuevo estado: ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("UPDATE Proveedores SET estado = ? WHERE id_prov = ?", (nuevo_estado, id_prov))
    conn.commit()
    conn.close()
    print("Proveedor actualizado correctamente.")

# Delete
def eliminar_proveedor():
    id_prov = int(input("ID del proveedor a eliminar: "))

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Proveedores WHERE id_prov = ?", (id_prov,))
    conn.commit()
    conn.close()
    print("Proveedor eliminado correctamente.")