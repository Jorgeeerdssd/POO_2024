from clientes import *

from funciones import *

def main():
    while True:
        borrarPantalla()
        print("""
      .::  Menu Principal ::. 
          1.- Insertar
          2.- Consultar
          3.- Actualizar
          4.- Eliminar (nif)
          """)
        opcion = input("\t Elige una opción: ").upper()

        
        if opcion == '1':
                borrarPantalla()
                print("\n:: AGREGAR CLIENTE ::")
                nombre = input("Nombre del cliente: ")
                direccion = input("Dirección del cliente: ")
                tel = input("Teléfono del cliente: ")
                nif = input("Nif del cliente ")
                ciudad = input("Ciudad del Clinete ")
                cliente=cliente(nombre, direccion, tel, nif, ciudad)
                resultado = agregar()
                if resultado:
                    print(f"Cliente {nombre, direccion, tel, nif, ciudad} agregado correctamente")
                else:
                    print("Error, por favor inténtelo de nuevo")
                esperarTecla()

            
        elif opcion=="2":
                nif=input("Ingrese el nif: ")
                resultados= consulta ()
                for fila in resultados:
                    print(fila)
                esperarTecla()

        elif opcion == '3' :
            borrarPantalla()
            print(f"\n \t .:: {nif}, vamos a modificar un Cliente ::. \n")
            nif = input("\t \t nif de cliente a actualizar: ")
            nombre = input("\t Nuevo nombre: ")
            direccion = input("\t Nueva direccion: ")
            tel = input("\t Nuevo celular: ")
            ciudad = input("\t Nueva ciudad: ")
  
            #Agregar codigo
            resultado=actualizardatos(nif,nombre,direccion,tel,ciudad)
            if resultado:
                print(f"\n\t\t.::Cliente actualizado correctamente::.")
            else:
                print(f"\n\t\t**No fue posible actualizar al cliente... vuelva a intentarlo**")
            esperarTecla()

        elif opcion == '4':
            borrarPantalla()
            print("\n:: ELIMINAR Nif ::")
            nif= int(input("Ingrese el NIF del Cliente a eliminar: "))
            resultado = eliminar (nif)
            if resultado:
                    print(f"El Cliente con nig {nif} se ha eliminado correctamente")
            else:
                    print("Error, por favor inténtelo de nuevo")
        
     

if __name__ == "__main__":
    main()
