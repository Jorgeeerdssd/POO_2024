#una funcion es un conjuto de instrucciones agrupadas bajo un nombre en particular como un programa mas pequeño que cumpple 
#la funcio se puede reutilizar con el simple hecho de invocarla es decir mandarla llamar

#sintaxis:
#def nombredeMifuncion(Parametros):
#bloque o conjunto de instrucciones 

#Nombre de mi funcion (parametros)

#las funciones pueden ser de 4 tipos 
#1.- funciones que no recibe parametros y no regresa valor
#2.- funciones que no recibe parametos y regresa valor 
#3.- funcio que recibe parametros y no regresa valor
#4.- funcion que recibe y regresa

#1.- funciones que no recibe parametros y no regresa valor
""""
def sumaNumeros1():
    n1=int(input("Numero # 1;"))
    n2=int(input("Numero # 2;"))
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

sumaNumeros1()
"""
#2.- funciones que no recibe parametos y regresa valor 
"""""

def sumaNumeros2():
    n1=int(input("Numero # 1;"))
    n2=int(input("Numero # 2;"))
    suma=n1+n2
    return f"{n1}+{n2}={suma}"

print(sumaNumeros2)
"""
#3.- funcio que recibe parametros y no regresa valor
"""""

def sumaNumeros3(n1,n2):
    
    suma=n1+n2
    print(f"{n1}+{n2}={suma}")

num1=int(input("Numero 1:"))
num2=int(input("Numero 2"))
sumaNumeros3(num1,num2)
"""""

#4.- funcion que recibe y regresa
def sumaNumeros4(n1,n2):
    
    suma=n1+n2
    return (f"{n1}+{n2}={suma}")

num1=int(input("Numero 1:"))
num2=int(input("Numero 2:"))
print(sumaNumeros4(num1,num2))

#crear un programa que solicite a traves de una funcion la siguiente informacion
#nombre del paciente, edad, estatura, tipo de sangre, 
#Utilizar los 4 tipos de funciones.