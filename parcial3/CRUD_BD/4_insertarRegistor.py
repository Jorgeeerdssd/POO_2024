from conexionBD import *

try:
    micursor=conexion.cursor()
    sql="INSERT INTO clientes (id, nombre, direccion, tel) VALUES (NULL, 'Jorge Rosales', 'Fidel Velazquez 1 Meseros 103', '6181234567')"

    micursor.execute(sql)
    #Es necesaio ejecutar el commin para que finalice el sql con exito
    conexion.commit()
except:
    print(f"Ocurrio un erro por favor intentelo mas tarde")
else:
    print ("Registo incertado corretamente")

    