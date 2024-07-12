from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="select * from clientes"

    micursor.execute(sql)
    
    resultado=micursor.fetchall()

    for fila in resultado:
        print(f"id:{fila[0]} \n Nombre:{fila[1]} \n Direccion:{fila[2]} \n Tel:{fila[3]}")

except:
    print(f"Ocurrio un erro por favor intentelo mas tarde")
else:
    print ("Registos consultados corretamente")

    