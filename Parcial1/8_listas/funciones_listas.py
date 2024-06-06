paises=["MExico", "USA", "Brasil", "China"]
numero=[100,80,3.1416,75]
varios=["UTD",True,100,0.100]

#Ordenar las listas 
# print(paises)
# paises.sort()
# print(paises)


# print(numero)
# numero.sort()
# print(numero)

# print(varios)
# varios.sort()
# print(varios)

#agregar elemneto 
print(numero)
numero.append(100)#agregar valores 
print(numero)
numero.insert(len(numero),200)#agrega un elemento al final de la lista 
print(numero)

#remover elementos
print(numero)
numero.remove(100)
print(numero)
numero.pop(5)
print(numero)