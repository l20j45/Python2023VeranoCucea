import ConectorBaseDeDatos
import mysql.connector
import Materia

#CRUD
def altaMateria(id,title):
    try:
        conexion = ConectorBaseDeDatos.conexion('local')
        cursor = conexion.cursor()
        sql = f"INSERT INTO Materia (id, title) VALUES ('{id}', '{title}');"
        cursor.execute(sql)
        print(sql)
        conexion.commit()
        cursor.close()
        conexion.close()
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
        cursor.close()
        conexion.close()
def verMateria(id):
    try:
        conexion = ConectorBaseDeDatos.conexion('local')
        cursor = conexion.cursor()
        cursor.execute(f'SELECT * FROM materia where id = {id}')
        registros = cursor.fetchall()
        for registro in registros:
            #materia = Materia(registro[0],registro[1])
            print(f'id = {registro[0]} titulo = {registro[1]}')
        cursor.close()
        conexion.close()
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
        cursor.close()
        conexion.close()
def verTodasMateria():
    try:
        conexion = ConectorBaseDeDatos.conexion('local')
        cursor = conexion.cursor()
        cursor.execute('SELECT * FROM materia')
        registros = cursor.fetchall()
        for registro in registros:
            #materia = Materia(registro[0],registro[1])
            print(f'id = {registro[0]} titulo = {registro[1]}')
        cursor.close()
        conexion.close()
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
        cursor.close()
        conexion.close()
def modificarMateria(id,title):
    try:
        conexion = ConectorBaseDeDatos.conexion('local')
        cursor = conexion.cursor()
        sql = f"UPDATE Materia SET id = {id} where title = '{title}';"
        cursor.execute(sql)
        print(sql)
        conexion.commit()
        cursor.close()
        conexion.close()
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
        cursor.close()
        conexion.close()
def borrarMateria(id):
    try:
        conexion = ConectorBaseDeDatos.conexion('local')
        cursor = conexion.cursor()
        sql = f"DELETE FROM materia WHERE id = '{id}'"
        cursor.execute(sql)
        print(sql)
        conexion.commit()
        cursor.close()
        conexion.close()
    except mysql.connector.Error as err:
        print("Ocurrió un error al conectar: ", err)
        cursor.close()
        conexion.close()