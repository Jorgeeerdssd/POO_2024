"""""

list (Array)
son colleciones o conjunto de daros/valores bajo 
un mismi nombre, para acceder a valores se 
hace un indice numerico


nota; sus valores si son modificanles 

la lista es una coleccion ordenada y modificacbles, Permite Miembros duplicados

"""""
#Ejemlo 1 crear una lista con valores numericos enteros e imprimir la lista

#numeros=[23,24]
#print(numeros)

#recorrer la lista con un for
# for i in numeros:
#     print(i)

#recorrer las lista con un while 

# i=0
# while i<len(numeros):
#     print(numeros[i])
#     i+=1

#ejemplo 2 ingresar una lista en la palabra, posterior mente ingresar una palabra 
#para buscar la coincidencia en la lista E si aparece la palabra y en que posicion en caco conrtrario indicar una sola 
#si no la encontro 

# while (True):
#     palabra=["hola","2024","10.23","True","hola","hola"]
#     palabra_buscar=input("Ingresa la palabra a mostrar: ")

#     if palabra_buscar in palabra :
#         print(f"La palabra {palabra_buscar}, en la posicion {palabra.count(palabra)}")    

#         for i in range(len(palabra)):
#             if palabra_buscar==palabra[i]:
#                 print(f"Se encontro en esta posicion {i}")
            
#     else:
#         print(f"No se encontro la palabra dentro de la lista")
  
#Ejemplo 3, lista multilinea o multidimensional (matriz) para crear una agrenda telefonica

# agenda=[
#     ["Carlos",9168316843],
#     ["Fernanado",618351684],
#     ["Matias",1684312248],
#     ["Juan",1563248621]
# ]

# print(agenda)

# for i in agenda:
#     print(f"{agenda.index(i)+1}.-{i}")

#Ejemplo 4: crear un programa que permita Gestionar (administrar) peliculas, color un meno de opciones para agregar,
#remover, consuktar peliculaa
#nota
#1.- Utilizar funciones y mandar llamar desde otro archivo 
#2.- Utilizar listas para almacenar los nombres de las peliculas 

def nuevaPelicula():
    peliculas.append(pelicula)
    espera