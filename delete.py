def delete(conn):
    conn = conn

    cursor = conn.cursor()
    sql = '''DELETE FROM carrera WHERE idCarrera = 1'''
    cursor.execute(sql)
    conn.commit()
    respuesta = "Carrera eliminada correctamente"
    return respuesta