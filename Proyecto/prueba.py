import tkinter as tk
from tkinter import messagebox
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from adminPanel import AdminPanel
from professorPanel import ProfessorPanel
from studentPanel import StudentPanel

class CursoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Gestión de Cursos")
        self.root.geometry("400x300")
        self.root['bg'] = '#74a5d6'
        self.root.iconbitmap('Usac_logo.ico')        


        self.login_frame = tk.Frame(self.root)
        self.login_frame.pack()        

        self.username_label = tk.Label(self.login_frame, background="#74a5d6", width=18,height=6)
        self.username_label.pack()

        self.username_label = tk.Label(self.login_frame, text="Nombre de Usuario:")
        self.username_label.pack()
        
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()

        self.password_label = tk.Label(self.login_frame, text="Contraseña:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(self.login_frame, text="Iniciar Sesión", command=self.login)
        self.login_button.pack()

    def login(self):
        
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin123":
            # Redirigir al panel de administrador
            self.show_admin_panel()
        elif username == "profesor" and password == "profesor123":
            # Redirigir al panel de profesor
            self.show_professor_panel()
        elif username == "estudiante" and password == "estudiante123":
            # Redirigir al panel de estudiante
            self.show_student_panel()
        else:
            # Mostrar mensaje de error
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def show_admin_panel(self):        
        adPanel = tk.Tk()
        admin_panel = AdminPanel(adPanel)
        root.mainloop()

        
    def show_professor_panel(self):        
        proPanel = tk.Tk()
        admin_panel = ProfessorPanel(proPanel)
        root.mainloop()
        

    def show_student_panel(self):        
        stuPanel = tk.Tk()
        admin_panel = StudentPanel(stuPanel)
        root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CursoApp(root)
    root.mainloop()
