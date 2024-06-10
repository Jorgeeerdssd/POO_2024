#Manejo de erroes es la forma en la que tienen los lenguajes de progamacion 
#Para evitar que sucedan errores en tiempo de ejecucion

#Ejemplo 1 Error cuando una variable no se genera

# try:
#     nombre=input("Dame el nombre: ")
#     if len(nombre)>1:
#         nombre_usuario="El nombre es: " + nombre
#     print(nombre_usuario)
# except:
#     print("Es necesario introducir un nombre de Usuario: ")


#Ejemplo 2 Cuando se soicita un numero y se introduce una letra

# try:
#     numero=int(input("Ingresa un numero: "))
#     if numero>0:
#         print("Soy un numero entero positivo")
#     else:
#         print("soy un numero entero negativo")
# except:
#     print("Ingresa un numero.")
# else:
#     print("Todo salio bien")

#Ejemplo 3 Cuando se generan multiples excepciones
try:
    numero=int(input("Dame un numero: "))

    print("El cuadrado es:"+str(numero*numero))
except ValueError:
    print("Debes de introducir un numero no se puede converitr a caracteer que no sea numerico")
except TypeError:
    print("no se puede convertir a numero entero")
else:
    print("Finalizo Correctamente")
finally:
    print("listo se termino")