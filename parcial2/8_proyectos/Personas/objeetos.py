from clases import *

estudiante1=Estudiantes("Anna Torres Guzman", 20, "6121234567", "Meca", 233255790)
docente1=Docentes("Daniel FUentes Loera", 40, "6183335678", "TI", 123)

print(f"Estudiante: \n Nombre: {estudiante1.nombre} \n Edad: {estudiante1.edad} \n Telefono; {estudiante1.tel} \n Carrera: {estudiante1.carrera} \n Matricula: {estudiante1.matricula}" )

print(f"Docente: \n Nombre: {docente1.nombre} \n Edad: {docente1.edad} \n Telefono; {docente1.tel} \n Modalida: {docente1.modalidad} \n Numero de empleado: {docente1.num_empleado}" )