import mysql.connector
from datetime import datetime
from registro_usuarios import Usuario




class ReporteGenerator(Usuario):
    def __init__(self, nombre, correo, pwd, edad, ubicacion, telefono, rango,estatus, ):
        super().__init__(nombre, correo, pwd, edad, ubicacion, telefono, rango,estatus)
        self.estatus = estatus

    
    
    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            port="3306",
            password='123456',
            database='python'
        )
        self.cursor = self.conn.cursor()

    def generar_reporte(self):
        print("Genera Un Reporte")

        usuario_id = input("Ingresa tu ID de usuario: ")

        self.cursor.execute("SELECT id FROM usuarios WHERE id = %s", (usuario_id,))
        resultado = self.cursor.fetchone()
        if not resultado:
            print("ID de usuario no válido. Asegúrate de que el usuario exista en la tabla usuarios.")
            self.cursor.close()
            self.conn.close()
            return

        asunto = input("Cual Es El Asunto:")
        ubicacion = input("Donde Ocurrio:")

        categorias_disponibles = ["Residuos Sólidos",
                                  "Contaminación del Agua",
                                  "Contaminación del Aire",
                                  "Deforestación",
                                  "Deforestación", 
                                  "Energías Renovables"]

        print("Categorías Disponibles:")
        for i, categoria in enumerate(categorias_disponibles, start=1):
            print(f"{i}. {categoria}")

        categoria_numero = int(input("Elige el número de la categoría: "))
        if 1 <= categoria_numero <= len(categorias_disponibles):
            categoria = categorias_disponibles[categoria_numero - 1]
        else:
            print("Número de categoría no válido. Seleccionando la categoría predeterminada.")
            categoria = "Categoria Predeterminada"

        evidencia = input("¿Tienes evidencia?:")
        estado = "Verificacion"

        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("\nDetalles del Reporte:")
        print("{:<20}: {}".format("Usuario ID", usuario_id))
        print("{:<20}: {}".format("Asunto", asunto))
        print("{:<20}: {}".format("Ubicación", ubicacion))
        print("{:<20}: {}".format("Categoría", categoria))
        print("{:<20}: {}".format("Evidencia", evidencia))
        print("{:<20}: {}".format("Fecha", fecha_actual))

        confirmacion = input("¿Deseas confirmar este reporte? 1.Si, 2.No: ").lower()
        if confirmacion != "1":
            print("Cancelando Operación.")
            self.cursor.close()
            self.conn.close()
            return

        insert_query = "INSERT INTO reportes (Usuario_R, asunto, ubicacion, categorias, evidencia, estado, fecha) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        self.cursor.execute(insert_query, (usuario_id, asunto, ubicacion, categoria, evidencia, estado, fecha_actual))
        self.conn.commit()

        print("Reporte Completado")

    def cerrar_conexion(self):
        self.cursor.close()
        self.conn.close()


