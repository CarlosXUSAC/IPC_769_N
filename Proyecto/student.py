import tkinter as tk
import xml.etree.ElementTree as ET


class ProfessorPanel:
    def __init__(self, root):
        self.root = root
        self.root.title("Panel de Profesor")
        self.root.geometry("600x400")

        self.professor_label = tk.Label(self.root, text="Panel de Profesor")
        self.professor_label.pack()

        self.load_data_button = tk.Button(self.root, text="Cargar Datos", command=self.load_data)
        self.load_data_button.pack()

        self.edit_course_button = tk.Button(self.root, text="Editar Curso Asignado", command=self.edit_course)
        self.edit_course_button.pack()

        self.logout_button = tk.Button(self.root, text="Cerrar Sesión", command=self.logout)
        self.logout_button.pack()

        self.professor_data = None  # Almacenará los datos del profesor

    def load_data(self):
        # Carga los datos del archivo XML MOCK_DATA.xml y muestra los datos relevantes
        try:
            tree = ET.parse("MOCK_DATA.xml")
            data = tree.getroot()
            # Encuentra el nodo correspondiente al profesor actual (puede ser según el ID, usuario, etc.)
            # Supongamos que se identifica al profesor por su ID (cambiarlo según tus necesidades)
            professor_id = "ID_DEL_PROFESOR_A_ACTUALIZAR"
            for element in data.findall(".//MOCK_DATA[@id='{}']".format(professor_id)):
                self.professor_data = element
                # Muestra los datos relevantes en la interfaz gráfica (nombre, apellido, cursos, etc.)
                # Puedes usar self.professor_data.find(...) para acceder a elementos específicos del profesor
                # Mostrar los datos en etiquetas o campos de texto en la GUI
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error al cargar datos: {e}")

    def edit_course(self):
        if self.professor_data is not None:
            # Implementa la lógica para que el profesor pueda editar el campo 'Curso_asignado'
            # Puedes usar self.professor_data.find(...) para acceder al campo 'Curso_asignado'
            # Actualiza el campo en la interfaz gráfica y en el archivo XML
            pass
        else:
            tk.messagebox.showerror("Error", "Cargue los datos primero")

    def logout(self):
        # Implementa la lógica para cerrar sesión aquí
        pass

if __name__ == "__main__":
    root = tk.Tk()
    professor_panel = ProfessorPanel(root)
    root.mainloop()
