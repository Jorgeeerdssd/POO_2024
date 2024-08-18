from empleados.empleado import Empleado
from funciones import borrarPantalla, esperarTecla

def menu_principal():
    while True:
        borrarPantalla()
        print("""
      .::  Menú Principal ::. 
          1.- Crear empleado
          2.- Mostrar empleados
          3.- Actualizar empleado
          4.- Eliminar empleado
          5.- Salir 
          """)
        opcion = input("\t Elige una opción: ").upper()

        if opcion == '1' or opcion == "CREAR EMPLEADO":
            borrarPantalla()
            print("\n \t ..:: Crear Empleado ::..")
            nombre = input("\t Nombre: ")
            puesto = input("\t Puesto: ")
            salario = float(input("\t Salario: "))
            empleado = Empleado(nombre, puesto, salario)
            resultado = empleado.crear()
            if resultado:
                print(f"\n\tEl empleado {nombre} se creó correctamente.")
            else:
                print(f"\n\t **Por favor inténtelo de nuevo más tarde.")
            esperarTecla()
        elif opcion == '2' or opcion == "MOSTRAR EMPLEADOS":
            borrarPantalla()
            print("\n \t ..:: Mostrar Empleados ::..")
            empleados = Empleado.mostrar()
            if len(empleados) > 0:
                print(f"\n\tLista de empleados:")
                for emp in empleados:
                    print(f"ID: {emp[0]}, Nombre: {emp[1]}, Puesto: {emp[2]}, Salario: {emp[3]}")
            else:
                print("\n\t**No existen empleados registrados.")
            esperarTecla()
        elif opcion == '3' or opcion == "ACTUALIZAR EMPLEADO":
            borrarPantalla()
            print("\n \t ..:: Actualizar Empleado ::..")
            id = int(input("\t ID del empleado a actualizar: "))
            nombre = input("\t Nuevo nombre: ")
            puesto = input("\t Nuevo puesto: ")
            salario = float(input("\t Nuevo salario: "))
            resultado = Empleado.actualizar(id, nombre, puesto, salario)
            if resultado:
                print(f"\n\tEl empleado con ID {id} se actualizó correctamente.")
            else:
                print(f"\n\t **Por favor inténtelo de nuevo más tarde.")
            esperarTecla()
        elif opcion == '4' or opcion == "ELIMINAR EMPLEADO":
            borrarPantalla()
            print("\n \t ..:: Eliminar Empleado ::..")
            id = int(input("\t ID del empleado a eliminar: "))
            resultado = Empleado.eliminar(id)
            if resultado:
                print(f"\n\tEl empleado con ID {id} se eliminó correctamente.")
            else:
                print(f"\n\t **Por favor inténtelo de nuevo más tarde.")
            esperarTecla()
        elif opcion == '5' or opcion == "SALIR":
            print("\n\t.:. ¡Gracias, adiós! ...")
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            esperarTecla()

if __name__ == "__main__":
    menu_principal()
