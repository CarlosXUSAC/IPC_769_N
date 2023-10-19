import tkinter as tk
import xml.etree.ElementTree as ET
import xml.dom.minidom as minidom
from tkinter import messagebox
from cursos import CoursePanel
from asignacionPanel import AsignPanel
from adminCourses import CourseManagementApp
from studentPanel import StudentPanel

class AdminPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel de Administrador")
        self.root.geometry("400x350")
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

        self.alumnos_label = tk.Label(self.root, text="Alumnos")
        self.alumnos_label.grid(row=3, column=2, padx=10, pady=10)
        self.alumnos_label['bg'] = '#66D773'

        self.reg_alumnos_button = tk.Button(self.root, text="Registrar", command=self.manage_courses)
        self.reg_alumnos_button.grid(row=3, column=3, padx=10, pady=10)

        self.gestion_cursos_label = tk.Label(self.root, text="Gestión de Cursos")
        self.gestion_cursos_label.grid(row=4, column=2, padx=10, pady=10)
        self.gestion_cursos_label['bg'] = '#66D773'

        self.gestion_cursos_button = tk.Button(self.root, text="Gestionar", command=self.register_student)
        self.gestion_cursos_button.grid(row=4, column=3, padx=10, pady=10)

        self.logout_button = tk.Button(self.root, text="Cerrar Sesión", command=self.root.quit)
        self.logout_button.grid(row=5, column=2, columnspan=2, padx=10, pady=10)

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
        coursePanel = tk.Tk()
        admin_panel = CoursePanel(coursePanel)
        root.mainloop()

    def register_student(self):
        coursePanel = tk.Tk()
        cursos_file = "ruta/al/archivo_de_cursos.xml"  # Reemplaza con la ruta correcta
        admin_panel = CourseManagementApp(coursePanel, cursos_file)
        coursePanel.mainloop()


    def view_professors(self):
        try:
            tree = ET.parse("professors.xml")
            root = tree.getroot()

            # Crear una nueva ventana para mostrar la lista de profesores
            view_professors_window = tk.Toplevel(self.root)
            view_professors_window.title("Lista de Profesores")            
            view_professors_window.iconbitmap('Usac_logo.ico')

            # Crear un área de texto para mostrar la lista de profesores
            text_area = tk.Text(view_professors_window)
            text_area.pack()

            # Iterar a través de los elementos XML y mostrar la información de los profesores
            for professor in root.findall("Professor"):
                name = professor.find("Nombre").text
                last_name = professor.find("Apellido").text
                usuario = professor.find("Usuario").text  # Corrección en la etiqueta
                password = professor.find("Password").text  # Corrección en la etiqueta
                text_area.insert(tk.END, f"Nombre: {name}\nApellido: {last_name}\nUsuario: {usuario}\nContraseña: {password}\n\n")

        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo 'professors.xml' no existe.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al leer 'professors.xml': {str(e)}")



    def view_courses(self):
        try:
            tree = ET.parse("cursos.xml")  # Asegúrate de que el nombre del archivo sea correcto
            root = tree.getroot()

            # Crear una nueva ventana para mostrar la lista de cursos
            view_courses_window = tk.Toplevel(self.root)
            view_courses_window.title("Lista de Cursos")
            view_courses_window.iconbitmap('Usac_logo.ico')

            # Crear un área de texto para mostrar la lista de cursos
            text_area = tk.Text(view_courses_window)
            text_area.pack()

            # Iterar a través de los elementos XML y mostrar la información de los cursos
            for course in root.findall("Curso"):
                course_code = course.find("Codigo").text
                course_name = course.find("Nombre").text
                catedratico = course.find("Catedratico").text
                horario = course.find("Horario").text
                cupo = course.find("Cupo").text
                costo = course.find("Costo").text
                text_area.insert(tk.END, f"Código: {course_code}\nNombre: {course_name}\nCatedrático: {catedratico}\nHorario: {horario}\nCupo: {cupo}\nCosto: {costo}\n\n")

        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo 'cursos.xml' no existe.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al leer 'cursos.xml': {str(e)}")

    def manage_courses(self):
        cursos_file = "ruta_al_archivo.xml"  # Reemplaza esto con la ubicación real de tu archivo XML
        coursePanel = tk.Tk()
        admin_panel = StudentPanel(coursePanel)
        coursePanel.mainloop()

    def logout(self):
        self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    admin_panel = AdminPanel(root)
    root.mainloop()
