import funcionDeConexion
import mysql.connector
def interfazSql(id,title):
    try:
        conexion = funcionDeConexion.conexionBd(1)
        cursor = conexion.cursor()
        sql = f"INSERT INTO Materia (id, title) VALUES ('{id}', '{title}');"
        print(sql)
        cursor.execute(sql)
        conexion.commit()
        conexion.close()
    except mysql.connector.Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        # reverting changes because of exception
        conexion.rollback()

interfazSql('5','Administracion')