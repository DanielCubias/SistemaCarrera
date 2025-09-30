## conexion  con base de datos


def connexion():
    
    import mysql.connector
    conn = mysql.connector.connect(
    host="localhost",
    user="root",
    port = 3307,
    password="1234",
    database="gestioncarrera"
    )

    print("Conexion exitosamente")
    return conn