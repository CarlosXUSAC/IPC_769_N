import tkinter as tk
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from tkinter import messagebox

class CoursePanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Registro de Cursos")
        self.root.geometry("600x300")
        self.root['bg'] = '#EFF5C3'
        self.root.iconbitmap('Usac_logo.ico')

        self.labelX = tk.Label(self.root)
        self.labelX.grid(row=0, column=0, padx=20)
        self.labelX['bg'] = '#EFF5C3'

        self.professor_label = tk.Label(self.root)
        self.professor_label.grid(row=0, column=2, columnspan=2, padx=10, pady=10)
        self.professor_label['bg'] = '#EFF5C3'

        self.codigo_label = tk.Label(self.root, text="Codigo:")
        self.codigo_label.grid(row=1, column=1, padx=10, pady=10)
        self.codigo_entry = tk.Entry(self.root)
        self.codigo_entry.grid(row=1, column=2, padx=10, pady=10)

        self.nombre_label = tk.Label(self.root, text="Nombre:")
        self.nombre_label.grid(row=1, column=3, padx=10, pady=10)
        self.nombre_entry = tk.Entry(self.root)
        self.nombre_entry.grid(row=1, column=4, padx=10, pady=10)

        self.catedratico_label = tk.Label(self.root, text="Catedratico:")
        self.catedratico_label.grid(row=2, column=1, padx=10, pady=10)
        self.catedratico_entry = tk.Entry(self.root)
        self.catedratico_entry.grid(row=2, column=2, padx=10, pady=10)

        self.horario_label = tk.Label(self.root, text="Horario:")
        self.horario_label.grid(row=2, column=3, padx=10, pady=10)
        self.horario_entry = tk.Entry(self.root)
        self.horario_entry.grid(row=2, column=4, padx=10, pady=10)

        self.cupo_label = tk.Label(self.root, text="Cupo:")
        self.cupo_label.grid(row=5, column=1, padx=10, pady=10)
        self.cupo_entry = tk.Entry(self.root)
        self.cupo_entry.grid(row=5, column=2, padx=10, pady=10)

        self.costo_label = tk.Label(self.root, text="Costo:")
        self.costo_label.grid(row=5, column=3, padx=10, pady=10)
        self.costo_entry = tk.Entry(self.root)
        self.costo_entry.grid(row=5, column=4, padx=10, pady=10)

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
        codigo = self.codigo_entry.get()
        nombre = self.nombre_entry.get()
        catedratico = self.catedratico_entry.get()
        horario = self.horario_entry.get()
        cupo = self.cupo_entry.get()
        costo = self.costo_entry.get()    
            
        # Abre el archivo XML (o crea uno si no existe)
        try:
            tree = ET.parse("cursos.xml")
            root = tree.getroot()
        except FileNotFoundError:
            root = ET.Element("Cursos")
            tree = ET.ElementTree(root)              
            
        # Crea un nuevo elemento XML para el curso
        curso = ET.Element("Curso")
        ET.SubElement(curso, "Codigo").text = codigo
        ET.SubElement(curso, "Nombre").text = nombre
        ET.SubElement(curso, "Catedratico").text = catedratico
        ET.SubElement(curso, "Horario").text = horario
        ET.SubElement(curso, "Cupo").text = cupo
        ET.SubElement(curso, "Costo").text = costo
    
        # Agrega el elemento del curso a la estructura XML
        root.append(curso)
    
        # Guarda los cambios en el archivo XML con formato y saltos de línea
        xml_str = self.prettify_xml(root)
        with open("cursos.xml", "w") as xml_file:
            xml_file.write(xml_str)
    
        # Mostrar un mensaje de éxito
        self.show_message("Datos registrados con éxito")
    
        # Limpiar los campos después de registrar       
        self.codigo_entry.delete(0, tk.END)
        self.nombre_entry.delete(0, tk.END)
        self.catedratico_entry.delete(0, tk.END)
        self.horario_entry.delete(0, tk.END)
        self.cupo_entry.delete(0, tk.END)
        self.costo_entry.delete(0, tk.END)
           

    def view_courses(self):
        # Implementa la lógica para que el estudiante pueda ver los cursos disponibles aquí
        pass   

    def logout(self):
        self.root.destroy()
        

if __name__ == "__main__":
    root = tk.Tk()
    course_panel = CoursePanel(root)
    root.mainloop()
