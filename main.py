from customtkinter import *
from tkinter import ttk
from PIL import Image
import mysql.connector
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import Menu
from PIL import Image, ImageDraw, ImageFont
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk
from customtkinter import CTk, CTkFrame, CTkToplevel

app = CTk()
app.title("Panel Control")
app.geometry("1500x768")
app.resizable(False, False)

set_appearance_mode("dark")

subtitulo = CTkFont("Arial", 15)

# DEFINICION DE LOS COLORES
color_azul = "#5dade2"
color_medio_guero = "#DAF7A6"
color_azul = "#2874a6"
color_medio_guero = "#DAF7A6"
color_amarillo = "#FFC300"
color_verde = "#138d75"
color_blanco = "#FDFEFE"
color_azul_contra = "#2471a3"
color_negro = "#17202A"


# DEFINIMOS LOS FRAMES A USAR EN LA APP
banner = CTkFrame(master=app, corner_radius=0, fg_color=color_azul)
centro = CTkFrame(master=app, corner_radius=0, fg_color=color_medio_guero)

def load_images():
    images = {
        "crear_usuario": CTkImage(dark_image=Image.open("icons/agregar-usuario.png"), size=(50, 50)),
        "agua": CTkImage(dark_image=Image.open("icons/agua.png"), size=(120, 60)),
        "metodo_de_pago": CTkImage(dark_image=Image.open("icons/metodo-de-pago.png"), size=(50, 50)),
        "ver_pagos": CTkImage(dark_image=Image.open("icons/buscar.png"), size=(50, 50)),
        "recibo": CTkImage(dark_image=Image.open("icons/recibo.png"), size=(50, 50)),
        "configuraciones": CTkImage(dark_image=Image.open("icons/configuraciones.png"), size=(50, 50)),
        "fondo" : CTkImage(dark_image=Image.open("icons/fondo.png"), size=(350,350)),
        "usuario" : CTkImage(dark_image=Image.open("icons/usuario.png"), size=(150,150)),
        "pago" : CTkImage(dark_image=Image.open("icons/pago.png"), size=(150,150)),
        "lupa" : CTkImage(dark_image=Image.open("icons/validando-billete.png"), size=(100,100))
    }
    return images

images = load_images()

# DEFINIMOS LAS ETIQUETAS CON IMAGEN
agua_logo_lb = CTkLabel(master=banner, text="", image=images["agua"])



#================================================FUNCIONES==================================
# Configuración de la base de datos
db_config = {
    'user': 'dni',
    'password': 'MinuzaFea265/',
    'host': 'localhost',
    'database': 'water'
}


