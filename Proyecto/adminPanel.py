import tkinter as tk
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from tkinter import messagebox

class AdminPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel de Administrador")
        self.root.geometry("400x300")
        self.root['bg'] = '#66D773'
        self.root.iconbitmap('Usac_logo.ico')


        self.admin_label = tk.Label(self.root, text="Panel de Administrador")
        self.admin_label.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
        self.admin_label['bg'] = '#66D773'

        self.labelX = tk.Label(self.root)
        self.labelX.grid(row=0, column=0, padx=40)
        self.labelX['bg'] = '#66D773'

        self.register_professor_button = tk.Button(self.root, text="Registrar Profesor", command=self.register_professor)
        self.register_professor_button.grid(row=1, column=2, padx=10, pady=10)

        self.create_course_button = tk.Button(self.root, text="Crear Curso", command=self.create_course)
        self.create_course_button.grid(row=1, column=3, padx=10, pady=10)

        self.view_professors_button = tk.Button(self.root, text="Ver Profesores", command=self.view_professors)
        self.view_professors_button.grid(row=2, column=2, padx=10, pady=10)

        self.view_courses_button = tk.Button(self.root, text="Ver Cursos", command=self.view_courses)
        self.view_courses_button.grid(row=2, column=3, padx=10, pady=10)

        self.logout_button = tk.Button(self.root, text="Cerrar Sesión", command=self.logout)
        self.logout_button.grid(row=3, column=2, columnspan=2, padx=10, pady=10)

    def show_message(self, message):
        messagebox.showinfo("Éxito", message)

    def prettify_xml(self, elem):
        """Devuelve una versión formateada del elemento XML como una cadena."""
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return "\n".join([line for line in reparsed.toprettyxml(indent="   ").split("\n") if line.strip()])

    def register_professor(self):
        # Crear una nueva ventana para el registro de profesores
        register_professor_window = tk.Toplevel(self.root)
        register_professor_window.title("Registro de Profesor")
        register_professor_window.geometry("400x300")        
        register_professor_window.iconbitmap('Usac_logo.ico')

        # Agregar etiquetas y campos de entrada para Nombre, Apellido, DPI, Contraseña y Confirmación
        tk.Label(register_professor_window, text="Nombre").grid(row=0, column=0)
        name_entry = tk.Entry(register_professor_window)
        name_entry.grid(row=0, column=1)

        tk.Label(register_professor_window, text="Apellido").grid(row=1, column=0)
        last_name_entry = tk.Entry(register_professor_window)
        last_name_entry.grid(row=1, column=1)

        tk.Label(register_professor_window, text="DPI").grid(row=2, column=0)
        dpi_entry = tk.Entry(register_professor_window)
        dpi_entry.grid(row=2, column=1)

        tk.Label(register_professor_window, text="Contraseña").grid(row=3, column=0)
        password_entry = tk.Entry(register_professor_window, show="*")
        password_entry.grid(row=3, column=1)

        tk.Label(register_professor_window, text="Confirmación").grid(row=4, column=0)
        confirm_password_entry = tk.Entry(register_professor_window, show="*")
        confirm_password_entry.grid(row=4, column=1)        

        # Función para registrar al profesor
        def register():
            # Obtener los valores de los campos
            name = name_entry.get()
            last_name = last_name_entry.get()
            dpi = dpi_entry.get()
            password = password_entry.get()
            confirm_password = confirm_password_entry.get()
        
            # Realizar validaciones (por ejemplo, para asegurarse de que las contraseñas coincidan)
            if password != confirm_password:
                messagebox.showerror("Error", "Las contraseñas no coinciden")
                return
            
            # Abre el archivo XML (o crea uno si no existe)
            try:
                tree = ET.parse("professors.xml")
                root = tree.getroot()
            except FileNotFoundError:
                root = ET.Element("Professors")
                tree = ET.ElementTree(root)

            # Crea un nuevo elemento XML para el estudiante
            professor = ET.Element("Professor")
            ET.SubElement(professor, "Nombre").text = name
            ET.SubElement(professor, "Apellido").text = last_name
            ET.SubElement(professor, "DPI").text = dpi
            ET.SubElement(professor, "Password").text = password

            # Agrega el elemento del estudiante a la estructura XML
            root.append(professor)

           # Guarda los cambios en el archivo XML con formato y saltos de línea
            xml_str = self.prettify_xml(root)
            with open("professors.xml", "w") as xml_file:
                xml_file.write(xml_str)
        
            # Mostrar un mensaje de éxito
            self.show_message("Datos registrados con éxito")                            
                    
            # Limpiar los campos después de registrar
            self.nombre_entry.delete(0, tk.END)
            self.last_name_entry.delete(0, tk.END)
            self.dpi_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.confirm_password_entry.delete(0, tk.END)                   
            

        # Botón para registrar al profesor
        tk.Button(register_professor_window, text="Registrar", command=register).grid(row=5, column=0, columnspan=2)

        # Botón para cerrar la ventana de registro
        tk.Button(register_professor_window, text="Cerrar", command=register_professor_window.destroy).grid(row=6, column=0, columnspan=2)

    def create_course(self):
        # Implementa la lógica para crear cursos aquí
        pass

    def view_professors(self):
        # Implementa la lógica para ver la lista de profesores aquí
        pass

    def view_courses(self):
        # Implementa la lógica para ver la lista de cursos aquí
        pass

    def logout(self):
        # Implementa la lógica para cerrar sesión aquí
        pass

if __name__ == "__main__":
    root = tk.Tk()
    admin_panel = AdminPanel(root)
    root.mainloop()
