import tkinter as tk
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from tkinter import messagebox

class ProfessorRegistrar:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Profesor")
        self.root.geometry("400x300")
        self.root.iconbitmap('Usac_logo.ico')

        tk.Label(root, text="Nombre").grid(row=0, column=0)
        self.name_entry = tk.Entry(root)
        self.name_entry.grid(row=0, column=1)

        tk.Label(root, text="Apellido").grid(row=1, column=0)
        self.last_name_entry = tk.Entry(root)
        self.last_name_entry.grid(row=1, column=1)

        tk.Label(root, text="DPI").grid(row=2, column=0)
        self.dpi_entry = tk.Entry(root)
        self.dpi_entry.grid(row=2, column=1)

        tk.Label(root, text="Contraseña").grid(row=3, column=0)
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.grid(row=3, column=1)

        tk.Label(root, text="Confirmación").grid(row=4, column=0)
        self.confirm_password_entry = tk.Entry(root, show="*")
        self.confirm_password_entry.grid(row=4, column=1)

        tk.Button(root, text="Registrar", command=self.register).grid(row=5, column=0, columnspan=2)
        tk.Button(root, text="Cerrar", command=root.destroy).grid(row=6, column=0, columnspan=2)

    def show_message(self, message):
        messagebox.showinfo("Éxito", message)

    def prettify_xml(self, elem):
        """Devuelve una versión formateada del elemento XML como una cadena."""
        rough_string = ET.tostring(elem, 'utf-8')
        reparsed = minidom.parseString(rough_string)
        return "\n".join([line for line in reparsed.toprettyxml(indent="   ").split("\n") if line.strip()])

    def register(self):
        name = self.name_entry.get()
        last_name = self.last_name_entry.get()
        dpi = self.dpi_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

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

        # Crea un nuevo elemento XML para el profesor
        professor = ET.Element("Professor")
        ET.SubElement(professor, "Nombre").text = name
        ET.SubElement(professor, "Apellido").text = last_name
        ET.SubElement(professor, "DPI").text = dpi
        ET.SubElement(professor, "Password").text = password

        # Agrega el elemento del profesor a la estructura XML
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


if __name__ == "__main__":
    root = tk.Tk()
    professorRegistrar = ProfessorRegistrar(root)
    root.mainloop()