def interfaz():
    crearUsuarioWindow = CTkToplevel(app)
    crearUsuarioWindow.title("Crear Persona")
    crearUsuarioWindow.geometry("1000x600")
    crearUsuarioWindow.resizable(False, False)
    
    imagenes = load_images()

    #Definimos los frames
    frame1 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color=color_negro)
    frame2 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color=color_azul)

    def getDatos():
        nombre = entName.get()
        direccion = entDireccion.get()
        telefono = entTelefono.get()
        email = entEmail.get()
        comunidad = entComunidad.get()
        cp = entCp.get()

        guardar_datos(nombre, direccion, telefono, email)

    def salir():
        crearUsuarioWindow.destroy()

    usuario = CTkLabel(master=frame2, text="", image=imagenes["usuario"])
    usuario.pack()
    fondo = CTkLabel(master=frame1, text="", image=imagenes["fondo"])
    fondo.place(
        relx=0.5,
        rely=0.5
    )

    lbName = CTkLabel(
        master=frame1,
        text="Nombre",
        text_color=color_blanco,
        font=subtitulo,
    )
    entName = CTkEntry(
        master=frame1,
        placeholder_text="Martin Antonio",
        width=240,
        height=20,
    )

    lbDireccion = CTkLabel(
        master=frame1,
        text="Direccion",
        text_color=color_blanco,
        font=subtitulo
    )
    entDireccion = CTkEntry(
        master=frame1,
        placeholder_text="Francisco #12",
        width=240,
        height=20
    )
    lbTelefono = CTkLabel(
        master=frame1,
        text="Celular",
        text_color=color_blanco,
        font=subtitulo
    )
    entTelefono = CTkEntry(
        master=frame1,
        placeholder_text="0909129856",
        width=240,
        height=20
    )
    lbEmail = CTkLabel(
        master=frame1,
        text="Email",
        text_color=color_blanco,
        font=subtitulo
        )
    entEmail = CTkEntry(
        master=frame1,
        placeholder_text="usuario@example.com",
        width=240,
        height=20
    )
    lbComunidad = CTkLabel(
        master=frame1,
        text="Comunidad",
        text_color=color_blanco,
        font=subtitulo
    )
    entComunidad = CTkEntry(
        master=frame1,
        placeholder_text="Loreto",
        width=240,
        height=20
    )
    lbCp = CTkLabel(
        master=frame1,
        text="C.P",
        font=subtitulo
    )
    entCp = CTkEntry(
        master=frame1,
        placeholder_text="98815",
        width=200,
        height=20
    )
    lbNota = CTkLabel(
        master=frame2,
        text="Notas",
        font=("Arial", 15)
    )
    nota = CTkTextbox(
        master=frame2,
        font=subtitulo,
        width=240,
        height=290
        )
    btnGuardar = CTkButton(
        master=frame1,
        text="Guardar",
        width=200,
        height=30,
        command=getDatos
    )
    btnSalir = CTkButton(
        master=frame1,
        text="Salir",
        width=200,
        height=30,
        command=salir
    )

    lbName.grid(
        row=0,
        column=0,
        pady=10,
        padx=10
    )
    entName.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )
    lbDireccion.grid(
        row=0,
        column=2,
        padx=10,
        pady=10
    )
    entDireccion.grid(
        row=0,
        column=3,
        padx=10,
        pady=10
    )
    lbTelefono.grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )
    entTelefono.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )
    lbEmail.grid(
        row=1,
        column=2,
        padx=10,
        pady=10
    )
    entEmail.grid(
        row=1,
        column=3,
        padx=10,
        pady=10
    )
    lbComunidad.grid(
        row=2,
        column=0,
        pady=10,
        padx=10
    )
    entComunidad.grid(
        row=2,
        column=1,
        padx=10,
        pady=10
    )
    lbCp.grid(
        row=2,
        column=2,
        padx=10,
        pady=10
    )
    entCp.grid(
        row=2,
        column=3,
        padx=10,
        pady=10
    )
    lbNota.place(
        relx=0.1,
        rely=0.4
    )
    nota.place(
        relx=0.1,
        rely=0.5
    )
    btnGuardar.place(
        relx=0.1,
        rely=0.9
    )
    btnSalir.place(
        relx=0.6,
        rely=0.9
    )

    frame1.place(
        relx=0.0,
        rely=0.0,
        relwidth=0.7,
        relheight=1.0
    )
    frame2.place(
    relx=0.7,
    rely=0.0,
    relwidth=0.3,
    relheight=1.0
    )



def verPagos():
    crearUsuarioWindow = CTkToplevel(app)
    crearUsuarioWindow.title("Ver Pago")
    crearUsuarioWindow.geometry("1000x600")
    crearUsuarioWindow.resizable(False, False)
    
    imagenes = load_images()

    # Definimos los frames
    frame1 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color="black")
    frame2 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color=color_azul)

    frame1.place(
        relx=0.0,
        rely=0.0,
        relwidth=0.7,
        relheight=1.0
    )
    frame2.place(
        relx=0.7,
        rely=0.0,
        relwidth=0.3,
        relheight=1.0
    )

    # Crear el Treeview en frame1
    tree = ttk.Treeview(frame1, columns=("id_pago", "id_factura", "fecha_pago", "monto", "metodo_pago"), show='headings')
    tree.heading("id_pago", text="ID Pago")
    tree.heading("id_factura", text="ID Factura")
    tree.heading("fecha_pago", text="Fecha de Pago")
    tree.heading("monto", text="Monto")
    tree.heading("metodo_pago", text="Método de Pago")
    
    # Ajustar el ancho de las columnas
    tree.column("id_pago", width=100)
    tree.column("id_factura", width=100)
    tree.column("fecha_pago", width=100)
    tree.column("monto", width=100)
    tree.column("metodo_pago", width=100)

    tree.pack(fill=tk.BOTH, expand=True)

    # Conectar a la base de datos y obtener los datos
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM pagos"
        cursor.execute(query)
        rows = cursor.fetchall()

        # Insertar los datos en el Treeview
        for row in rows:
            tree.insert("", "end", values=(row["id_pago"], row["id_factura"], row["fecha_pago"], row["monto"], row["metodo_pago"]))

        cursor.close()
        conn.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    crearUsuarioWindow.mainloop()



