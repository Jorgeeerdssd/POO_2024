

from conexionBD import *
import datetime


class cliente:
    def __init__(self, nombre, nif, direccion, ciudad, tel):
        self.nombre = nombre
        self.nif =nif
        self.direccion = direccion
        self.ciudad=ciudad
        self.tel=tel

    
def consulta(nif):
        try:
            cursor.execute(
                "DELETE FROM Citas WHERE id=%s",
                (nif,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al realizar consulta: {e}")
            return False

def actualizardatos(nif, nombre, direccion, tel, ciudad):
        try:
            cursor.execute(
                "UPDATE cliente SET nombre=%s, direccion=%s, telefono=%s, puesto=%s, salario=%s WHERE ID=%s",
                (nombre, direccion, tel, direccion, ciudad, nif)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
            return False
        

def eliminar(nif, nombre, direccion, tel, ciudad):
        try:
            cursor.execute(
                "Delate cliente SET nombre=%s, direccion=%s, telefono=%s, puesto=%s, salario=%s WHERE ID=%s",
                (nombre, direccion, tel, ciudad, nif)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar al cliente: {e}")
            return False
    
def agregar(nombre, direccion, tel, ciudad, nif):
        try:
            cursor.execute(
                "INSERT INTO Animales VALUES(NULL, %s, %s, %s, %s)",
                (nombre, direccion, tel, ciudad, nif)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al agregar animal: {e}")
            return False