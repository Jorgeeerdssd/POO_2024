#nombre_paciente=input("Ingresa el nombre del paciente:")
#tipo_sanre=input("Ingresa el tipo de sangre:")

nuevo_paciente="si"
nuevo_paciente=="no"
while nuevo_paciente=="si":

    nombre_paciente=input("Ingresa el nombre del paciente:")
    tipo_sangre=input("Ingresa el tipo de sangre:")

    m1s=int(input("Precion arterial S:"))
    m2s=int(input("Precion arterial S:"))
    m3s=int(input("Precion arterial S:"))
    promedio_mediciones_parciales_SIStolica=(m1s+m2s+m3s)/3
    print("Promedio de las mediciones parciales SIStolica:", promedio_mediciones_parciales_SIStolica)

    m1d=int(input("Precion arterial D:"))
    m2d=int(input("Precion arterial D:"))
    m3d=int(input("Precion arterial D:"))
    promedio_mediciones_parciales_DIAstica=(m1d+m2d+m3d)/3
    print("Promedio de las mediciones parciales DIAstolica:", promedio_mediciones_parciales_DIAstica)

    mdf=int(input("Ingrese la precion final del dia:"))


    precion_final=(promedio_mediciones_parciales_DIAstica+promedio_mediciones_parciales_SIStolica+mdf)/3
    
    if promedio_mediciones_parciales_SIStolica <=120 and promedio_mediciones_parciales_DIAstica <=80:
        print("Presenta una precion normal.")
    elif promedio_mediciones_parciales_DIAstica>=80 and promedio_mediciones_parciales_SIStolica>=120:
        print("Presion alta.")
    
    print(nombre_paciente)
    print(tipo_sangre)

    nuevo_paciente=input("¿Deseas otro paciente? (si,no)").lower()
    if nuevo_paciente=="no":
        break
