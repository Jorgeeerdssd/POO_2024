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
    print(f"Error:{e}")
    print(f"Tipo de error;{type(e).__name__}")
    print(f"Ocurrio un erro por favor intentelo mas tarde")
else:
#Verificar si la conexion es correcta 

    if conexion.is_connected():
        print("Se creo la conexion exitosamente")

    else:
        print("No se pudo crear la conexion. Verificar")
