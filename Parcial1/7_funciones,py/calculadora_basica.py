"""""
opcion=True
while opcion:
    print ("\n\t.:: Calculadora Basica ::.\n 1.-Suma \n 2.-resta \n 3,- Multiplicacion \n 4.- Divicion\n 5.-Salir")
    opcion=input("\t Elige una opcion:").upper()

    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        n1=int(input("Numero # 1:"))
        n2=int(input("Numero # 2:"))
        print(f"{n1}+{n2}={n1+n2}")
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        n1=int(input("Numero # 1:"))
        n2=int(input("Numero # 2:"))
        print(f"{n1}-{n2}={n1-n2}")
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
        n1=int(input("Numero # 1:"))
        n2=int(input("Numero # 2:"))
        print(f"{n1}*{n2}={n1*n2}")
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        n1=int(input("Numero # 1:"))
        n2=int(input("Numero # 2:"))
        print(f"{n1}*{n2}={n1/n2}")
    else:
        print("Gracias por utilizar el sistema ...")
        opcion=False
"""""
import os
# def solicitarNumeros():
#     global n1,n2
#     n1=int(input("Numero # 1:"))
#     n2=int(input("Numero # 2:"))

# def calculadora(n1,n2,opcion):
#     if opcion=="1" or opcion=="+" or opcion=="SUMA":
        
#         return f"{n1}+{n2}={n1+n2}"
#     elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        
#         return f"{n1}-{n2}={n1-n2}"
#     elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
       
#         return f"{n1}*{n2}={n1*n2}"
#     elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        
#         return f"{n1}*{n2}={n1/n2}"
#     else:
#         opcion=False
#         return "Gracias por utilizar el sistema ..."

# def espereTecla():
#     print("Oprima cualquier tecla.")
#     input()

opcion=True
while opcion:
    os.system("clear")
    print("\n\t..::: CALCULADORA BÁSICA :::... \n 1.- Suma \n 2.- Resta \n 3.-Multiplicacion \n 4.- División \n 5.- SALIR ")
    opcion=input("\t Elige una opción: ").upper()
    solicitarNumeros()
    print(calculadora(n1,n2,opcion))