import mysql.connector

def filtro_por_id_usuario(id_usuario):
    print("--Bienvenido Al Filtro--")
    print("--Tus Reportes--")

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        port="3306",
        password='123456',
        database='python'
    )
    cursor = conn.cursor()

    cursor.execute("""
        SELECT categorias, estado 
        FROM reportes 
        WHERE Usuario_R = %s
    """, (id_usuario,))
    
    resultados = cursor.fetchall()

    if resultados:
        for i, row in enumerate(resultados, start=1):
            print(f"{i}. Categoría: {row[0]}, Estatus: {row[1]}")
    else:
        print("No hay reportes para el usuario con ID proporcionado.")

    cursor.close()
    conn.close()


