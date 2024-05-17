"""
cilo for estructurra interectiva que se ejecuta X veces 

SINTAXIS 
for variables in elemento_iterables(lista, rango, etc.):
bloque de instrucciones

"""

contador=1
for contador in range (1,6):
    print("@")

#ejemplo 2 crear un programa que imporma los numero del 1 al 5 y los sume y al final imprima la suma 

contador=1 
sum=0
for contador in range (1,6):
  
    print(contador)
    sum+= contador

print(f"La suma es: {sum}")

#crear un programa que imprima la tabla de multiiplicar que el usuario desee 
tabla=int(input("Ingresa un numero para multiplicar"))
contador=1
multi=0
for contador in range (1,11):
    multi=contador*tabla
    print(f"{tabla}X{contador}={multi}")

