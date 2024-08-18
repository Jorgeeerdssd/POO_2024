from conexionBD import conexion, cursor

class Empleado:
    def __init__(self, nombre, puesto, salario):
        self.nombre = nombre
        self.puesto = puesto
        self.salario = salario

    def crear(self):
        try:
            cursor.execute(
                "INSERT INTO empleados VALUES (NULL, %s, %s, %s)",
                (self.nombre, self.puesto, self.salario)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al crear empleado: {e}")
            return False

    @staticmethod
    def mostrar():
        try:
            cursor.execute("SELECT * FROM empleados")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al mostrar empleados: {e}")
            return []

    @staticmethod
    def actualizar(id, nombre, puesto, salario):
        try:
            cursor.execute(
                "UPDATE empleados SET nombre=%s, puesto=%s, salario=%s WHERE id=%s",
                (nombre, puesto, salario, id)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar empleado: {e}")
            return False

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute(
                "DELETE FROM empleados WHERE id=%s",
                (id,)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al eliminar empleado: {e}")
            return False
