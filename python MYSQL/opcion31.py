import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password"
)

c = db.cursor()
c.execute("CREATE DATABASE employee_db")

db.close()