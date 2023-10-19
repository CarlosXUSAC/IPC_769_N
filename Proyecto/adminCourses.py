import tkinter as tk
import tkinter.messagebox as messagebox
import xml.etree.ElementTree as ET

class CourseManagementApp:
    def __init__(self, root, cursos_file):
        self.root = root
        self.cursos_file = cursos_file
        self.root.title("Gestión de Cursos")
        self.root.geometry("500x300")
        self.root['bg'] = '#F5C3CB'
        self.root.iconbitmap('Usac_logo.ico')
        
        self.initialize_ui()

    def initialize_ui(self):
        self.course_code_label = tk.Label(self.root, background='#F5C3CB', height=3)
        self.course_code_label.grid(row=0, column=0)
        self.course_code_label = tk.Label(self.root, background='#F5C3CB', width=15)
        self.course_code_label.grid(row=1, column=0)
        self.course_code_label = tk.Label(self.root, background='#F5C3CB', width=5)
        self.course_code_label.grid(row=1, column=2)
        self.course_code_label = tk.Label(self.root, background='#F5C3CB')
        self.course_code_label.grid(row=5, column=0)

        self.course_code_label = tk.Label(self.root, text="Código del Curso:", background='#F5C3CB')
        self.course_code_label.grid(row=1, column=1)
        self.course_code_entry = tk.Entry(self.root)
        self.course_code_entry.grid(row=1, column=3)

        self.course_name_label = tk.Label(self.root, text="Nombre del Curso:", background='#F5C3CB')
        self.course_name_label.grid(row=2, column=1)
        self.course_name_entry = tk.Entry(self.root)
        self.course_name_entry.grid(row=2, column=3)
        
        self.course_catedratico_label = tk.Label(self.root, text="Catedrático:", background='#F5C3CB')
        self.course_catedratico_label.grid(row=3, column=1)
        self.course_catedratico_entry = tk.Entry(self.root)
        self.course_catedratico_entry.grid(row=3, column=3)
        
        self.course_horario_label = tk.Label(self.root, text="Horario:", background='#F5C3CB')
        self.course_horario_label.grid(row=4, column=1)
        self.course_horario_entry = tk.Entry(self.root)
        self.course_horario_entry.grid(row=4, column=3)
        
        # self.add_button = tk.Button(self.root, text="Agregar Curso", command=self.add_course)
        # self.add_button.grid(row=4, column=0)
        
        self.edit_button = tk.Button(self.root, text="Editar Curso", command=self.edit_course)
        self.edit_button.grid(row=6, column=1)
        
        self.delete_button = tk.Button(self.root, text="Eliminar Curso", command=self.delete_course)
        self.delete_button.grid(row=6, column=3)

        self.exit_button = tk.Button(self.root, text="Salir", command=self.logout)
        self.exit_button.grid(row=6, column=5)

    def show_message(self, message):
        messagebox.showinfo("Éxito", message)

    def add_course(self):
        course_code = self.course_code_entry.get()
        course_name = self.course_name_entry.get()
        course_catedratico = self.course_catedratico_entry.get()
        course_horario = self.course_horario_entry.get()
        
        if course_code and course_name and course_catedratico and course_horario:
            tree = ET.parse(self.cursos_file)
            root = tree.getroot()
            course_element = ET.Element('Curso')
            
            code_element = ET.Element('Codigo')
            code_element.text = course_code
            course_element.append(code_element)
            
            name_element = ET.Element('Nombre')
            name_element.text = course_name
            course_element.append(name_element)
            
            catedratico_element = ET.Element('Catedratico')
            catedratico_element.text = course_catedratico
            course_element.append(catedratico_element)
            
            horario_element = ET.Element('Horario')
            horario_element.text = course_horario
            course_element.append(horario_element)
            
            root.append(course_element)
            tree.write(self.cursos_file)
            self.show_message("Curso agregado con éxito.")
        else:
            self.show_message("Por favor, ingresa todos los datos del curso.")

    def edit_course(self):
        course_code = self.course_code_entry.get()
        course_name = self.course_name_entry.get()
        course_catedratico = self.course_catedratico_entry.get()
        course_horario = self.course_horario_entry.get()
        
        if course_code:
            tree = ET.parse(self.cursos_file)
            root = tree.getroot()
            for course_element in root:
                code_element = course_element.find('Codigo')
                if code_element is not None and code_element.text == course_code:
                    name_element = course_element.find('Nombre')
                    if name_element is not None:
                        name_element.text = course_name
                    catedratico_element = course_element.find('Catedratico')
                    if catedratico_element is not None:
                        catedratico_element.text = course_catedratico
                    horario_element = course_element.find('Horario')
                    if horario_element is not None:
                        horario_element.text = course_horario
                    tree.write(self.cursos_file)
                    self.show_message(f"Curso '{course_code}' editado con éxito.")
                    return
            self.show_message(f"Curso '{course_code}' no encontrado.")
        else:
            self.show_message("Por favor, ingresa el código del curso.")

    def delete_course(self):
        course_code = self.course_code_entry.get()
        
        if course_code:
            tree = ET.parse(self.cursos_file)
            root = tree.getroot()
            for course_element in root:
                code_element = course_element.find('Codigo')
                if code_element is not None and code_element.text == course_code:
                    root.remove(course_element)
                    tree.write(self.cursos_file)
                    self.show_message(f"Curso '{course_code}' eliminado con éxito.")
                    return
            self.show_message(f"Curso '{course_code}' no encontrado.")
        else:
            self.show_message("Por favor, ingresa el código del curso.")

    def logout(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    
    cursos_file = 'cursos.xml'
    
    course_management_app = CourseManagementApp(root, cursos_file)
    
    root.mainloop()
