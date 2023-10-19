import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import xml.etree.ElementTree as ET 

class AsignPanel:
    def __init__(self, root, validated_username):
        self.root = root
        self.validated_username = validated_username # Almacena el nombre de usuario validado
        self.root.title("Seleccionar Cursos")
        self.root.geometry("500x400")
        self.root['bg'] = '#E2B3BF'
        self.root.iconbitmap('Usac_logo.ico')

        # Resto de la inicialización de la interfaz de usuario...

        self.tree = ET.parse('cursos.xml')  # Archivo que contiene la lista de cursos
        self.root_cursos = self.tree.getroot()

        self.tree_student = ET.parse('students.xml')  # Archivo que contiene los datos de los estudiantes
        self.root_students = self.tree_student.getroot()

        self.selected_courses = []

        self.courses_label = tk.Label(self.root, text="Cursos Disponibles:")
        self.courses_label.grid(row=1, column=1, padx=10, pady=10)
        self.courses_listbox = tk.Listbox(self.root)
        self.courses_listbox.grid(row=1, column=2, padx=10, pady=10)

        self.selected_courses_label = tk.Label(self.root, width=10, background='#E2B3BF')
        self.selected_courses_label.grid(row=1, column=0)

        self.register_button = tk.Button(self.root, text="Seleccionar Curso", command=self.select_course)
        self.register_button.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

        self.save_button = tk.Button(self.root, text="Guardar Selección", command=self.save_selection)
        self.save_button.grid(row=3, column=2, columnspan=2, padx=10, pady=10)

        self.salir_button = tk.Button(self.root, text="Salir", command=self.logout)
        self.salir_button.grid(row=6, column=4, padx=10, pady=10)

        self.update_course_list()

    def show_student_panel(self):
        stuPanel = tk.Tk()
        student_panel = AsignPanel(stuPanel, self.validated_username)
        stuPanel.mainloop()



    def show_message(self, message):
        messagebox.showinfo("Éxito", message)

    def update_course_list(self):
        self.courses_listbox.delete(0, tk.END)
        for curso in self.root_cursos:
            nombre_curso = curso.find('Nombre').text
            if nombre_curso not in self.selected_courses:
                self.courses_listbox.insert(tk.END, nombre_curso)

    def select_course(self):
        selected_course = self.courses_listbox.get(self.courses_listbox.curselection())
        if selected_course:
            if selected_course not in self.selected_courses:
                self.selected_courses.append(selected_course)
                self.update_course_list()

    def save_selection(self):
        student_username = self.validated_username  # Utiliza el nombre de usuario validado

        # Buscar al estudiante por su nombre de usuario
        student_element = None
        for student in self.root_students:
            if student.find('Usuario').text == student_username:
                student_element = student
                break

        if student_element is not None:
            # Obtener la sección "Cursos" del estudiante en el archivo "students.xml"
            cursos_element = student_element.find('Cursos')
            if cursos_element is None:
                cursos_element = ET.SubElement(student_element, 'Cursos')

            # Limpiar la sección "Cursos" antes de agregar los cursos nuevamente
            for curso in cursos_element.findall('Curso'):
                cursos_element.remove(curso)

            # Agregar los cursos a la sección "Cursos"
            for course in self.selected_courses:
                curso_element = ET.SubElement(cursos_element, 'Curso')
                curso_element.text = course

            # Guardar los cambios en el archivo "students.xml"
            self.tree_student.write("students.xml")
            self.show_message("Selección de cursos guardada con éxito.")
        else:
            self.show_message("Estudiante no encontrado. Verifica el nombre de usuario.")

    def logout(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    asign_panel = AsignPanel(root)
    root.mainloop()
