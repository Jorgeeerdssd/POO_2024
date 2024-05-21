#Hacer un programa que muestre todos los numeros entre 2 numeros que diga el usuario
n1=int(input("Ingresa un numero"))
n2=int(input("Ingresa un numero"))


if n1<n2:
    for i in range (n1,n2):
        print (i)
elif n1 > n2:
    for i in range (n2, n1):
        print(i)
