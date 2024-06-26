# Escribir un programa  que añada valores a una lista mientras que su longitud 
#  sea menor a 120, y luego mostrar la lista: Usar un while y for

# Usar un bucle while para añadir valores hasta que la longitud sea menor a 120

mi_lista=int(input("Ingresa un valor "))
while mi_lista < 120:
    mi_lista.append(len(mi_lista) + 1)


print("Lista :")
print(mi_lista)