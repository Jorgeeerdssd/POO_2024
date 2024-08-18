from conexionBD import *

class Animales:
    def __init__(self, nombre, raza, edad, id_cliente):
        self.nombre=nombre
        self.raza=raza
        self.edad=edad
        self.id_cliente=id_cliente

    def agregarAnimal(self):
        try:
            cursor.execute(
                "INSERT INTO Animales VALUES(NULL, %s, %s, %s, %s)",
                (self.nombre, self.raza, self.edad, self.id_cliente)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al agregar animal: {e}")
            return False
        
    @staticmethod
    def eliminarAnimal(id):
        try:
            cursor.execute(
                "DELETE FROM Animales WHERE id=%s",
                (id,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar animal: {e}")
            return False
        
    def actualizarHistorial(id_animal, fecha, detalle):
        try:
            cursor.execute(
                "INSERT INTO Historial_Animales VALUES(NULL, %s, %s, %s)",
                (id_animal, fecha, detalle)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar historial: {e}")
            return False





