#Ejemplo 4: crear un programa que permita Gestionar (administrar) peliculas, color un meno de opciones para agregar,
#remover, consuktar peliculaa
#nota
#1.- Utilizar funciones y mandar llamar desde otro archivo 
#2.- Utilizar listas para almacenar los nombres de las peliculas 


peliculas=[]
opcion=True
while opcion:
    print("\n ..::: Cinemania :::.. \n 1. Peliculas Disponibles \n 2. Nueva Pelicula \n 3. Eliminar Pellicula \n 4. Editar Pelicula \n 5. Salir")
    opcion=input("\t Elige una opcion:").upper()
    if opcion==1 : 
        print("Peliculas Disponibles:",peliculas)
    elif opcion==2 :
        print("Nueva Pelicula \n año de lansamiento:")
    elif opcion==3:
        print("Eliminar Pelicula")
    elif opcion==4:
        print("Pelicula que desea editar")
    if opcion==5:
        break
        

