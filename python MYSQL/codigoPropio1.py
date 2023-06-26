import mysql.connector
opcionBaseDeDatos = 1
if opcionBaseDeDatos == 1 :
    #Forma local
    host="localhost"
    user="l20j45"
    passwd="localTest"
    port = 3306
elif opcionBaseDeDatos == 2 :
    #Forma remota
    host="142.44.163.242"
    user="Alumno"
    passwd="AlumnoPython1@."
    port = 4000

try:
	conexion = mysql.connector.connect(
    host=host,
    user=user,
    passwd=passwd,
    port=port
)
	print("Conexión correcta")
except mysql.connector.Error as err:
	print("Ocurrió un error al conectar: ", err)
finally:
    conexion.close()