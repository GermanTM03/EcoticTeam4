from reportes import ReporteGenerator
from filtro import FiltroGenerator
from notis import confirmar
from status import filtro_por_id_usuario
from registro_admins import main
from admin import FPU
from modificarus import Main1






def general():
 
    while True:
           print("Que operacion quieres realizar??")
           print("1.GenerarReportes, 2.Notificaciones,3.Busqueda,4.Tus Reportes,5.Cerrar Sesion")
           
           seleccion = input("Selecciona una opcion:")
           
           if seleccion.lower()== "1":
               print("Inicia tu resporte especificando si es ambiental o algo similar.")
               # Uso de la clase
               generador_reportes = ReporteGenerator()
               generador_reportes.generar_reporte()
               generador_reportes.cerrar_conexion()
           elif seleccion.lower()=="2":
               print("Estas Son Las Notificaciones De Los Reportes Añadidos:")
               confirmar()
           elif seleccion.lower()=="3":
               print("Busca mediante el filtro")
               filtro_instance = FiltroGenerator()

               filtro_instance.filtrar()

               filtro_instance.cerrar_conexion()
           elif seleccion.lower()=="4":
                id_usuario = input("Tu id de usuario: ")
                filtro_por_id_usuario(id_usuario)
           elif seleccion.lower()=="5":
               print("Cerrando Sesion")
               break
        
def admin():
 
    while True:
           print("¿Que operacion quieres realizar?")
           print("1.Reportes Modificar, 2.Agregar Usuarios, 3.Modificar Usuario,4.Cerrar Sesion")
           
           seleccion = input("Selecciona una opcion:")
           
           if seleccion.lower()== "1":
               id_usuario = input("Ingresa El ID de usuario: ")
               FPU(id_usuario)

           elif seleccion.lower()=="2":
               print("Agregar Administrador:")
               main()
           elif seleccion.lower()=="3":
               print("Modificar Usuario:")
               Main1()
         
           elif seleccion.lower()=="4":
                print("Cerrando Sesion")
                break
            


