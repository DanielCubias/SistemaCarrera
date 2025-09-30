import conn as cn


def selecionmenu():

    print("-----Bienvenidos al sistema de carrera-----")
    print("escoge una opcion:\n 0 - comprobar conexion\n 1 - añadir  \n 2 - actualizar \n 3 - ver \n 4 - borrar")
    numeroUsuario = int(input(" Selecciona un numero del 1 al 4 "))

    if numeroUsuario == 0:
        cn.connexion()
    # elif numeroUsuario == 1:

            


selecionmenu()
    


    



    