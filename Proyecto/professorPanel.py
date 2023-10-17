import tkinter as tk
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
import hashlib
from tkinter import messagebox

class ProfessorPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Catedraticos")
        self.root.geometry("600x300")
        self.root['bg'] = '#D8B175'
        self.root.iconbitmap('Usac_logo.ico')

        self.labelX = tk.Label(self.root)
        self.labelX.grid(row=0, column=0, padx=20)
        self.labelX['bg'] = '#D8B175'

        self.professor_label = tk.Label(self.root)
        self.professor_label.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
        self.professor_label['bg'] = '#D8B175'

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

        self.password_label = tk.Label(self.root, text="Contraseña:")
        self.password_label.grid(row=2, column=3, padx=10, pady=10)
        self.password_entry = tk.Entry(self.root)
        self.password_entry.grid(row=2, column=4, padx=10, pady=10)

        self.confirmar_label = tk.Label(self.root, text="Confirmar Contraseña:")
        self.confirmar_label.grid(row=5, column=3, padx=10, pady=10)
        self.confirmar_entry = tk.Entry(self.root)
        self.confirmar_entry.grid(row=5, column=4, padx=10, pady=10)

        self.register_button = tk.Button(self.root, text="Registrar", command=self.register)    #command=self.register
        self.register_button.grid(row=6, column=2, columnspan=2, padx=10, pady=10)        

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
        password = self.password_entry.get()
        confirm_password = self.confirmar_entry.get()
    
        # Verifica que las contraseñas coincidan
        if password != confirm_password:
            self.show_message("Las contraseñas no coinciden.")
            return
    
        # Abre el archivo XML (o crea uno si no existe)
        try:
            tree = ET.parse("professors.xml")
            root = tree.getroot()
        except FileNotFoundError:
            root = ET.Element("Professors")
            tree = ET.ElementTree(root)           
    
        # Encripta la contraseña antes de almacenarla
        password_hash = hashlib.sha256(password.encode()).hexdigest()
    
        # Crea un nuevo elemento XML para el estudiante
        professor = ET.Element("Professor")
        ET.SubElement(professor, "Nombre").text = nombre
        ET.SubElement(professor, "Apellido").text = apellido
        ET.SubElement(professor, "DPI").text = dpi        
        ET.SubElement(professor, "Password").text = password_hash  # Almacena la contraseña encriptada
    
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
        self.apellido_entry.delete(0, tk.END)
        self.dpi_entry.delete(0, tk.END)      
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
    professor_panel = ProfessorPanel(root)
    root.mainloop()
