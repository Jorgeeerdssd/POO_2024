def solicitarNumeros():
    #global n1,n2
    n1=int(input("Numero # 1:"))
    n2=int(input("Numero # 2:"))
    return n1,n2

def calculadora(n1,n2,opcion):
    if opcion=="1" or opcion=="+" or opcion=="SUMA":
        return f"{n1}+{n2}={n1+n2}"
    elif opcion=="2" or opcion=="-" or opcion=="RESTA":
        return f"{n1}-{n2}={n1-n2}"
    elif opcion=="3" or opcion=="*" or opcion=="MULTIPLICACION":
        return f"{n1}*{n2}={n1*n2}"
    elif opcion=="4" or opcion=="/" or opcion=="DIVISION":
        return f"{n1}/{n2}={n1/n2}"
    elif opcion=="5" or opcion=="^^" or opcion=="Potencia":
         return pow(n1,n2)
     elif opcion=="6" or opcion=="Raiz":
         import math
         print(math.sqrt(n1))

def espereTecla():
    print("Oprima cualquier tecla para continuar ...")
    input()    