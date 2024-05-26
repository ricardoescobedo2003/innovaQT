from customtkinter import *
from tkinter import ttk
from PIL import Image
import mysql.connector
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import Menu


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
        "fondo" : CTkImage(dark_image=Image.open("icons/fondo.png"), size=(250,250)),
        "usuario" : CTkImage(dark_image=Image.open("icons/usuario.png"), size=(150,150))
    }
    return images

images = load_images()

# DEFINIMOS LAS ETIQUETAS CON IMAGEN
agua_logo_lb = CTkLabel(master=banner, text="", image=images["agua"])



#================================================FUNCIONES==================================
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
        app.destroy()

    usuario = CTkLabel(master=frame2, text="", image=imagenes["usuario"])
    usuario.pack()
    fondo = CTkLabel(master=frame1, text="", image=imagenes["fondo"])
    fondo.place(
        relx=0.7,
        rely=0.6
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
    image=images["metodo_de_pago"]
)

ver_pago_btn = CTkButton(
    master=banner,
    text="Ver Pagos",
    image=images["ver_pagos"]
)

crear_recibo_btn = CTkButton(
    master=banner,
    text="Crear Recibo",
    image=images["recibo"]
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
