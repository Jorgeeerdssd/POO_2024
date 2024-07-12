from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="delete from clientes where id=1"

    micursor.execute(sql)
    #Es necesaio ejecutar el commin para que finalice el sql con exito
    conexion.commit()
except:
    print(f"Ocurrio un erro por favor intentelo mas tarde")
else:
    print ("Se elimino corretamente")
