import mysql.connector
from usuarios import general, admin
import getpass

def LoginUs():
    def logeo(es_admin):
        try:
            conn = mysql.connector.connect(
                host='localhost',
                user='root',
                port="3306",
                password='123456',
                database='python'
            )

            cursor = conn.cursor()

            while True:
                print("Hola, ingresa tus datos para ingresar")
                usuario = input("Corre0: ")
                contraseña = getpass.getpass("Ingresa tu contraseña: ")

                query = "SELECT * FROM usuarios WHERE correo = %s AND pwd = %s AND rango = %s"
                cursor.execute(query, (usuario, contraseña, es_admin))
                resultado = cursor.fetchone()

                if resultado:
                    print("\nInformación del usuario:")
                    print("ID Usuario:", resultado[0])
                    print("Nombre Completo:", resultado[1])
                    print("Correo:", resultado[2])
                    break
                else:
                    print("Usuario y/o contraseña incorrectos. Intenta de nuevo")

            cursor.close()
            conn.close()

            return resultado  
        except mysql.connector.Error as err:
            print(f"Error de MySQL: {err}")
            return None

    return logeo

def imprimir_resultado(resultado):
    if resultado:
        print("\nResultado del inicio de sesión:")
        print("Usuario Logueado:", resultado[0])
        print("Nombre Completo:", resultado[1])
        print("Correo:", resultado[2])
    else:
        print("\nUsuario y/o contraseña incorrectos. Intenta de nuevo")

def extraer_usuario_logueado():
    print("Selecciona una opción")
    print("1.Administrador, 2.Usuario")
    op = input("Ingresa Una Opcion: ")

    if op == "1":
        print("Logueo como Admin")
        admin_logeo = LoginUs()(es_admin=1)
        resultado_admin = admin_logeo
        imprimir_resultado(resultado_admin)  
        if resultado_admin:
            admin()  
    elif op == "2":
        print("Registro Como Usuario")
        user_logeo = LoginUs()(es_admin=0)
        resultado_user = user_logeo
        imprimir_resultado(resultado_user)  
        if resultado_user:
            general()  
    else:
        print("Opción Incorrecta")


