from funciones import *
from veterinaria.animales import *
from veterinaria.citas import *
from veterinaria.personas import *
from veterinaria.servicios import *
from veterinaria.veterinarias import *

def main():

    while True:
        borrarPantalla()
        print("\n:: Bienvenido a la Clínica Veterinaria ::")
        print("1. Gestionar Clientes")
        print("2. Gestionar Empleado")
        print("3. Gestionar Citas")
        print("4. Servicios")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == '1':
            borrarPantalla()
            print("\n:: GESTIÓN DE CLIENTES ::")
            print("1. Agregar Cliente")
            print("2. Actualizar datos Cliente")
            print("3. Agregar animal del Cliente")
            print("4. Eliminar animal del Cliente")
            print("5. Mostrar Cliente")
            opcion = input("Elige una opción: ")
            if opcion == '1':
                borrarPantalla()
                print("\n:: AGREGAR CLIENTE ::")
                nombre = input("Nombre del cliente: ")
                direccion = input("Dirección del cliente: ")
                telefono = input("Teléfono del cliente: ")
                tipo = input("Tipo de cliente (Regular/VIP): ")
                cliente=Clientes(nombre, direccion, telefono, tipo)
                resultado = cliente.agregarCliente()
                if resultado:
                    print(f"Cliente {nombre} agregado correctamente")
                else:
                    print("Error, por favor inténtelo de nuevo")
                esperarTecla()

            elif opcion == '2':
                borrarPantalla()
                print("\n:: ACTUALIZAR CLIENTE ::")
                id= int(input("Ingrese el ID del cliente a modificar: "))
                nombre = input("Nombre del cliente: ")
                direccion = input("Dirección del cliente: ")
                telefono = input("Teléfono del cliente: ")
                tipo = input("Tipo de cliente (Regular/VIP): ")
                resultado = Clientes.actualizarDatos(id, nombre, direccion, telefono, tipo)
                if resultado:
                    print(f"El cliente con ID {id} actualizado correctamente")
                else:
                    print("Error, por favor inténtelo de nuevo")
                esperarTecla()
            elif opcion=='3':
                borrarPantalla()
                print("\n:: AGREGAR ANIMAL::")
                nombre = input("Nombre del animal: ")
                raza = input("Raza: ")
                edad = input("Edad: ")
                id_cliente = input("ID del cliente: ")
                animal=Animales(nombre, raza, edad, id_cliente)
                resultado=animal.agregarAnimal()
                if resultado:
                    print(f"Animal {nombre} agregado correctamente al cliente ID {id_cliente}")
                else:
                    print("Error, por favor inténtelo de nuevo")
                esperarTecla()
            elif opcion == '4':
                borrarPantalla()
                print("\n:: ELIMINAR ANIMAL ::")
                id= int(input("Ingrese el ID del animal a eliminar: "))
                resultado = Animales.eliminarAnimal(id)
                if resultado:
                    print(f"El Animal con ID {id} se ha eliminado correctamente")
                else:
                    print("Error, por favor inténtelo de nuevo")
                esperarTecla()
            elif opcion=="5":
                id=input("Ingrese el id: ")
                resultados=Clientes.mostrar(id)
                for fila in resultados:
                    print(fila)
                esperarTecla()






        elif opcion == '2':
            borrarPantalla()
            print("\n:: GESTIÓN DE EMPLEADOS ::")
            print("1. Agregar Empleado")
            print("2. Actualizar datos Empleado")
            print("3. Atender cita")
            print("4. Mostrar empleados")
            opcion = input("Elige una opción: ")
            if opcion == '1':
                borrarPantalla()
                print("\n:: AGREGAR EMPLEADO ::")
                nombre = input("Nombre del empleado: ")
                direccion = input("Dirección del empleado: ")
                telefono = input("Teléfono del empleado: ")
                puesto = input("Puesto del empleado: ")
                salario = input("Salario del empleado: ")
                empleado=Empleados(nombre, direccion, telefono, puesto, salario)
                resultado = empleado.agregarEmpleado()
                if resultado:
                    print(f"Empleado {nombre} agregado correctamente")
                else:
                    print("Error, por favor inténtelo de nuevo")
                esperarTecla()
            elif opcion == '2':
                borrarPantalla()
                print("\n:: ACTUALIZAR EMPLEADO ::")
                id= int(input("Ingrese el ID del empleado a modificar: "))
                nombre = input("Nombre del empleado: ")
                direccion = input("Dirección del empleado: ")
                telefono = input("Teléfono del empleado: ")
                puesto = input("Puesto del empleado: ")
                salario = input("Salario del empleado: ")
                resultado = Empleados.actualizarDatos(id, nombre, direccion, telefono, puesto, salario)
                if resultado:
                    print(f"El empleado con ID {id} actualizado correctamente")
                else:
                    print("Error, por favor inténtelo de nuevo")
                esperarTecla()
            elif opcion== '3':
                borrarPantalla()
                print("\n:: ATENDER CITA ::")
                id_Empleado = int(input("Ingresa el ID del empleado a atender la cita: "))
                id= int(input("Ingrese el ID de la cita a atender: "))
                resultado = Empleados.atenderCita(id)
                if resultado:
                    print(f"Cita atendida correctamente")
                else:
                    print("Error, por favor inténtelo de nuevo")
                esperarTecla()
            elif opcion=="4":
                id=input("Ingrese el id: ")
                resultados=Empleados.mostrar(id)
                for fila in resultados:
                    print(fila)
                esperarTecla()
            


            


        elif opcion == '3':
            borrarPantalla()
            print("\n:: GESTIÓN DE CITAS ::")
            print("1. Agendar cita")
            print("2. Cancelar cita")
            print("3. Confirmar cita")
            opcion = input("Elige una opción: ")
            if opcion == '1':
                borrarPantalla()
                print("\n:: AGENDAR CITA ::")
                fecha = input("Fecha de la cita: ")
                id_cliente = input("ID del cliente: ")
                id_animal = input("ID del animal: ")
                id_empleado = input("ID del empleado: ")
                id_servicio = input("ID del servicio: ")
                cita=Citas(fecha, id_cliente, id_animal, id_empleado, id_servicio)
                resultado = cita.programarCita()
                if resultado:
                    print(f"Cita agendada correctamente")
                else:
                    print("Error, por favor inténtelo de nuevo")
                esperarTecla()
            elif opcion== '2':
                borrarPantalla()
                print("\n:: CANCELAR CITA ::")
                id= int(input("Ingrese el ID de la cita a cancelar: "))
                resultado = Citas.cancelarCita(id)
                if resultado:
                    print(f"Cita cancelada correctamente")
                else:
                    print("Error, por favor inténtelo de nuevo")
                esperarTecla()
            elif opcion== '3':
                borrarPantalla()
                Citas.confirmarCita()
                esperarTecla()
            





        elif opcion == '4':
            borrarPantalla()
            print("\n:: SERVICIOS ::")
            servicios=Servicios.mostrarServicios()
            if len(servicios) > 0:
                print(f"\n\tLista de servicios:")
                print("1.- Agregar Nuevo Servicio")
                print("2.- Actualizar costo")
                for ser in servicios:
                    print(f"{ser[0]+2}.- {ser[1]}")
            else:
                print("\n\t**No existen servicios registrados.")
            opcion = input("Elige una opción: ")
            if opcion == '1':
                borrarPantalla()
                print("\n:: AGREGAR NUEVO SERVICIO ::")
                nombre = input("Nombre del servicio: ")
                descripcion = input("Descripción del servicio: ")
                costo = input("Costo: ")
                tipo = input("Tipo: ")
                duracion = input("Duración: ")
                servicio=Servicios(nombre, descripcion, costo, tipo, duracion)
                resultado = servicio.agregarServicio()
                if resultado:
                    print(f"Servicio agregado correctamente")
                else:
                    print("Error, por favor inténtelo de nuevo")
                esperarTecla()
            elif opcion == '2':
                borrarPantalla()
                print("\n:: ACTUALIZAR COSTO DE SERVICIO ::")
                id= int(input("Ingrese el ID del servicio a modificar: "))
                costo=float(input("Ingrese el nuevo costo del servicio: "))
                resultado = Servicios.actualizarCosto(id, costo)
                if resultado:
                    print(f"El costo se ha actualizado correctamente")
                else:
                    print("Error, por favor inténtelo de nuevo")
                esperarTecla()
            elif opcion== '3':
                borrarPantalla()
                print("\n:: ADMINISTRAR VACUNA ::")
                id= int(input("Ingrese el ID de la cita de la vacuna: "))
                resultado = Vacunas.administrarVacuna(id)
                if resultado:
                    print(f"Vacuna aplicada correctamente")
                else:
                    print("Error, por favor inténtelo de nuevo")
                esperarTecla()
            elif opcion== '4':
                borrarPantalla()
                print("\n:: REALIZAR CONSULTA ::")
                id= int(input("Ingrese el ID de la cita de la consulta: "))
                resultado = Consultas.realizarConsulta(id)
                if resultado:
                    print(f"Consulta realizada correctamente")
                else:
                    print("Error, por favor inténtelo de nuevo")
                esperarTecla()
            
            


        elif opcion == '5':
            print("Bye")
            break
        else:
            print("Opción No válida")
            esperarTecla()


if __name__ == "__main__":
    main()






