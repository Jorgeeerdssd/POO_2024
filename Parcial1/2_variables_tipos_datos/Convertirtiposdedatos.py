"""""
    Comentarios varias lineas de codigo 
        Nota:Al momento de concatenar no es posible incluir en algunas ocasiones contenido de variables que no sean del tipo str 

"""""

#Comentario de una linea 

#Concatenar un str con str 

texto="Soy cadena de texto"
numero=23
print(texto+"y soy una cadena")


#Concatenar un int con str 


numero=23
numero_str=str(numero)
print("EL numero: "+numero_str)

print("El numero; "+str(numero))

#Concatenar un str con int 
n1='23'
n2=33
#siempre modificar la exprecion
suma=int(n1)+n2

print ("El numero: "+str(numero))


#Concatenar un float y int con str 
n1='23'
n2=33.0

suma=int(n1)+n2

print ("El numero: "+str(numero))
print(f"El numero; {int(suma)}")

#Concatenar un float y float con float

n1='23.34'
n2='33.99'

suma=float(n1)+float(n2)

print(f"El numero; {suma}")
