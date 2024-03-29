import random
import string
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
import tkinter as tk
from tkinter import messagebox
import xml.etree.ElementTree as ET
from adminPanel import AdminPanel
from professorPanel import ProfessorPanel
from professorReg import ProfessorReg
from asignacionPanel import AsignPanel
from PIL import Image, ImageTk
import hashlib 

class CursoApp:
    def __init__(self, root):
        self.root = root
        self.validated_username = None
        self.root.title("Sistema de Gestión de Cursos")
        self.root.geometry("350x480")
        self.root['bg'] = '#74a5d6'
        self.root.iconbitmap('Usac_logo.ico')  
        self.logo = Image.open("logo-usac.png")
        self.logo_photo = ImageTk.PhotoImage(self.logo)
        self.logo_label = tk.Label(self.root, image=self.logo_photo)
        self.logo_label.pack()

        self.login_frame = tk.Frame(self.root, background="#74a5d6")
        self.login_frame.pack()                             

        self.username_label = tk.Label(self.login_frame, text="Nombre de Usuario:", background="#74a5d6", width=18, height=2)
        self.username_label.pack()
        
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack()

        self.password_label = tk.Label(self.login_frame, text="Contraseña:", background="#74a5d6", width=18, height=2)
        self.password_label.pack()
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack()

        self.logo_label = tk.Label(self.login_frame, background="#74a5d6", width=18)
        self.logo_label.pack()

        self.login_button = tk.Button(self.login_frame, text="Iniciar Sesión", command=self.login)
        self.login_button.pack()

    def login(self):        
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        password = hashlib.sha256(password.encode()).hexdigest() 

        self.username_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)

        if username == "Admin" and password == "a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3":
            self.show_admin_panel()
        elif self.validate_user(username, password, "students.xml", "Student"):
            self.validated_username = username
            self.show_student_panel()
        elif self.validate_user(username, password, "professors.xml", "Professor"):
            self.show_professor_panel()
        else:
            if messagebox.askyesno("Recuperar Contraseña", "¿Olvidaste tu contraseña?"):
                email = self.get_user_email(username, "students.xml", "Student")
                if email:
                    new_password = self.generate_new_password()
                    self.update_password(username, new_password, "students.xml", "Student")
                    self.send_password_reset_email(username, email, new_password)
                else:
                    messagebox.showerror("Error", "No se pudo encontrar el correo electrónico del usuario.")
            else:
                messagebox.showerror("Error", "Usuario o contraseña incorrectos")

    def generate_new_password(self, length=12):
        characters = string.ascii_letters + string.digits
        new_password = ''.join(random.choice(characters) for _ in range(length))
        return new_password

    def validate_user(self, username, password, xml_file, user_element_name):
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()

            for user in root.findall(user_element_name):
                xml_username = user.find("Usuario").text
                xml_password = user.find("Password").text

                if xml_username == username and xml_password == password:
                    return True

        except ET.ParseError as e:
            print(f"Error al analizar el archivo XML: {e}")

        return False            

    def get_user_email(self, username, xml_file, user_element_name):
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()

            for user in root.findall(user_element_name):
                xml_username = user.find("Usuario").text
                xml_email_element = user.find("Correo")

                if xml_username == username and xml_email_element is not None:
                    return xml_email_element.text

        except ET.ParseError as e:
            print(f"Error al analizar el archivo XML: {e}")

        return None
    
    def update_password(self, username, new_password, xml_file, user_element_name):
        try:
            tree = ET.parse(xml_file)
            root = tree.getroot()

            for user in root.findall(user_element_name):
                xml_username = user.find("Usuario").text

                if xml_username == username:
                    user.find("Password").text = hashlib.sha256(new_password.encode()).hexdigest()
                    tree.write(xml_file)

        except ET.ParseError as e:
            print(f"Error al analizar el archivo XML: {e}")

    def send_password_reset_email(self, username, email, new_password):
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        smtp_username = 'usac9520488@gmail.com'
        smtp_password = 'Cuco174**'

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)

            msg = MIMEMultipart()
            msg['From'] = smtp_username
            msg['To'] = email
            msg['Subject'] = 'Recuperación de contraseña'

            message = f"Hola {username}, tu nueva contraseña es: {new_password}"
            msg.attach(MIMEText(message, 'plain'))

            server.sendmail(smtp_username, email, msg.as_string())

            server.quit()

            messagebox.showinfo("Éxito", "Se ha enviado un correo con la nueva contraseña.")
        except Exception as e:
            messagebox.showerror("Error", f"Error al enviar el correo: {e}")

    def show_admin_panel(self):        
        adPanel = tk.Tk()
        admin_panel = AdminPanel(adPanel)
        root.mainloop()

    def show_professor_panel(self):        
        proPanel = tk.Tk()
        admin_panel = ProfessorReg(proPanel)
        root.mainloop()

    def show_student_panel(self):
        stuPanel = tk.Tk()
        student_panel = AsignPanel(stuPanel, self.validated_username)
        stuPanel.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = CursoApp(root)
    root.mainloop()
