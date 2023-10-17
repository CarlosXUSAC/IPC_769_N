import tkinter as tk
import sqlite3


def iniciar_sesion():
    username = username_entry.get()
    password = password_entry.get()
    
    # Conecta a la base de datos
    connection = sqlite3.connect("usuarios.db")
    cursor = connection.cursor()
    
    # Consulta la base de datos para verificar las credenciales
    cursor.execute("SELECT tipo FROM usuarios WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()
    
    if result:
        tipo_usuario = result[0]
        if tipo_usuario == "Administrador":
            # Abre la vista de administración
            # Puedes llamar a otra función o abrir una nueva ventana aquí
            print("Vista de Administración")
        elif tipo_usuario == "Catedrático":
            # Abre la vista para catedráticos
            print("Vista para Catedráticos")
        elif tipo_usuario == "Alumno":
            # Abre la vista de alumno
            print("Vista de Alumno")
    else:
        print("Credenciales incorrectas")
    
    connection.close()

# Crear la ventana de inicio de sesión
root = tk.Tk()
root.title("Inicio de Sesión")
root.iconbitmap("Usac_logo.ico")
root['bg'] = '#74a5d6'

# Agregar un logo de la institución (reemplaza "logo.png" con tu propio archivo)
# Puedes usar la biblioteca Pillow para mostrar imágenes
from PIL import Image, ImageTk
logo = Image.open("logo-usac.png")
logo_photo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(root, image=logo_photo)
logo_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Entradas de usuario y contraseña
tk.Label(root, text="Usuario:", bg='#74a5d6').grid(row=1, column=0)
username_entry = tk.Entry(root)
username_entry.grid(row=1, column=1)


tk.Label(root, text="Contraseña:", bg='#74a5d6').grid(row=2, column=0)
password_entry = tk.Entry(root, show="*")  # Muestra asteriscos en lugar de caracteres
password_entry.grid(row=2, column=1)
# Botón de inicio de sesión
login_button = tk.Button(root, text="Iniciar Sesión", command=iniciar_sesion)
login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
