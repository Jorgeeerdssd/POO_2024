"""
cilo while es una estructurra interectiva que se ejecuta X veces siempre y cuando la condicion se cumpla 
y se seguira ejecutando tantas veces como sea true la condicion 

SINTAXIS 
While condicion:
bloque de instrucciones


"""

contador=1
while contador<=5:
    print("@")
    contador+=1
#ejemplo 2 crear un programa que imporma los numero del 1 al 5 y los sume y al final imprima la suma 

contador=1
sum=0

while contador<=5:
    print(contador)
    sum+=contador
    contador+=1

print(f"la suma es: {sum}")


# contador=1 
# sum=0
# for contador in range (1,6):
  
#     print(contador)
#     sum+= contador

# print(f"La suma es: {sum}"
#crear un programa que imprima la tabla de multiiplicar que el usuario desee 

tabla=int(input("Ingresa el numero a multiplicar"))

contador=1
multi=0
while contador<=10:
    multi=contador*tabla
    print(f"{tabla}X{contador}={multi}")
    contador+=1

# tabla=int(input("Ingresa un numero para multiplicar"))
# contador=1
# multi=0
# for contador in range (1,11):
#     multi=contador*tabla
#     print(f"{tabla}X{contador}={multi}")