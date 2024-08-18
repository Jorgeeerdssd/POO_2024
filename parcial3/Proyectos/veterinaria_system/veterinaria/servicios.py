from conexionBD import *

class Servicios:
    def __init__(self, nombre, descripcion, costo, tipo, duracion):
        self.nombre=nombre
        self.descripcion=descripcion
        self.costo=costo
        self.tipo=tipo
        self.duracion=duracion

    def agregarServicio(self):
        try:
            cursor.execute(
                "INSERT INTO Servicios VALUES(NULL, %s, %s,%s, %s, %s)",
                (self.nombre, self.descripcion, self.costo, self.tipo, self.duracion)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al agregar servicio{e}")
            return False
    
    @staticmethod
    def actualizarCosto(id, costo):
        try:
            cursor.execute(
                "UPDATE Servicios SET costo=%s WHERE id=%s",
                (costo, id)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar costo: {e}")
            return False
        
    @staticmethod
    def mostrarServicios():
        try:
            cursor.execute("SELECT * FROM Servicios")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al mostrar servicios: {e}")
            return []


class Vacunas(Servicios):
    def __init__(self, nombre, descripcion, costo, tipo):
        super().__init__(nombre, descripcion, costo)
        self.tipo = tipo


    @staticmethod
    def administrarVacuna(id):
        try:
            cursor.execute(
                "DELETE FROM Citas WHERE id=%s",
                (id,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al administrar vacuna: {e}")
            return False
        
class Consultas(Servicios):
    def __init__(self, nombre, descripcion, costo, duracion):
        super().__init__(nombre, descripcion, costo)
        self.duracion = duracion


    @staticmethod
    def realizarConsulta(id):
        try:
            cursor.execute(
                "DELETE FROM Citas WHERE id=%s",
                (id,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al realizar consulta: {e}")
            return False



