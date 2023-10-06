import mysql.connector
from registro_usuarios import Usuario

class ubi(Usuario):
    def __init__(self,  ubicacion):
        super().__init__(ubicacion)


class FiltroGenerator(ubi):
    

    def __init__(self):
        self.conn = mysql.connector.connect(
            host='localhost',
            user='root',
            port="3306",
            password='123456',
            database='python'
        )
        self.cursor = self.conn.cursor()

    def filtrar(self):
        print("--Bienvenido Al Filtro--")
        print("--Opciones--")
        print("1. Categorías\n2. Estatus\n3. Evidencias\n4. Ubicacion")
        opcion = input("Selecciona Una Opcion: ")

        if opcion == "1":
            self.filtrar_por_categorias()
        elif opcion == "2":
            self.filtrar_por_estatus()
        elif opcion == "3":
            self.filtrar_por_evidencias()
    
        elif opcion == "4":
            self.filtrar_por_ubicacion()
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

    def filtrar_por_categorias(self):
        print("Categorías Disponibles:")
        self.cursor.execute("SELECT DISTINCT categorias FROM reportes")
        categorias_resultados = self.cursor.fetchall()

        for i, row in enumerate(categorias_resultados, start=1):
            print(f"{i}. Categoría: {row[0]}")

        categoria_numero = int(input("Elige el número de la categoría: "))
        if 1 <= categoria_numero <= len(categorias_resultados):
            selected_categoria = categorias_resultados[categoria_numero - 1][0]
            print(f"Mostrando reportes de la categoría: {selected_categoria}")

            self.mostrar_reportes("categorias", selected_categoria)
        else:
            print("Número de categoría no válido.")

    def filtrar_por_estatus(self):
        print("Estatus Disponibles:")
        estados = ["Activa", "Inactiva", "Verificacion"]
        for i, estado in enumerate(estados, start=1):
            print(f"{i}. {estado}")

        estado_seleccionado = input("Elige el estado (Activa/Inactiva/Verificacion): ")
        estado_seleccionado = estado_seleccionado.capitalize()  

        if estado_seleccionado in estados:
            print(f"Mostrando reportes con el estatus: {estado_seleccionado}")
            self.mostrar_reportes("estado", estado_seleccionado)
        else:
            print("Estatus no válido.")

    def filtrar_por_evidencias(self):
        var = input("Selecciona una opción: 1. Mostrar con evidencia / 2. Mostrar sin evidencia")

        if var == "1" or var == "2":
            evidencia_value = "si" if var == "1" else "no"
            print(f"Mostrando reportes con evidencia: {evidencia_value}")

            self.mostrar_reportes("evidencia", evidencia_value)
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

    def filtrar_por_ubicacion(self):
        ubicacion = input("Ingresa la ubicación para filtrar: ")

        self.cursor.execute("SELECT asunto, ubicacion FROM reportes WHERE ubicacion = %s", (ubicacion,))
        resultados = self.cursor.fetchall()

        if resultados:
            print(f"Mostrando reportes en la ubicación {ubicacion}:")
            for i, row in enumerate(resultados, start=1):
                print(f"{i}. Asunto: {row[0]}, Ubicación: {row[1]}")
        else:
            print(f"No hay reportes en la ubicación {ubicacion}.")
    
    def mostrar_reportes(self, filtro_tipo, filtro_valor):
        columnas = {
            "categorias": "categorias",
            "estado": "estado",
            "evidencia": "evidencia"
        }
        self.cursor.execute(f"SELECT id, categorias, asunto, estado FROM reportes WHERE {columnas[filtro_tipo]} = %s", (filtro_valor,))
        resultados = self.cursor.fetchall()

        for i, row in enumerate(resultados, start=1):
            print(f"{i}. ID: {row[0]}, Categoría: {row[1]}, Asunto: {row[2]}, Estatus: {row[3]}")

    def cerrar_conexion(self):
        self.cursor.close()
        self.conn.close()



