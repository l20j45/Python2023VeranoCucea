import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='peliculas')
	print("Conexión correcta")
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)

import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='peliculas')
	try:
		with conexion.cursor() as cursor:
			consulta = "INSERT INTO peliculas(titulo, anio) VALUES (%s, %s);"
			#Podemos llamar muchas veces a .execute con datos distintos
			cursor.execute(consulta, ("Volver al futuro 1", 1985))
			cursor.execute(consulta, ("Ready Player One", 2018))
			cursor.execute(consulta, ("It", 2017))
			cursor.execute(consulta, ("Pulp Fiction", 1994))
		conexion.commit()
	finally:
		conexion.close()
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)


import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='peliculas')
	try:
		with conexion.cursor() as cursor:
			# En este caso no necesitamos limpiar ningún dato
			cursor.execute("SELECT id, titulo, anio FROM peliculas;")
 
			# Con fetchall traemos todas las filas
			peliculas = cursor.fetchall()
 
			# Recorrer e imprimir
			for pelicula in peliculas:
				print(pelicula)
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)



import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='peliculas')
	try:
		with conexion.cursor() as cursor:
			
			consulta = "SELECT id, titulo, anio FROM peliculas WHERE anio > %s;"
			cursor.execute(consulta, (2000))
 
			# Con fetchall traemos todas las filas
			peliculas = cursor.fetchall()
 
			# Recorrer e imprimir
			for pelicula in peliculas:
				print(pelicula)
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)


import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='peliculas')
	try:
		with conexion.cursor() as cursor:
			
			consulta = "UPDATE peliculas SET titulo = %s WHERE id = %s;"
			nuevo_titulo = "Ready Player One: comienza el juego"
			id_editar = 2
			cursor.execute(consulta, (nuevo_titulo, id_editar))
 
		# No olvidemos hacer commit cuando hacemos un cambio a la BD
		conexion.commit()
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)


import pymysql
try:
	conexion = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='peliculas')
	try:
		with conexion.cursor() as cursor:
			
			consulta = "DELETE FROM peliculas WHERE anio < %s;"
			anio = 2000
			cursor.execute(consulta, (anio))
 
		# No olvidemos hacer commit cuando hacemos un cambio a la BD
		conexion.commit()
	finally:
		conexion.close()
	
except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	print("Ocurrió un error al conectar: ", e)