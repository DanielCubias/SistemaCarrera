import conn as cn


def selecionmenu():
    print("-----Bienvenidos al sistema de carrera-----")
    print("escoge una opcion:\n 0 - comprobar conexion\n 1 - añadir  \n 2 - actualizar \n 3 - ver \n 4 - borrar")
    numeroUsuario = int(input(" Selecciona un numero del 1 al 4 "))

    while numeroUsuario < 0 or numeroUsuario >= 4:

        if numeroUsuario == 1:
            cn.connexion()
            



selecionmenu()
    


    



    