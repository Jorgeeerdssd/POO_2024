import conexionBD

try:
    micursor=conexionBD.conexion.cursor()
    sql="create table clientes(id int primary key auto_increment, nombre varchar (60), direccion varchar(120), tel varchar(10)) "

    micursor.execute(sql)
except:
    print(f"Ocurrio un erro por favor intentelo mas tarde")
else:
    print ("se creo la tabla exirosamente")