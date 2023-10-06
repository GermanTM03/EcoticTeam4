import mysql.connector

def FPU(id_usuario):
    print("--Bienvenido Al Filtro--")
    print("--Reportes--")

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        port="3306",
        password='123456',
        database='python'
    )
    cursor = conn.cursor()

    mapeo_estados = {
        '1': 'Activa',
        '2': 'Inactiva',
        '3': 'Verificacion'
    }

    cursor.execute("""
        SELECT categorias, estado, ubicacion
        FROM reportes 
        WHERE Usuario_R = %s
    """, (id_usuario,))
    
    resultados = cursor.fetchall()

    if resultados:
        for i, row in enumerate(resultados, start=1):
            print(f"{i}. Categoría: {row[0]}, Estatus: {row[1]}, Ubicación: {row[2]}")
        
        reporte_seleccionado = int(input("Selecciona el número de reporte para modificar su estado (0 para salir): "))
        
        if 0 < reporte_seleccionado <= len(resultados):
            nuevo_estado = input("Ingresa el nuevo estado para el reporte (1.Activa, 2.Inactiva, 3.Verificacion): ")
            nuevo_estado = mapeo_estados.get(nuevo_estado, 'Activa')  # Valor predeterminado: 'Activa' si la entrada no coincide
            update_query = "UPDATE reportes SET estado = %s WHERE Usuario_R = %s AND categorias = %s"
            cursor.execute(update_query, (nuevo_estado, id_usuario, resultados[reporte_seleccionado - 1][0]))
            conn.commit()
            print("Estado del reporte actualizado.")
        elif reporte_seleccionado == 0:
            print("Saliendo del filtro.")
        else:
            print("Número de reporte no válido.")
    else:
        print("No hay reportes para el usuario con ID proporcionado.")

    cursor.close()
    conn.close()

