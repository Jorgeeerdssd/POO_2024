# Crear una lista y un diccionario con el contenido de esta tabla: 

#   ACCION              TERROR        DEPORTES
#   MAXIMA VELOCIDAD    LA MONJA       ESPN
#   ARMA MORTAL 4       EL CONJURO     MAS DEPORTE
#   RAPIDO Y FURIOSO I  LA MALDICION   ACCION


#   imprimir la información

# Catalogo=[
#     ["Accion"], ["Terror"], ["Deportes"],
#     ["Maxima Velocidad"], ["La monja"], ["ESPN"],
#     ["Arma Mortal 4"], ["El conjuro"], ["Mas deporte"],
#     ["Rapido y Fusioso I"], ["LA maldicion"], ["Accion"],
# ]

# print(Catalogo)

catalogo={
    "ACCION",   "TERROR",   "DEPORTES",
    "MAXIMA VELOCIDAD",    "LA MONJA",       "ESPN",
    "ARMA MORTAL 4",       "EL CONJURO",    "MAS DEPORTE",
    "RAPIDO Y FURIOSO I",  "LA MALDICION",   "ACCION",

}

print(catalogo)


catalogo["Nueva pelicula"]=str(input("Infresa la nueva peliucla"))
borrarPantalla = lambda: os.system ("cls")