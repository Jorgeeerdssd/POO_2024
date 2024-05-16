"""""

Exite una estructura de control llama "if"
la cual evalua una condicion para encontrar el valor "true" y se se cumple 
la condicion se ejecuta la linea l las lineas de codigo

Tienes 4 tipos de variables de if 
1
2
3
4

"""""

#if simple
"""""
color =input("Ingresa un color")

if color =="rojo":
    print("Soy el color rojo")

#if compuesto

color =input("Ingresa un color")

if color =="rojo":
    print("Soy el color rojo")
else:
    print("No soy el color rojo, soy el rosa")

"""""


#if anidado
"""""
color =input("Ingresa un color")

if color =="rojo":
    print("Soy el color rojo")
    if color!="rojo":
        print("No soy el color rojo")
else:
    print("No soy el color rojo, soy el rosa")
"""""


#if y elif
#no puedes poner un elif si no tienes un if, es como e segun de pseint 
"""""
color =input("Ingresa un color")

if color =="rojo":
    print("Soy el color rojo")
elif color=="amarillo":
    print("Soy color amarilo")
elif color=="azul":
    print("soy color aazul")
elif color=="morad":
    print("soy color morado")
else:
    ("No soy ninguno de los colores")

"""""
#crear un programa que solicite el numero de la semana 
#e imprima en pantalla el dia que le corresponde 

dia=input("ingrea el numero del dia de la semana")

if dia=="1":
    print("Lunes")
elif dia=="2":
    print("martes")
elif dia=="3":
    print("miercoles")
elif dia=="4":
    print("jueves")
elif dia=="5":
    print("viernes")
elif dia=="6":
    print("sabado")
elif dia=="7":
    print("domingo")
else:
    print("dia de la semana no encontrado")
