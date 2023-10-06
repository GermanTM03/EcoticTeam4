from registro_usuarios import recopilar_informacion, mostrar_resultados, guardar_usuario_en_mysql
from login import extraer_usuario_logueado

o1 = "Salir"
o2 = "Registro"
o3 = "Login"

def inicio():
    print("Bienvenido a Eco-tic :D")


def seleccion():
    print("Puedes Seleccionar Una Opcion:")

def opciones():
    while True:
        seleccion()
        print(f"1. {o3}, 2. {o2}, 3. {o1}")

        sel = input("Escribe Una Opcion: ")
        if sel.lower() == "1":
             extraer_usuario_logueado()
            
        elif sel.lower() == "2":
            
            nuevo_usuario = recopilar_informacion()
            
            mostrar_resultados(nuevo_usuario)
            guardar_usuario_en_mysql(nuevo_usuario)
            

               
        elif sel.lower() == "3":
            print("Cancelemos Operaciones")
            break

if __name__ == "__main__":
    inicio()
    opciones()
