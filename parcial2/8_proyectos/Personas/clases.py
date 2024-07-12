class Personas:
 def __init__(self, nombre,edad,tel,info_personal,informar_carrera):
    self.nombre=nombre
    self.edad=edad
    self.tel=tel
    self.info_personal=info_personal
    self.informar_carrera=informar_carrera


 
class Estudiantes:
   def __init__(self, nombre,edad,tel,info_personal,informar_carrera):
    super().__init__(self,nombre,edad,tel,info_personal,informar_carrera)
    self.informar_carrera=informar_carrera




class Docentes:
  def __init__(self, nombre,edad,tel,info_personal,info_persona,informar_modalidad,modalidad,num_empleado):
    super().__init__(self,nombre,edad,tel,info_personal,info_persona,informar_modalidad,modalidad,num_empleado)
    self.info_persona=info_persona
    self.informar_modalidad=informar_modalidad



  
