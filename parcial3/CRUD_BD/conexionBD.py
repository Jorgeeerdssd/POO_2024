import mysql.connector

#Conexion con la base datos de MYSQL
try:
    conexion=mysql.connector.connect(
         host='localHost',
        user='root',
        password='',
        database='bd_python'
)
except Exception as e:
    
    print(f"Ocurrio un erro por favor intentelo mas tarde")
