import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Configuración de la base de datos
db_config = {
    'user': 'dni',
    'password': 'MinuzaFea265/',
    'host': 'localhost',
    'database': 'water'
}

def buscar_pago(id_factura):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM pagos WHERE id_factura = %s"
        cursor.execute(query, (id_factura,))
        pago = cursor.fetchone()
        
        if pago:
            print(f"ID Pago: {pago['id_pago']}")
            print(f"ID Factura: {pago['id_factura']}")
            print(f"Fecha de Pago: {pago['fecha_pago']}")
            print(f"Monto: {pago['monto']}")
            print(f"Método de Pago: {pago['metodo_pago']}")
        else:
            print("No se encontró un pago con ese ID de factura.")
        
        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def buscar_pago_interfaz():
    def on_buscar_click():
        id_factura = entry_id_factura.get()
        if id_factura:
            buscar_pago(id_factura)
        else:
            messagebox.showwarning("Entrada inválida", "Por favor ingrese un ID de factura.")

    toplevel = tk.Toplevel(root)
    toplevel.title("Buscar Pago por ID Factura")

    label_id_factura = tk.Label(toplevel, text="ID Factura:")
    label_id_factura.pack(pady=5)
    
    entry_id_factura = tk.Entry(toplevel)
    entry_id_factura.pack(pady=5)
    
    btn_buscar = tk.Button(toplevel, text="Buscar", command=on_buscar_click)
    btn_buscar.pack(pady=5)

root = tk.Tk()
root.title("Sistema de Pagos")

btn_abrir_buscar = tk.Button(root, text="Buscar Pago por ID Factura", command=buscar_pago_interfaz)
btn_abrir_buscar.pack(pady=20)

root.mainloop()
