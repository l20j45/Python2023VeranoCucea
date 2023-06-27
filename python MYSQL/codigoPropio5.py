import funcionDeConexion
import mysql.connector
def interfazSql(sql,columns,table,param):
    try:
        conexion = funcionDeConexion.conexionBd(1)
        cursor = conexion.cursor()
        cursor.execute(sql,[columns,table,param])
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
    finally:
        print("conexion closed")
        conexion.close()

interfazSql("Select %s from %s where name like '%s%'",'name, lastname','maestro', 'd')