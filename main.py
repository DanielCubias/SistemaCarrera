import psycopg2
import conn as cn
import delete as dl
 
if __name__ == "__main__":
    try:

        print("-----Bienvenidos al sistema de carrera-----")
        print("escoge una opcion:\n 0 - comprobar conexion\n 1 - añadir  \n 2 - actualizar \n 3 - ver \n 4 - borrar")
        numeroUsuario = int(input(" Selecciona un numero del 1 al 4 "))

        if numeroUsuario == 0:
            cn.connexion()
        elif numeroUsuario == 4:
            conexion = cn.connexion()
            resultado = dl.delete(conexion)
            print(resultado)
    
    except (Exception, psycopg2.Error) as error:
        print("error: ",  error)

   
        


    



    