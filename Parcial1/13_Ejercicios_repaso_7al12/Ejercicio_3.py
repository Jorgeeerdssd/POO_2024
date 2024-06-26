# Crear un programa para comprobar si una lista esta vacia y si esta vacia llenarla con 
#  palabras o frases hasta que el usuario asi lo crea conveniente, posteriormente imprimir 
#  el contenido de la lista en mayusculas


while (True):
    print("Ingresa La palabra o frase que deseas agregar:")

    lista=[]
    lista.append(input())

   
    opcion=input("Deseas Agregar Otra frase o palabra (si,no)").lower()
    if opcion=="no":
        print(lista)
        break