def crearAgua():
    crearUsuarioWindow = CTkToplevel(app)
    crearUsuarioWindow.title("Crear Pago")
    crearUsuarioWindow.geometry("1000x600")
    crearUsuarioWindow.resizable(False, False)
    
    imagenes = load_images()

    #Definimos los frames
    frame1 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color=color_negro)
    frame2 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color=color_azul)

    def getDatos():
        id_factura = entFactura.get()
        fecha_pago = entFecha.get()
        monto = entMonto.get()
        metodo_pago = metodoOpciones.get()

        insertar_pago(id_factura, fecha_pago, monto, metodo_pago)
        crearRecibo()        

    def salir():
        crearUsuarioWindow.destroy()

    recibo = CTkLabel(master=frame2, text="", image=imagenes["pago"])
    recibo.pack()
    fondo = CTkLabel(master=frame1, text="", image=imagenes["fondo"])
    fondo.place(
        relx=0.5,
        rely=0.5
    )

    lbFactira = CTkLabel(
        master=frame1,
        text="No Factura",
        text_color=color_blanco,
        font=subtitulo,
    )
    entFactura = CTkEntry(
        master=frame1,
        placeholder_text="01012021-0001",
        width=240,
        height=20,
    )

    lbFecha = CTkLabel(
        master=frame1,
        text="Fecha",
        text_color=color_blanco,
        font=subtitulo
    )
    entFecha = CTkEntry(
        master=frame1,
        placeholder_text="2024-09-21",
        width=240,
        height=20
    )
    lbMonto = CTkLabel(
        master=frame1,
        text="Monto $",
        text_color=color_blanco,
        font=subtitulo
    )
    entMonto = CTkEntry(
        master=frame1,
        placeholder_text="300.45",
        width=240,
        height=20
    )
    lbMetodo = CTkLabel(
        master=frame1,
        text="Metodo",
        text_color=color_blanco,
        font=subtitulo
        )
    metodoOpciones = CTkComboBox(
        master=frame1,
            values=[
                "Efectivo",
                "Tarjeta",
                "Transferencia"
            ]    
            )

    lbNota = CTkLabel(
        master=frame2,
        text="Notas",
        font=("Arial", 15)
    )
    nota = CTkTextbox(
        master=frame2,
        font=subtitulo,
        width=240,
        height=290
        )
    
    btnGuardar = CTkButton(
        master=frame1,
        text="Guardar",
        width=200,
        height=30,
        command=getDatos
    )
    btnSalir = CTkButton(
        master=frame1,
        text="Salir",
        width=200,
        height=30,
        command=salir
    )

    lbFactira.grid(
        row=0,
        column=0,
        pady=10,
        padx=10
    )
    entFactura.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )
    lbFecha.grid(
        row=0,
        column=2,
        padx=10,
        pady=10
    )
    entFecha.grid(
        row=0,
        column=3,
        padx=10,
        pady=10
    )
    lbMonto.grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )
    entMonto.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )
    lbMetodo.grid(
        row=1,
        column=2,
        padx=10,
        pady=10
    )
    metodoOpciones.grid(
        row=1,
        column=3,
        padx=10,
        pady=10
    )
    lbNota.place(
        relx=0.1,
        rely=0.4
    )
    nota.place(
        relx=0.1,
        rely=0.5
    )
    btnGuardar.place(
        relx=0.1,
        rely=0.9
    )
    btnSalir.place(
        relx=0.6,
        rely=0.9
    )

    frame1.place(
        relx=0.0,
        rely=0.0,
        relwidth=0.7,
        relheight=1.0
    )
    frame2.place(
    relx=0.7,
    rely=0.0,
    relwidth=0.3,
    relheight=1.0
    )


