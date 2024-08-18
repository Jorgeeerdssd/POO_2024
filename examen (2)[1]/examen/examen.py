import mysql.connector
from mysql.connector import Error
import os, time
import getpass

try: 
    conexion = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
        database = "agencia_autos"
    )
    cursor = conexion.cursor(buffered=True)
except Error as e:
    print(f"Error {e}")

class Usuarios:
    def __init__(self, nombre, apellido, email, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.contraseña = contraseña

    def iniciar(email,contraseña):
        sql = "SELECT * FROM usuarios WHERE email = %s AND contraseña = %s "
        val = (email, contraseña)
        
        cursor.execute(sql,val)
        res = cursor.fetchone()
        if res:
            return res
        else:
            return None
    
    def registrar(self):
        sql = "INSERT INTO usuarios VALUES (null,%s,%s,%s,%s)"
        val = (self.nombre,self.apellido,self.email,self.contraseña)
        cursor.execute(sql,val)
        req = conexion.commit()
        if req:
            return True
class Autos:
    def __init__(self,matricula,marca,modelo,color,nif):
        self.matricula = matricula
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.nif = nif
    
    def insertar(self):
        sql = "INSERT INTO autos VALUES (%s,%s,%s,%s,%s)"
        val = (self.matricula,self.marca,self.modelo,self.color,self.nif)
        cursor.execute(sql,val)
        conexion.commit()
        return True

    def consultar():
        sql = "SELECT * FROM autos"
        cursor.execute(sql)
        res = cursor.fetchall()
        return res
    
    def actualizar(self):
        sql = "UPDATE autos SET marca = %s, modelo = %s, color =%s  WHERE matricula = %s"
        val = (self.marca, self.modelo,self.color,self.matricula)
        cursor.execute(sql,val)
        conexion.commit()
        return True

    def eliminar(matricula):
        sql = "DELETE FROM autos WHERE matricula = %s "
        val = (matricula, )
        cursor.execute(sql,val)
        conexion.commit()
        return True

class Revisiones:
    def __init__(self,norevision,cambiofiltro,cambioaceite,cambiofrenos,otros):
        self.norevision = norevision
        self.cambiofiltro = cambiofiltro
        self.cambioaceite = cambioaceite
        self.cambiosfrenos = cambiofrenos
        self.otros = otros
    
    def insertar(self, matricula):
        sql = "INSERT INTO autos VALUES (%s,%s,%s,%s,%s,%s)"
        val = (self.norevision,self.cambiofiltro,self.cambioaceite,self.cambiosfrenos,self.otros, matricula)
        cursor.execute(sql,val)
        conexion.commit()
        return True

    def consultar():
        sql = "SELECT * FROM revisiones"
        cursor.execute(sql)
        res = cursor.fetchall()
        return res
    
    def actualizar(self):
        sql = "UPDATE revisiones SET cambiofiltro = %s, cambioaceite = %s, cambiofrenos =%s, otros = %s  WHERE no_revision = %s"
        val = (self.cambiofiltro, self.cambioaceite,self.cambiosfrenos,self.otros,)
        cursor.execute(sql,val)
        conexion.commit()
        return True

    def eliminar(norevision):
        sql = "DELETE FROM autos WHERE matricula = %s "
        val = (norevision, )
        cursor.execute(sql,val)
        conexion.commit()
        return True
    


class Clientes:
    def __init__(self, nif,nombre,direccion,ciudad,tel):
        self.nif = nif
        self.nombre = nombre
        self.direccion = direccion
        self.ciudad = ciudad
        self.tel = tel

    def insertar(self):
        sql = "INSERT INTO clientes VALUES (%s,%s,%s,%s,%s)"
        val = (self.nif,self.nombre,self.direccion,self.ciudad,self.tel)
        cursor.execute(sql,val)
        conexion.commit()
        return True

    def consultar():
        sql = "SELECT * FROM clientes"
        cursor.execute(sql)
        res = cursor.fetchall()
        return res
    
    def actualizar(self):
        sql = "UPDATE clientes SET nombre = %s, direccion = %s, ciudad =%s, tel=%s  WHERE nif = %s"
        val = (self.nombre, self.direccion,self.ciudad,self.tel,self.nif)
        cursor.execute(sql,val)
        conexion.commit()
        return True

    def eliminar(nif):
        sql = "DELETE FROM clientes WHERE nif = %s "
        val = (nif, )
        cursor.execute(sql,val)
        conexion.commit()
        return True

def main():
    while True:
        os.system("cls")
        print("""
            1.- Iniciar
            2.- Registrar
            3.- Salir
        """)
        option = input("Ingresa una opcion: ").upper()
        os.system("cls")
        if option == "1" or option == "INICIAR":
            email = input("Email: ")
            contraseña = getpass.getpass("Contraseña: ")     
            req = Usuarios.iniciar(email,contraseña)
            if len(req) > 0:
                menu_usuario(req[1],req[2])
            else: 
                print("Email o Contraseña incorrectos...")
                time.sleep(2)
        elif option == "2" or option == "REGISTRAR":
            os.system("cls")
            name = input("\t\t Nombre: ")
            lastname = input("\t\t Apellido: ")
            email = input("\t\t EMAIL: ")
            contraseña = getpass.getpass("\t\t CONTRASEÑA:")
            req = Usuarios(name,lastname,email,contraseña)
            res = req.registrar()
            if res:
                os.system("cls")
                print("\t\tRegistro exitoso")
                input("Presiona una tecla")
        elif option == "3" or option == "SALIR":
            print("GRACIAS POR USAR AGENCIA DE AUTOS")
            break
def menu_usuario(name, lastname):
    while True:
        os.system("cls")
        print(f"\t\t BIENVENIDO {name} {lastname} A LA AGENCIA DE AUTOS")
        print(""" 
            1.- Clientes
            2.- Autos
            3.- Revisiones
            4.- salir
            """)
        option = input("Ingresa tu opcion: ").upper()
        if option == "1" or option == "CLIENTES":
            while True:
                os.system("cls")
                print("""
                    1.- Insertar
                    2.- Consultar
                    3.- Actualizar
                    4.- Eliminar
                    5.- Salir
                """)
                option = input("Elige una opcion: ")
            
                os.system("cls")
                if option == "1" or option == "INSERTAR":
                    os.system("cls")
                    nif = input("Ingresa el NIF del usuario (5 digitos): ")
                    nombre= input("Ingresa el nombre del cliente: ")
                    direccion = input("Ingresa la direccion del cliente: ")
                    ciudad = input("Ingresa la ciudad del cliente: ")
                    tel = input("Ingresa el telefono del cliente: ")
                    req = Clientes(nif,nombre,direccion,ciudad,tel)
                    res = req.insertar()
                    if res:
                        print("Se ha agregado el usuario correctamente")
                        input("Presiona una tecla")
                elif option == "2" or option == "CONSULTAR":
                    os.system("cls")
                    req = Clientes.consultar()
                    for x in req:
                        print(f"NIF: {x[0]}")
                        print(f"Nombre: {x[1]}")
                        print(f"direccion: {x[2]}")
                        print(f"Ciudad: {x[3]}")
                        print(f"Telefono: {x[4]}")
                        print("\n")
                    input("\n\t\t Presiona una tecla")

                elif option == "3" or option == "ACTUALIZAR":
                    os.system("cls")
                    nif = input("Ingresa el NIF del usuario a actualizar: ")
                    nombre = input("Ingresa el nuevo nombre: ")
                    direccion = input("Ingresa la direccion: ")
                    ciudad = input("Ingresa la ciudad: ")
                    tel = input("Ingresa el telefono: ")
                    req = Clientes(nif,nombre,direccion,ciudad,tel)
                    res = req.actualizar()
                    if res: 
                        print("Se ha actualizado correctamente el usuario... ")
                        input("\nPresiona una tecla")


                elif option == "4" or option == "Eliminar":
                    os.system("cls")
                    nif = input("Ingresa el NIF del usuario a eliminar: ")
                    req = Clientes.eliminar(nif)
                    if req:
                        print("El usuario se ha borrado correctamente")
                        input("Presiona una tecla")
                elif option == "5" or option == "SALIR":
                    os.system("cls")
                    break
        elif option == "2" or option == "AUTOS":
            while True:
                os.system("cls")
                print("""
                1.- Insertar
                2.- Consultar
                3.- Actualizar
                4.- Eliminar
                5.- Salir
                """)
                option = input("Elige una opcion: ")
                
                if option == "1" or option == "INSERTAR":
                    os.system("cls")
                    matricula = input("Ingresa la matricula (7 digitos): ")
                    marca= input("Ingresa la marca: ")
                    modelo = input("Ingresa el modelo: ")
                    color = input("Ingresa el color: ")
                    nif = input("Ingresa el nif del cliente: ")
                    req = Autos(matricula,marca,modelo,color,nif)
                    res = req.insertar()
                    if res:
                        print("Se ha agregado el usuario correctamente")
                        input("Presiona una tecla")
                elif option == "2" or option == "CONSULTAR":
                    os.system("cls")
                    req = Autos.consultar()
                    for x in req:
                        print(f"Matricula: {x[0]}")
                        print(f"Marca: {x[1]}")
                        print(f"Modelo: {x[2]}")
                        print(f"Color: {x[3]}")
                        print(f"nif: {x[4]}")
                        print("\n")
                    input("\n\t\t Presiona una tecla")

                elif option == "3" or option == "ACTUALIZAR":
                    os.system("cls")
                    matricula = input("Ingresa la matricula (7 digitos): ")
                    marca= input("Ingresa la nueva marca: ")
                    modelo = input("Ingresa el nuevo modelo: ")
                    color = input("Ingresa el nuevo color: ")
                    nif=""
                    req = Autos(matricula,marca,modelo,color,nif)
                    res = req.actualizar()
                    if res: 
                        print("Se ha actualizado correctamente el usuario... ")
                        input("\nPresiona una tecla")


                elif option == "4" or option == "Eliminar":
                    os.system("cls")
                    matricula = input("Ingresa la matricula carro del usuario a eliminar: ")
                    req = Autos.eliminar(matricula)
                    if req:
                        print("El usuario se ha borrado correctamente")
                        input("Presiona una tecla")
                elif option == "5" or option == "SALIR":
                    os.system("cls")
                    break
    
        elif option == "3" or option == "RESIVIONES":
            while True:
                os.system("cls")
                print("""
                1.- Insertar
                2.- Consultar
                3.- Actualizar
                4.- Eliminar
                5.- Salir
                """)
                option = input("Elige una opcion: ")

                if option == "1" or option == "INSERTAR":
                    os.system("cls")
                    norevision = input("Ingresa el no de revision: ")
                    cambiofiltro= input("Cambio de filtro? (S/N): ")
                    cambioaceite = input("Cambio de aceite? (S/N): ")
                    cambiofrenos = input("Cambio frenos? (S/N): ")
                    otros = input("Otros: ")
                    matricula = input("Matricula :")
                    req = Revisiones(norevision,cambiofiltro,cambioaceite,cambiofrenos,otros)
                    res = req.insertar(matricula)
                    if res:
                        print("Se ha agregado el usuario correctamente")
                        input("Presiona una tecla")
                elif option == "2" or option == "CONSULTAR":
                    os.system("cls")
                    req = Revisiones.consultar()
                    for x in req:
                        print(f"No Revision: {x[0]}")
                        print(f"cambio de filtro: {x[1]}")
                        print(f"Cambio de aceite: {x[2]}")
                        print(f"Cambio de frenos: {x[3]}")
                        print(f"Otros: {x[4]}")
                        print(f"Matricula: {x[5]}")
                        print("\n")
                    input("\n\t\t Presiona una tecla")

                elif option == "3" or option == "ACTUALIZAR":
                    os.system("cls")
                    norevision = input("Ingresa el no de revision: ")
                    cambiofiltro= input("Cambio de filtro? (S/N): ")
                    cambioaceite = input("Cambio de aceite? (S/N): ")
                    cambiofrenos = input("Cambio frenos? (S/N): ")
                    otros = input("Otros: ")
                    req = Revisiones(norevision,cambiofiltro,cambioaceite,cambiofrenos,otros)
                    res = req.actualizar()
                    if res: 
                        print("Se ha actualizado correctamente el usuario... ")
                        input("\nPresiona una tecla")


                elif option == "4" or option == "Eliminar":
                    os.system("cls")
                    nif = input("Ingresa la matricula carro del usuario a eliminar: ")
                    req = Revisiones.eliminar(norevision)
                    if req:
                        print("El usuario se ha borrado correctamente")
                        input("Presiona una tecla")
                elif option == "5" or option == "SALIR":
                    os.system("cls")
                    break
        elif option == "4" or option == "SALIR":
            os.system("cls")
            print("CERRANDO SESION...")
            time.sleep(2)
            break
if __name__ == "__main__":
    main()