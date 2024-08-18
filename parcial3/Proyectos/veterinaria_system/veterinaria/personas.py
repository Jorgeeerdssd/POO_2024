from conexionBD import *

class Personas:
    def __init__(self,nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono


class Clientes(Personas):
    def __init__(self, nombre, direccion, telefono, tipo):
        super().__init__(nombre, direccion, telefono)
        self.tipo = tipo

    @staticmethod
    def mostrar(id):
        try:
            cursor.execute(
                "select * from clientes where id=%s",
                (id,)
            )
            return cursor.fetchall()
        except:
            return []
        
    def agregarCliente(self):
        try:
            cursor.execute(
                "INSERT INTO Clientes VALUES(NULL, %s, %s, %s, %s)",
                (self.nombre, self.direccion, self.telefono, self.tipo)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al agregar cliente: {e}")
            return False
    @staticmethod    
    def actualizarDatos(id, nombre, direccion, telefono, tipo):
        try:
            cursor.execute(
                "UPDATE Clientes SET nombre=%s, direccion=%s, telefono=%s, tipo=%s WHERE ID=%s",
                (nombre, direccion, telefono, tipo, id)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar cliente: {e}")
            return False

class Empleados(Personas):
    def __init__(self, nombre, direccion, telefono, puesto, salario):
        super().__init__(nombre, direccion, telefono)
        self.puesto = puesto
        self.salario = salario

    @staticmethod
    def mostrar(id):
        try:
            cursor.execute(
                "select * from empleados where id=%s",
                (id,)
            )
            return cursor.fetchall()
        except:
            return []
    
    def agregarEmpleado(self):
        try:
            cursor.execute(
                "INSERT INTO Empleados VALUES(NULL, %s, %s, %s, %s, %s)",
                (self.nombre, self.direccion, self.telefono, self.puesto, self.salario)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al agregar Empleado: {e}")
            return False
    
    @staticmethod    
    def actualizarDatos(id, nombre, direccion, telefono, puesto, salario):
        try:
            cursor.execute(
                "UPDATE Empleados SET nombre=%s, direccion=%s, telefono=%s, puesto=%s, salario=%s WHERE ID=%s",
                (nombre, direccion, telefono, puesto, salario, id)
            )
            conexion.commit()
            return True
        except Exception as e:
            print(f"Error al actualizar empleado: {e}")
            return False
        
    @staticmethod
    def atenderCita(id):
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
        


