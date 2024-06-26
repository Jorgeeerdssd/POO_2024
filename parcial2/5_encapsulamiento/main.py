from coches import *

#Crear un objetos o instanciar la clase
print("Objeto 1")
coche1=Coches("Blanco", "VW", "2022", 220, 150, 5)
# coche1.getInfo()

# print("Objeto 2")
# coche2=Coches("Azul", "NIssan", "2020", 180, 150, 5)
# coche2.getInfo()

print(coche1.atributo_publico)
#print(coche1.__atributo_privado__)#No es posible 
print(coche1.MetodoPublico())
#cohce1_MetodoPrivado()#NO es posible
coche1.getMetodoPublico()