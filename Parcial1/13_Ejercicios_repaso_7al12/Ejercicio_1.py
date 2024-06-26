#  Hacer un programa que tenga una lista de 8 numeros enteros y realice lo siguiente: 

#  a.- Recorrer la lista y mostrarla
#  b.- hacer una funcion que recorra la lista de numeros y devuelva un string
#  c.- ordenarla y mostrarla
#  d.- mostrar su longitud
#  e.- buscar algun elemento que el usuario pida por teclado

while (True):

    lista=[
        [1],
        [2],
        [52],
        [35],
        [644],
        [198],
        [998],
        [365],
    ]

    print(lista)

    for i in lista:
        print(f"{lista.index(i)+1}.-{i}")

        buscar_numero=input("Ingresa un numero a buscar: ")
    if buscar_numero in lista:
        print(f"La palabra {buscar_numero}, en la posicion {lista.count(lista)}")    

        for i in range(len(lista)):
            if buscar_numero==lista[i]:
                print(f"Se encontro en esta posicion {i}")
                
    else:
        print(f"No se encontro el numero dentro de la lista")