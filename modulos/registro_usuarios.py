import mysql.connector
import getpass

class Usuario:
    def __init__(self, nombre, correo, pwd, edad, ubicacion, telefono, rango):
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
    rango = '0'  # Rango por defecto para usuarios normales
    return Usuario(nombre, correo, pwd, edad, ubicacion, telefono, rango)

def guardar_usuario_en_mysql(usuario):
    # Conectarse a la base de datos MySQL (asegúrate de tener una base de datos y una tabla creadas)
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
    conn.close()

def mostrar_resultados(usuario):
    print("\nTu Usuario Ha Sido Guardado Correctamente:")
    print(f"Nombre: {usuario.nombre}, Correo: {usuario.correo}, Edad: {usuario.edad}, Ubicación: {usuario.ubicacion}, Teléfono: {usuario.telefono}, Rango: {usuario.rango}")

    respuesta_ubicacion = usuario.ubicacion.lower()

    if respuesta_ubicacion == "si":
        print("Ubicación permitida. Mensaje positivo.")
    elif respuesta_ubicacion == "no":
        print("Ubicación no permitida. Mensaje negativo.")
    else:
        print(f"Respuesta no reconocida para la ubicación: {usuario.ubicacion}")

    print("Usuario Finalizado :3 \n")

def main():
    nuevo_usuario = recopilar_informacion()
    guardar_usuario_en_mysql(nuevo_usuario)
    mostrar_resultados(nuevo_usuario)

if __name__ == "__main__":
    main()
