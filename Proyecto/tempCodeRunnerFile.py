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
