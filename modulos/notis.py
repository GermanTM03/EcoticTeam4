import mysql.connector
from datetime import datetime
from reportes import ReporteGenerator


class Notificaciones(ReporteGenerator):
    def __init__(self, estatus, Id_reporte):
        super().__init__(estatus,Id_reporte)
        self.reporte=Id_reporte


def notis():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        port="3306",
        password='123456',
        database='python'
    )
    cursor = conn.cursor()

    select_query = "SELECT ubicacion, asunto, fecha,estado FROM reportes WHERE estado = 'Activa' ORDER BY fecha DESC LIMIT 4"
    cursor.execute(select_query)

    active_reports = cursor.fetchall()

    print("\nNotificaciones Activas:")
    print("{:<20} {:<20} {:<20}".format("Ubicacion", "Asunto", "Fecha","Estado"))

    for report in active_reports:
        formatted_date = datetime.strftime(report[2], "%Y-%m-%d %H:%M:%S")
        print("{:<20} {:<20} {:<20}".format(report[0], report[1], formatted_date))

    cursor.close()
    conn.close()

def confirmar():
    while True:
        res = input("¿Quieres Recibir Notificaciones? 1.Si,2.No : ")

        if res.lower() == "1":
            notis()
            break
        elif res.lower() == "2":
            print("No Tendrás más notificaciones")
            break
        else:
            print("Respuesta no válida")


