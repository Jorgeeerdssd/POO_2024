import mysql.connector

#Conexion con la base datos de MYSQL
try:
    conexion=mysql.connector.connect(
        host='localHost',
        user='root',
        password=''
)
    
    #Crear un objeto de nuevo de tipo cursor para ejecutar sql
    micursor=conexion.cursor()

    sql="create database bd_python"
    micursor.execute(sql)

except Exception as e:
    print(f"Error:{e}")
    print(f"Tipo de error;{type(e).__name__}")
    print(f"Ocurrio un erro por favor intentelo mas tarde")
else:
    print("Se creo la base de datos exitasosamente")
    micursor.execute("show databases")
    for x in micursor:
        print(x)
    