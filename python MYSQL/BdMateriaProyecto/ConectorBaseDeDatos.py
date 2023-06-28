import mysql.connector

selectorBaseDeDatos = 'local'
def conexion(selectorBaseDeDatos):
    if selectorBaseDeDatos == 'local':
        #Base de datos local
        host="localhost"
        user="l20j45" 
        passwd="localTest"
        port = 3306
        database='mini-siiau'
    elif selectorBaseDeDatos == 'remoto':
        #Forma remota
        host="142.44.163.242"
        user="Alumno01"
        passwd="AlumnoPython1@."
        port = 4000
        database='mini-siiau'
    conexion = mysql.connector.connect(
        host = host, 
        user = user, 
        passwd = passwd, 
        port = port,  
        database = database);
    return conexion