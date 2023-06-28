import funcionDeConexion
import mysql.connector
def interfazSql(id,title):
    try:
        conexion = funcionDeConexion.conexionBd(1)
        cursor = conexion.cursor()
        sql = f"UPDATE Materia SET id = {id} where title = '{title}';"
        print(sql)
        cursor.execute(sql)
        conexion.commit()
    except mysql.connector.Error as error:
        print("Failed to update record to database rollback: {}".format(error))
        # reverting changes because of exception
        conexion.rollback()
    finally:
        cursor.close()
        conexion.close()

interfazSql('1001','Administracion')