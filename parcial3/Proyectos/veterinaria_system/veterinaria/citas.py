from conexionBD import *

class Citas:
    def __init__(self, fecha, id_cliente, id_animal, id_empleado, id_servicio):
        self.fecha=fecha
        self.id_cliente=id_cliente
        self.id_animal = id_animal
        self.id_empleado = id_empleado
        self.id_servicio = id_servicio

    def programarCita(self):
        try:
            cursor.execute(
                "INSERT INTO Citas VALUES (NULL, %s, %s, %s, %s, %s)",
                (self.fecha, self.id_cliente, self.id_animal, self.id_empleado, self.id_servicio)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al agendar cita: {e}")

    @staticmethod
    def cancelarCita(id):
        try:
            cursor.execute(
                "DELETE FROM Citas WHERE id=%s",
                (id,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al cancelar cita: {e}")
            return False
    @staticmethod   
    def confirmarCita():
        print("Cita confirmada")

    