def insertar_pago(id_factura, fecha_pago, monto, metodo_pago):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="dni",
            password="MinuzaFea265/",
            database="water"
        )
        cursor = db.cursor()
        sql = "INSERT INTO pagos (id_factura, fecha_pago, monto, metodo_pago) VALUES (%s, %s, %s, %s)"
        val = (id_factura, fecha_pago, monto, metodo_pago)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()
        messagebox.showinfo("Éxito", "Datos guardados exitosamente")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al guardar los datos: {err}")


def guardar_datos(nombre, direccion, telefono, email):
    try:
        db = mysql.connector.connect(
            host="localhost",
            user="dni",
            password="MinuzaFea265/",
            database="water"
        )
        cursor = db.cursor()
        sql = "INSERT INTO Personas (nombre, direccion, telefono, email) VALUES (%s, %s, %s, %s)"
        val = (nombre, direccion, telefono, email)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()
        messagebox.showinfo("Éxito", "Datos guardados exitosamente")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al guardar los datos: {err}")


def fetch_data():
    # Conectar a la base de datos MySQL
    db = mysql.connector.connect(
        host="localhost",
        user="dni",
        password="MinuzaFea265/",
        database="water"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM Personas")
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data

def display_data(frame):
    # Create Treeview
    tree = ttk.Treeview(frame, columns=("ID", "Nombre", "Dirección", "Teléfono", "Email", "Fecha de Registro"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Dirección", text="Dirección")
    tree.heading("Teléfono", text="Teléfono")
    tree.heading("Email", text="Email")
    tree.heading("Fecha de Registro", text="Fecha de Registro")

    # Insert data into Treeview
    def refresh_data():
        for i in tree.get_children():
            tree.delete(i)
        data = fetch_data()
        for row in data:
            tree.insert("", "end", values=row)
    
    refresh_data()

    # Add right-click menu
    def do_popup(event):
        try:
            popup.tk_popup(event.x_root, event.y_root, 0)
        finally:
            popup.grab_release()
    
    popup = Menu(tree, tearoff=0)
    popup.add_command(label="Actualizar", command=refresh_data)
    
    tree.bind("<Button-3>", do_popup)
    
    # Configure Treeview layout
    tree.pack(expand=True, fill='both')


def crearRecibo():
    crearUsuarioWindow = CTkToplevel(app)
    crearUsuarioWindow.title("Crear Recibo")
    crearUsuarioWindow.geometry("700x300")
    crearUsuarioWindow.resizable(False, False)

    imagenes = load_images()

    #Definimos los frames
    frame1 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color=color_negro)
    frame2 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color=color_azul)

    def generarRecibo():
        id_factura = entFactura.get() 
        generar_recibo(id_factura)

    usuario = CTkLabel(master=frame2, text="", image=imagenes["lupa"])
    fondo = CTkLabel(master=frame1, text="", image=imagenes["fondo"])
    fondo.place(
        relx=0.3,
        rely=0.3
    )

    btnGenerarPago = CTkButton(
        master=frame1,
        text="Crear Pago",
        width=200,
        height=20,
        command=generarRecibo
    )

    lbIdFactura = CTkLabel(
        master=frame1,
        text="ID Factura",
        text_color=color_blanco,
        font=subtitulo
    )
    entFactura = CTkEntry(
        master=frame1,
        placeholder_text="9010294",
        width=340,
        height=20
    )
    lbIdFactura.grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )
    entFactura.grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )
    btnGenerarPago.place(
        relx=0.1,
        rely=0.9
    )


    usuario.place(
        relx=0.3,
        rely=0.3
    )
    frame1.place(
        relx=0.0,
        rely=0.0,
        relwidth=0.7,
        relheight=1.0
    )
    frame2.place(
    relx=0.7,
    rely=0.0,
    relwidth=0.3,
    relheight=1.0
    )
    crearUsuarioWindow.mainloop() 


