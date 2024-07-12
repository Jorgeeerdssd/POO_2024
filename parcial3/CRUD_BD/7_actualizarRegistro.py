from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="update clientes set direccion='Col. del maestro' where id=0"

    micursor.execute(sql)
    #Es necesaio ejecutar el commin para que finalice el sql con exito
    conexion.commit()
except:
    print(f"Ocurrio un erro por favor intentelo mas tarde")
else:
    print ("Se actualizo corretamente")
