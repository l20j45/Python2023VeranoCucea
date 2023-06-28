import funcionDeConexion
import mysql.connector
def interfazSql(columns,table,param):
    try:
        conexion = funcionDeConexion.conexionBd(1)
        cursor = conexion.cursor()
        sql = f"Select {columns} from {table} where name like '{param}%'"
        cursor.execute(sql)
        registros = cursor.fetchall()
        for registro in registros:
            print(registro)
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
    finally:
        print("conexion closed")
        conexion.close()

interfazSql('name, lastname','maestro', 'd')