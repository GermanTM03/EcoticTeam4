import mysql.connector
import getpass

class Registro:
    def __init__(self, id, nombre, correo, pwd, edad, ubicacion, telefono, rango):
        self.id = id
        self.nombre = nombre
        self.correo = correo
        self.edad = edad
        self.ubicacion = ubicacion
        self.pwd = pwd
        self.telefono = telefono
        self.rango = rango

def recopilar_informacion():
    print("Ingresa Los Siguientes Datos Para Tu Registro:")
    nombre = input("Nombre Completo: ")
    correo = input("Correo: ")

    while True:
        pwd = getpass.getpass("Ingresa tu contraseña: ")
        confirm_pwd = getpass.getpass("Confirmacion De Contraseña: ")
        ubicacion = input("Permites Proporcionar tu ubicación? (si/no): ")
        if pwd == confirm_pwd:
            break
        else:
            print("Las contraseñas no coinciden. Inténtalo de nuevo.")

    edad = input("Edad: ")
    telefono = input("Teléfono: ")
    rango = input("Rango (1/0): ")  # Ahora el usuario puede elegir 1 o 0
    return Registro(id=None, nombre=nombre, correo=correo, pwd=pwd, edad=edad, ubicacion=ubicacion, telefono=telefono, rango=rango)

def guardar_usuario_en_mysql(usuario):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        port="3306",
        password='123456',
        database='python'
    )
    cursor = conn.cursor()

    insert_query = "INSERT INTO usuarios (nombre, correo, pwd, edad, ubicacion, telefono, rango) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    data = (usuario.nombre, usuario.correo, usuario.pwd, usuario.edad, usuario.ubicacion, usuario.telefono, usuario.rango)
    cursor.execute(insert_query, data)

    conn.commit()
    usuario.id = cursor.lastrowid  
    conn.close()

def actualizar_usuario_en_mysql(usuario):
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        port="3306",
        password='123456',
        database='python'
    )
    cursor = conn.cursor()

    update_query = "UPDATE usuarios SET nombre = %s, correo = %s, pwd = %s, edad = %s, ubicacion = %s, telefono = %s, rango = %s WHERE id = %s"
    data = (usuario.nombre, usuario.correo, usuario.pwd, usuario.edad, usuario.ubicacion, usuario.telefono, usuario.rango, usuario.id)
    cursor.execute(update_query, data)

    conn.commit()
    conn.close()

def mostrar_todos_usuarios():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        port="3306",
        password='123456',
        database='python'
    )
    cursor = conn.cursor()

    select_query = "SELECT * FROM usuarios"
    cursor.execute(select_query)

    usuarios = cursor.fetchall()

    print("\nLista de Usuarios:")
    for usuario in usuarios:
        print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Correo: {usuario[2]}, Edad: {usuario[4]}, Ubicación: {usuario[5]}, Teléfono: {usuario[6]}, Rango: {usuario[7]}")

    conn.close()

def mostrar_resultados(usuario):
    print("\nInformación del Usuario:")
    print(f"ID: {usuario.id}, Nombre: {usuario.nombre}, Correo: {usuario.correo}, Edad: {usuario.edad}, Ubicación: {usuario.ubicacion}, Teléfono: {usuario.telefono}, Rango: {usuario.rango}")

    if usuario.ubicacion is not None:
        respuesta_ubicacion = usuario.ubicacion.lower()

        if respuesta_ubicacion == "si":
            print("Ubicación permitida. Mensaje positivo.")
        elif respuesta_ubicacion == "no":
            print("Ubicación no permitida. Mensaje negativo.")
        else:
            print(f"Respuesta no reconocida para la ubicación: {usuario.ubicacion}")
    else:
        print("Ubicación no disponible.")

    print("Operación completada.\n")

def modificar_usuario():
    id_usuario = input("Ingresa el ID del usuario que deseas modificar: ")

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        port="3306",
        password='123456',
        database='python'
    )
    cursor = conn.cursor()

    select_query = "SELECT * FROM usuarios WHERE id = %s"
    cursor.execute(select_query, (id_usuario,))
    usuario_existente = cursor.fetchone()

    conn.close()

    if usuario_existente:
        usuario_existente = Registro(id=usuario_existente[0], nombre=usuario_existente[1], correo=usuario_existente[2], pwd=usuario_existente[3], edad=usuario_existente[4], ubicacion=usuario_existente[5], telefono=usuario_existente[6], rango=usuario_existente[7])

        print("Información actual del usuario:")
        mostrar_resultados(usuario_existente)

        nuevo_usuario = recopilar_informacion()

        nuevo_usuario.id = usuario_existente.id

        actualizar_usuario_en_mysql(nuevo_usuario)

        print("Usuario modificado correctamente:")
        mostrar_resultados(nuevo_usuario)
    else:
        print(f"El usuario con ID {id_usuario} no existe.")

def Main1():
    mostrar_todos_usuarios()
    modificar_usuario()
