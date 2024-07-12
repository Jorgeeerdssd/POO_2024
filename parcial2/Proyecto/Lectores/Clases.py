class Lectores:
    def __init__(self, nombre, direccion, tel):
        self.nombre = nombre
        self.direccion = direccion
        self.tel = tel

    def reservar(self):
        print(f"Esta reservado el libro por: {self.getNombre()} y su telefono es: {self.getTel()}")

    def entregar(self):
        print(f"Esta entregado el libro por: {self.getNombre()} y su telefono es: {self.getTel()}")   

    def getNombre(self):
        return self.nombre
    def getDireccion(self):
        return self.direccion
    def getTel(self):
        return self.tel
    def setNombre(self,nombre):
        self.nombre=nombre    
    def setDireccion(self,direccion):
        self.direccion=direccion  
    def setTel(self,tel):
        self.tel=tel

class Estudiantes(Lectores):
    def __int__(self,nombre,direccion,tel,carrera,matricula):
        super(). __int__(self,nombre,direccion,tel)

        self._carrera=carrera
        self._matricula=matricula
    def reservar(self):
        print(f"El estudiante: {self.getNombre()} reservo un libro y su matricula es: {self.getMatricula()} de la carrera de: {self.getCarrera()}")

    def entregar(self):
        print(f"El estudiante: {self.getNombre()} entrego un libro y su matricula es: {self.getMatricula()} de la carrera de: {self.getCarrera()}")

    
    def getNombre(self):
        return self.nombre
    def getDireccion(self):
        return self.direccion
    def getTel(self):
        return self.tel
    def setNombre(self,nombre):
        self.nombre=nombre    
    def setDireccion(self,direccion):
        self.direccion=direccion  
    def setTel(self,tel):
        self.tel=tel

    def getCarrera(self):
        return self._carrera
    def getMatricula(self):
        return self._matricula
    def setCarrera(self,_carrera):
        self._carrera=_carrera
    def setMatricula(self,_matricula):
        self._matricula=_matricula

class Docentes(Lectores):
    def __int__(self,nombre,direccion,tel,modalidad,num_empleado):
        super (). __int__ (self,nombre,direccion,tel)

        self.__modalidad=modalidad
        self.__num_empleado=num_empleado

    def reservar(self):
        print(f"El docente: {self.getNombre()} reservo un libro y su numero de empleado es: {self.getNum_empleado()} de la modalidad de: {self.getModalidad()}")

    def entregar(self):
        print(f"El docente: {self.getNombre()} entrego un libro y su numero de empleado es: {self.getNum_empleado()} de la modalidad de: {self.getModalidad()}")


    def getNombre(self):
        return self.nombre
    def getDireccion(self):
        return self.direccion
    def getTel(self):
        return self.tel
    def setNombre(self,nombre):
        self.nombre=nombre    
    def setDireccion(self,direccion):
        self.direccion=direccion  
    def setTel(self,tel):
        self.tel=tel

    def getModalidad(self):
        return self.__modalidad
    def getNum_empleado(self):
        return self.__num_empleado
    def setModalidad(self,__modalidad):
        self.__modalidad=__modalidad
    def setNum_empleado(self,__num_empleado):
        self.__num_empleado=__num_empleado