def generar_recibo(id_factura):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM pagos WHERE id_factura = %s"
        cursor.execute(query, (id_factura,))
        pago = cursor.fetchone()

        if pago:
            # Datos del pago
            id_pago = pago['id_pago']
            id_factura = pago['id_factura']
            fecha_pago = pago['fecha_pago'].strftime('%d-%m-%Y')
            monto = pago['monto']
            metodo_pago = pago['metodo_pago']

            # Crear imagen de recibo más grande
            img = Image.new('RGB', (600, 400), color='white')
            d = ImageDraw.Draw(img)
            font = ImageFont.truetype('arial.ttf', 24)
            font_small = ImageFont.truetype('arial.ttf', 18)

            # Logo (reemplaza 'logo.png' por el nombre de tu archivo de logo)
            logo = Image.open('icons/agua.png')
            logo = logo.resize((150, 150))  # Redimensionar el logo si es necesario
            img.paste(logo, (20, 20))

            # Texto del recibo
            y_text = 180  # Posición Y inicial para el texto
            d.text((20, y_text), f"Recibo de Pago", font=font, fill='black')
            y_text += 40
            d.text((20, y_text), f"ID Pago: {id_pago}", font=font_small, fill='black')
            y_text += 30
            d.text((20, y_text), f"ID Factura: {id_factura}", font=font_small, fill='black')
            y_text += 30
            d.text((20, y_text), f"Fecha de Pago: {fecha_pago}", font=font_small, fill='black')
            y_text += 30
            d.text((20, y_text), f"Monto: {monto} MX", font=font_small, fill='black')
            y_text += 30
            d.text((20, y_text), f"Método de Pago: {metodo_pago}", font=font_small, fill='black')

            # Guardar la imagen como un archivo
            img.save(f"recibo_{id_factura}.png")
            print(f"Recibo generado: recibo_{id_factura}.png")

        else:
            print("No se encontró un pago con ese ID de factura.")

        cursor.close()
        conn.close()

    except Error as e:
        print(f"Error al conectar con MySQL: {e}")
    except IOError as e:
        print(f"Error al abrir el archivo de logo: {e}")


# DEFINIMOS LOS BOTONES DE ACCION DENTRO DEL BANNER
crear_usuarioBtn = CTkButton(
    master=banner,
    text="Crear Persona",
    image=images["crear_usuario"],
    command=interfaz
)
crear_pago_btn = CTkButton(
    master=banner,
    text="Crear Pago",
    image=images["metodo_de_pago"],
    command=crearAgua
)

ver_pago_btn = CTkButton(
    master=banner,
    text="Ver Pagos",
    image=images["ver_pagos"],
    command=verPagos
)

crear_recibo_btn = CTkButton(
    master=banner,
    text="Crear Recibo",
    image=images["recibo"],
    command=crearRecibo
)

configuracion = CTkButton(
    master=banner,
    text="Ajustes",
    image=images["configuraciones"]
)

# DEFINIMOS LAS POSICIONES DE LOS WIDGETS
banner.place(
    relx=0.0,
    rely=0.0,
    relwidth=1.0,
    relheight=0.1
)
centro.place(
    relx=0.1,
    rely=0.2,
    relwidth=0.8,
    relheight=0.7
)

agua_logo_lb.place(
    relx=0.0,
    rely=0.1
)

crear_usuarioBtn.place(
    relx=0.1,
    rely=0.1
)
crear_pago_btn.place(
    relx=0.3,
    rely=0.1
)
ver_pago_btn.place(
    relx=0.5,
    rely=0.1
)
crear_recibo_btn.place(
    relx=0.7,
    rely=0.1
)
configuracion.place(
    relx=0.9,
    rely=0.1
)

# Mostrar datos en el frame "centro"
display_data(centro)

app.mainloop()
