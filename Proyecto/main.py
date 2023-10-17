# Ejemplo de registro de estudiante
def registrar_estudiante():
    # Captura los datos del estudiante
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    # ...
    contraseña = input("Contraseña: ")

    # Verifica si el usuario ya existe
    if usuario_existe(nombre_usuario):
        print("El nombre de usuario ya está en uso.")
    else:
        # Almacena los datos en el archivo de usuarios
        guardar_datos_usuario(nombre_usuario, contraseña, "Estudiante")
        print("Registro exitoso.")

# Ejemplo de inicio de sesión
def iniciar_sesion():
    nombre_usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    if validar_credenciales(nombre_usuario, contraseña):
        usuario = obtener_tipo_de_usuario(nombre_usuario)
        if usuario == "Estudiante":
            abrir_vista_estudiante()
        elif usuario == "Catedrático":
            abrir_vista_catedratico()
        elif usuario == "Administrador":
            abrir_vista_administrador()
    else:
        intentos_fallidos(nombre_usuario)
        print("Credenciales incorrectas.")


# Ejemplo de inscripción en un curso
def inscribirse_en_curso(nombre_usuario, codigo_curso):
    if curso_tiene_cupo_disponible(codigo_curso):
        asignar_curso_a_estudiante(nombre_usuario, codigo_curso)
        enviar_correo_confirmacion(nombre_usuario, "Inscripción exitosa.")
    else:
        print("El curso no tiene cupo disponible.")

# Ejemplo de visualización de cursos disponibles
def mostrar_cursos_disponibles():
    cursos = obtener_cursos_disponibles()
    for curso in cursos:
        print(f"Código: {curso['codigo']}")
        print(f"Nombre: {curso['nombre']}")
        # ...

# Ejemplo de envío de correo de confirmación
def enviar_correo_confirmacion(destinatario, mensaje):
    # Código para enviar un correo electrónico

# Ejemplo de creación de un curso por el administrador
def crear_curso(codigo, nombre, costo, horario, cupo, catedratico):
    if not curso_existe(codigo):
        guardar_curso(codigo, nombre, costo, horario, cupo, catedratico)
        print("Curso creado exitosamente.")
    else:
        print("El curso ya existe.")

# Ejemplo de edición de un curso por un catedrático
def editar_curso(codigo_curso, nuevo_nombre, nuevo_costo, nuevo_horario):
    if catedratico_es_duenio_del_curso(codigo_curso):
        actualizar_datos_del_curso(codigo_curso, nuevo_nombre, nuevo_costo, nuevo_horario)
        print("Curso actualizado exitosamente.")
    else:
        print("No tienes permiso para editar este curso.")

# Ejemplo de creación de un profesor por el administrador
def registrar_profesor(nombre, apellido, dpi, contraseña):
    if not usuario_existe(dpi):
        guardar_datos_usuario(dpi, contraseña, "Catedrático")
        print("Profesor registrado exitosamente.")
    else:
        print("El profesor ya está registrado.")

# Ejemplo de desbloqueo de cuenta por el administrador
def desbloquear_cuenta(nombre_usuario):
    if cuenta_bloqueada(nombre_usuario):
        desbloquear_usuario(nombre_usuario)
        print("Cuenta desbloqueada.")
    else:
        print("La cuenta no está bloqueada.")

# Generación de listados en formato .xlsx
def generar_listado_usuarios():
    # Código para generar listado de usuarios en formato .xlsx

# Ejemplo de edición de notas por el profesor
def editar_notas(codigo_curso, dpi_estudiante, nuevas_notas):
    if catedratico_es_duenio_del_curso(codigo_curso):
        actualizar_notas_del_estudiante(codigo_curso, dpi_estudiante, nuevas_notas)
        print("Notas actualizadas exitosamente.")
    else:
        print("No tienes permiso para editar notas de este curso.")

# Ejemplo de descarga de certificado por el estudiante
def descargar_certificado(codigo_curso, dpi_estudiante):
    nota = obtener_nota_del_estudiante(codigo_curso, dpi_estudiante)
    if nota >= 61:
        generar_certificado(codigo_curso, dpi_estudiante)
    else:
        print("No cumples con los requisitos para el certificado.")

