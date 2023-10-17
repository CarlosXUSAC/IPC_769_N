import tkinter as tk
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import hashlib
from tkinter import messagebox

class StudentPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel de Estudiante")
        self.root.geometry("600x300")
        self.root['bg'] = '#8C89D8'
        self.root.iconbitmap('Usac_logo.ico')

        self.labelX = tk.Label(self.root)
        self.labelX.grid(row=0, column=0, padx=20)
        self.labelX['bg'] = '#8C89D8'

        self.student_label = tk.Label(self.root, text="Panel de Estudiante")
        self.student_label.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
        self.student_label['bg'] = '#8C89D8'

        self.nombre_label = tk.Label(self.root, text="Nombre:")
        self.nombre_label.grid(row=1, column=1, padx=10, pady=10)
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.grid(row=1, column=2, padx=10, pady=10)

        self.apellido_label = tk.Label(self.root, text="Apellido:")
        self.apellido_label.grid(row=1, column=3, padx=10, pady=10)
        self.apellido_entry = tk.Entry(self.root)
        self.apellido_entry.grid(row=1, column=4, padx=10, pady=10)

        self.dpi_label = tk.Label(self.root, text="DPI:")
        self.dpi_label.grid(row=2, column=1, padx=10, pady=10)
        self.dpi_entry = tk.Entry(self.root)
        self.dpi_entry.grid(row=2, column=2, padx=10, pady=10)

        self.nacimiento_label = tk.Label(self.root, text="Nacimiento:")
        self.nacimiento_label.grid(row=2, column=3, padx=10, pady=10)
        self.nacimiento_entry = tk.Entry(self.root)
        self.nacimiento_entry.grid(row=2, column=4, padx=10, pady=10)

        self.telefono_label = tk.Label(self.root, text="Teléfono:")
        self.telefono_label.grid(row=3, column=1, padx=10, pady=10)
        self.telefono_entry = tk.Entry(self.root)
        self.telefono_entry.grid(row=3, column=2, padx=10, pady=10)

        self.usuario_label = tk.Label(self.root, text="Usuario:")
        self.usuario_label.grid(row=3, column=3, padx=10, pady=10)
        self.usuario_entry = tk.Entry(self.root)
        self.usuario_entry.grid(row=3, column=4, padx=10, pady=10)

        self.correo_label = tk.Label(self.root, text="Correo:")
        self.correo_label.grid(row=4, column=1, padx=10, pady=10)
        self.correo_entry = tk.Entry(self.root)
        self.correo_entry.grid(row=4, column=2, padx=10, pady=10)

        self.password_label = tk.Label(self.root, text="Contraseña:")
        self.password_label.grid(row=4, column=3, padx=10, pady=10)
        self.password_entry = tk.Entry(self.root)
        self.password_entry.grid(row=4, column=4, padx=10, pady=10)

        self.confirmar_label = tk.Label(self.root, text="Confirmar Contraseña:")
        self.confirmar_label.grid(row=5, column=3, padx=10, pady=10)
        self.confirmar_entry = tk.Entry(self.root)
        self.confirmar_entry.grid(row=5, column=4, padx=10, pady=10)

        self.register_button = tk.Button(self.root, text="Registrar", command=self.register)    #command=self.register
        self.register_button.grid(row=6, column=2, columnspan=2, padx=10, pady=10)

        self.view_courses_button = tk.Button(self.root, text="Ver Cursos", command=self.view_courses)
        self.view_courses_button.grid(row=6, column=3, columnspan=2, padx=10, pady=10)

        self.salir_button = tk.Button(self.root, text="Salir", command=self.logout)  #command=self.logout
        self.salir_button.grid(row=6, column=4, padx=10, pady=10)

    def show_message(self, message):
        messagebox.showinfo("Éxito", message)

    def prettify_xml(self, elem):
        """Devuelve una versión formateada del elemento XML como una cadena."""
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return "\n".join([line for line in reparsed.toprettyxml(indent="   ").split("\n") if line.strip()])

    def register(self):
        # Recopila los datos ingresados por el usuario
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        dpi = self.dpi_entry.get()
        nacimiento = self.nacimiento_entry.get()
        telefono = self.telefono_entry.get()
        usuario = self.usuario_entry.get()
        correo = self.correo_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirmar_entry.get()
    
        # Verifica que las contraseñas coincidan
        if password != confirm_password:
            self.show_message("Las contraseñas no coinciden.")
            return
    
        # Abre el archivo XML (o crea uno si no existe)
        try:
            tree = ET.parse("students.xml")
            root = tree.getroot()
        except FileNotFoundError:
            root = ET.Element("Students")
            tree = ET.ElementTree(root)
    
        # Verifica si el nombre de usuario ya existe en el archivo XML
        for student in root:
            existing_username = student.find("Usuario").text
            if existing_username == usuario:
                self.show_message("El nombre de usuario ya existe. Por favor, elija otro.")
                return
    
        # Encripta la contraseña antes de almacenarla
        password_hash = hashlib.sha256(password.encode()).hexdigest()
    
        # Crea un nuevo elemento XML para el estudiante
        student = ET.Element("Student")
        ET.SubElement(student, "Nombre").text = nombre
        ET.SubElement(student, "Apellido").text = apellido
        ET.SubElement(student, "DPI").text = dpi
        ET.SubElement(student, "Nacimiento").text = nacimiento
        ET.SubElement(student, "Telefono").text = telefono
        ET.SubElement(student, "Usuario").text = usuario
        ET.SubElement(student, "Correo").text = correo
        ET.SubElement(student, "Password").text = password_hash  # Almacena la contraseña encriptada
    
        # Agrega el elemento del estudiante a la estructura XML
        root.append(student)
    
        # Guarda los cambios en el archivo XML con formato y saltos de línea
        xml_str = self.prettify_xml(root)
        with open("students.xml", "w") as xml_file:
            xml_file.write(xml_str)
    
        # Mostrar un mensaje de éxito
        self.show_message("Datos registrados con éxito")
    
        # Limpiar los campos después de registrar
        self.nombre_entry.delete(0, tk.END)
        self.apellido_entry.delete(0, tk.END)
        self.dpi_entry.delete(0, tk.END)
        self.nacimiento_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.usuario_entry.delete(0, tk.END)
        self.correo_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.confirmar_entry.delete(0, tk.END)



    def view_courses(self):
        # Implementa la lógica para que el estudiante pueda ver los cursos disponibles aquí
        pass   

    def logout(self):
        # Implementa la lógica para cerrar sesión aquí
        pass

if __name__ == "__main__":
    root = tk.Tk()
    student_panel = StudentPanel(root)
    root.mainloop()
