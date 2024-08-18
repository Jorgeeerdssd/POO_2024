import tkinter as tk
from tkinter import messagebox,ttk
from modelos import Proveedores, Productos, Ventas, DetallesVentas
from usuarios import Usuarios
import re


def isEmail(correo):
    val = r'^[a-zA-Z0-9._%+-]+@+[a-zA-Z]+\.[a-zA-Z]{2,}$'
    if re.match(val, correo):
        return True
    else: 
        return False
    


class Aplicacion(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("FRUTIMAX")
        self.geometry("1920x1080")
        self.mostrar_menu_inicio()

    def mostrar_menu_inicio(self):
        self.limpiar_pantalla()
        tk.Label(self, text="..::FRUTIMAX::..", font=("Arial", 16)).pack(pady=20)
        tk.Button(self, text="Registrarse", command=self.mostrar_registro).pack(pady=10)
        tk.Button(self, text="Iniciar sesión", command=self.mostrar_login).pack(pady=10)
        tk.Button(self, text="Salir del sistema", command=self.quit).pack(pady=10)

    def mostrar_login(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Inicio de sesión", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="Correo:").pack()
        self.correo_entry = tk.Entry(self)
        self.correo_entry.pack(pady=5)
        tk.Label(self, text="Contraseña:").pack()
        self.contrasena_entry = tk.Entry(self, show='*')
        self.contrasena_entry.pack(pady=5)
        tk.Button(self, text="Iniciar sesión", command=self.login).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_inicio).pack(pady=10)


    def login(self):
        correo = self.correo_entry.get()
        contrasena = self.contrasena_entry.get()
        if isEmail(correo):
            usuario = Usuarios.verificar_credenciales(correo, contrasena)
            if usuario:
                self.mostrar_menu_cliente()
        elif isEmail(correo) == False: 
                usuario = Usuarios.verificar_credenciales_employee(correo, contrasena)
                if usuario:
                    print("SE HA ENCONTRADO UN USUARIO")
                    self.mostrar_menu_empleado()
        else:
            messagebox.showerror("Error", "Credenciales inválidas.")
    


    def mostrar_registro(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Registro de Usuario", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)
        tk.Label(self, text="Correo:").pack()
        self.correo_entry = tk.Entry(self)
        self.correo_entry.pack(pady=5)
        tk.Label(self, text="Contraseña:").pack()
        self.contrasena_entry = tk.Entry(self, show='*')
        self.contrasena_entry.pack(pady=5)
        tk.Label(self, text="Rol (empleado/cliente):").pack()
        self.rol_entry = tk.Entry(self)
        self.rol_entry.pack(pady=5)
        tk.Button(self, text="Registrar", command=self.registrar_usuario).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_inicio).pack(pady=10)

    def registrar_usuario(self):
        nombre = self.nombre_entry.get()
        correo = self.correo_entry.get()
        contrasena = self.contrasena_entry.get()
        rol = self.rol_entry.get()
        nuevo_usuario = Usuarios(nombre, correo, contrasena, rol)
        if nuevo_usuario.crear():
            messagebox.showinfo("Éxito", "Usuario registrado correctamente.")
            self.mostrar_menu_inicio()
        else:
            messagebox.showerror("Error", "No se pudo registrar el usuario.")

    def mostrar_menu_empleado(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Menú Empleado", font=("Arial", 14)).pack(pady=20)
        tk.Button(self, text="Gestión de Proveedores", command=self.mostrar_menu_proveedores).pack(pady=10)
        tk.Button(self, text="Gestión de Productos", command=self.mostrar_menu_productos).pack(pady=10)
        tk.Button(self, text="Gestión de Ventas", command=self.mostrar_menu_ventas).pack(pady=10)
        tk.Button(self, text="Gestión de Detalles de Ventas", command=self.mostrar_menu_detalles_ventas).pack(pady=10)
        tk.Button(self, text="Cerrar sesión", command=self.mostrar_menu_inicio).pack(pady=10)

    def mostrar_menu_cliente(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Menú Cliente", font=("Arial", 14)).pack(pady=20)
        tk.Button(self, text="Ver Productos", command=self.ver_productos).pack(pady=10)
        tk.Button(self, text="Cerrar sesión", command=self.mostrar_menu_inicio).pack(pady=10)

    def mostrar_menu_proveedores(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Gestión de Proveedores", font=("Arial", 14)).pack(pady=20)
        tk.Button(self, text="Ver Proveedores", command=self.ver_proveedores).pack(pady=10)
        tk.Button(self, text="Añadir Proveedor", command=self.anadir_proveedor).pack(pady=10)
        tk.Button(self, text="Actualizar Proveedor", command=self.actualizar_proveedor).pack(pady=10)
        tk.Button(self, text="Eliminar Proveedor", command=self.eliminar_proveedor).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_empleado).pack(pady=10)

    def mostrar_menu_productos(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Gestión de Productos", font=("Arial", 14)).pack(pady=20)
        tk.Button(self, text="Ver Productos", command=self.ver_productos).pack(pady=10)
        tk.Button(self, text="Añadir Producto", command=self.anadir_producto).pack(pady=10)
        tk.Button(self, text="Actualizar Producto", command=self.actualizar_producto).pack(pady=10)
        tk.Button(self, text="Eliminar Producto", command=self.eliminar_producto).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_empleado).pack(pady=10)

    def mostrar_menu_ventas(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Gestión de Ventas", font=("Arial", 14)).pack(pady=20)
        tk.Button(self, text="Ver Ventas", command=self.ver_ventas).pack(pady=10)
        tk.Button(self, text="Añadir Venta", command=self.anadir_venta).pack(pady=10)
        tk.Button(self, text="Actualizar Venta", command=self.actualizar_venta).pack(pady=10)
        tk.Button(self, text="Eliminar Venta", command=self.eliminar_venta).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_empleado).pack(pady=10)

    def mostrar_menu_detalles_ventas(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Gestión de Detalles de Ventas", font=("Arial", 14)).pack(pady=20)
        tk.Button(self, text="Ver Detalles de Ventas", command=self.ver_detalles_ventas).pack(pady=10)
        tk.Button(self, text="Añadir Detalle de Venta", command=self.anadir_detalle_venta).pack(pady=10)
        tk.Button(self, text="Actualizar Detalle de Venta", command=self.actualizar_detalle_venta).pack(pady=10)
        tk.Button(self, text="Eliminar Detalle de Venta", command=self.eliminar_detalle_venta).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_empleado).pack(pady=10)

    def ver_proveedores(self):
        self.limpiar_pantalla()
        proveedores = Proveedores.obtener_todos()
        tk.Label(self, text="Proveedores", font=("Arial", 14)).pack(pady=20)
        tree = ttk.Treeview(self, columns=("ID", "Nombre Compañía", "RFC", "Email", "Direccion", "Ciudad"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Nombre Compañía", text="Nombre Compañía")
        tree.heading("RFC", text="RFC")
        tree.heading("Email", text="Email")
        tree.heading("Direccion", text="Direccion")
        tree.heading("Ciudad", text="Ciudad")
        tree.pack(expand=True, fill='both')
        for proveedor in proveedores:
            tree.insert("", tk.END, values=(proveedor["idSupplier"], proveedor["company"], proveedor["rfc"], proveedor["email"], proveedor["address"], proveedor["city"]))
        tk.Button(self, text="Regresar", command=self.mostrar_menu_proveedores).pack(pady=10)

    def ver_productos(self):
        self.limpiar_pantalla()
        productos = Productos.obtener_todos()
        tk.Label(self, text="Productos", font=("Arial", 14)).pack(pady=20)
        tree = ttk.Treeview(self, columns=("ID", "Nombre", "Precio"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Nombre", text="Nombre")
        tree.heading("Precio", text="Precio")
        tree.pack(expand=True, fill='both', anchor="center")
        for producto in productos:
            tree.insert("", tk.END, values=(producto["idProduct"], producto["name_product"], producto["price"]))
        tk.Button(self, text="Regresar", command=self.mostrar_menu_cliente).pack(pady=10)

    def anadir_proveedor(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Añadir Proveedor", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)
        tk.Label(self, text="Apellido:").pack()
        self.apellido_entry = tk.Entry(self)
        self.apellido_entry.pack(pady=5)
        tk.Label(self, text="Compañia:").pack()
        self.nombre_compania_entry = tk.Entry(self)
        self.nombre_compania_entry.pack(pady=5)
        tk.Label(self, text="RFC:").pack()
        self.rfc_entry = tk.Entry(self)
        self.rfc_entry.pack(pady=5)
        tk.Label(self, text="Correo:").pack()
        self.correo_entry = tk.Entry(self)
        self.correo_entry.pack(pady=5)
        tk.Label(self, text="Teléfono:").pack()
        self.telefono_entry = tk.Entry(self)
        self.telefono_entry.pack(pady=5)
        tk.Label(self, text="Direccion:").pack()
        self.direccion_entry = tk.Entry(self)
        self.direccion_entry.pack(pady=5)
        tk.Label(self, text="Ciudad:").pack()
        self.ciudad_entry = tk.Entry(self)
        self.ciudad_entry.pack(pady=5)
        tk.Label(self, text="Estado:").pack()
        self.estado_entry = tk.Entry(self)
        self.estado_entry.pack(pady=5)
        tk.Label(self, text="Codigo Postal:").pack()
        self.cp_entry = tk.Entry(self)
        self.cp_entry.pack(pady=5)
        tk.Label(self, text="Pais:").pack()
        self.pais_entry = tk.Entry(self)
        self.pais_entry.pack(pady=5)
        tk.Button(self, text="Añadir", command=self.crear_proveedor).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_proveedores).pack(pady=10)

    def crear_proveedor(self):
        nombre_compania = self.nombre_compania_entry.get()
        rfc = self.rfc_entry.get()
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        correo = self.correo_entry.get()
        telefono = self.telefono_entry.get()
        direccion = self.direccion_entry.get()
        ciudad = self.ciudad_entry.get()
        estado = self.estado_entry.get()
        cp = self.cp_entry.get()
        pais = self.pais_entry.get()
        proveedor = Proveedores(nombre_compania, rfc, nombre, apellido, correo, telefono, direccion, ciudad,estado,cp,pais)
        if proveedor.crear():
            messagebox.showinfo("Éxito", "Proveedor añadido correctamente.")
            self.mostrar_menu_proveedores()
        else:
            messagebox.showerror("Error", "No se pudo añadir el proveedor.")

    def anadir_producto(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Añadir Producto", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)
        tk.Label(self, text="Precio:").pack()
        self.precio_entry = tk.Entry(self)
        self.precio_entry.pack(pady=5)
        tk.Label(self, text="ID Proveedor:").pack()
        self.id_proveedor_entry = tk.Entry(self)
        self.id_proveedor_entry.pack(pady=5)
        tk.Button(self, text="Añadir", command=self.crear_producto).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_productos).pack(pady=10)

    def crear_producto(self):
        nombre = self.nombre_entry.get()
        descripcion = self.descripcion_entry.get()
        precio = float(self.precio_entry.get())
        id_proveedor = int(self.id_proveedor_entry.get())
        producto = Productos(nombre, descripcion, precio, id_proveedor)
        if producto.crear():
            messagebox.showinfo("Éxito", "Producto añadido correctamente.")
            self.mostrar_menu_productos()
        else:
            messagebox.showerror("Error", "No se pudo añadir el producto.")

    def actualizar_proveedor(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Actualizar Proveedor", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="ID Proveedor:").pack()
        self.id_proveedor_entry = tk.Entry(self)
        self.id_proveedor_entry.pack(pady=5)
        tk.Label(self, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)
        tk.Label(self, text="Apellido:").pack()
        self.apellido_entry = tk.Entry(self)
        self.apellido_entry.pack(pady=5)
        tk.Label(self, text="Compañia:").pack()
        self.nombre_compania_entry = tk.Entry(self)
        self.nombre_compania_entry.pack(pady=5)
        tk.Label(self, text="RFC:").pack()
        self.rfc_entry = tk.Entry(self)
        self.rfc_entry.pack(pady=5)
        tk.Label(self, text="Correo:").pack()
        self.correo_entry = tk.Entry(self)
        self.correo_entry.pack(pady=5)
        tk.Label(self, text="Teléfono:").pack()
        self.telefono_entry = tk.Entry(self)
        self.telefono_entry.pack(pady=5)
        tk.Label(self, text="Direccion:").pack()
        self.direccion_entry = tk.Entry(self)
        self.direccion_entry.pack(pady=5)
        tk.Label(self, text="Ciudad:").pack()
        self.ciudad_entry = tk.Entry(self)
        self.ciudad_entry.pack(pady=5)
        tk.Label(self, text="Estado:").pack()
        self.estado_entry = tk.Entry(self)
        self.estado_entry.pack(pady=5)
        tk.Label(self, text="Codigo Postal:").pack()
        self.cp_entry = tk.Entry(self)
        self.cp_entry.pack(pady=5)
        tk.Label(self, text="Pais:").pack()
        self.pais_entry = tk.Entry(self)
        self.pais_entry.pack(pady=5)
        tk.Button(self, text="Actualizar", command=self.actualizar_proveedor_db).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_proveedores).pack(pady=10)

    def actualizar_proveedor_db(self):
        id_proveedor = int(self.id_proveedor_entry.get())
        nombre_compania = self.nombre_compania_entry.get()
        rfc = self.rfc_entry.get()
        nombre = self.nombre_entry.get()
        apellido = self.apellido_entry.get()
        correo = self.correo_entry.get()
        telefono = self.telefono_entry.get()
        direccion = self.direccion_entry.get()
        ciudad = self.ciudad_entry.get()
        estado = self.estado_entry.get()
        cp = self.cp_entry.get()
        pais = self.pais_entry.get()
        proveedor = Proveedores(nombre_compania, rfc, nombre, apellido, correo, telefono, direccion, ciudad,estado,cp,pais)
        if proveedor.actualizar(id_proveedor):
            messagebox.showinfo("Éxito", "Proveedor actualizado correctamente.")
            self.mostrar_menu_proveedores()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el proveedor.")

    def actualizar_producto(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Actualizar Producto", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="ID Producto:").pack()
        self.id_producto_entry = tk.Entry(self)
        self.id_producto_entry.pack(pady=5)
        tk.Label(self, text="Nombre:").pack()
        self.nombre_entry = tk.Entry(self)
        self.nombre_entry.pack(pady=5)
        tk.Label(self, text="Descripción:").pack()
        self.descripcion_entry = tk.Entry(self)
        self.descripcion_entry.pack(pady=5)
        tk.Label(self, text="Precio:").pack()
        self.precio_entry = tk.Entry(self)
        self.precio_entry.pack(pady=5)
        tk.Label(self, text="ID Proveedor:").pack()
        self.id_proveedor_entry = tk.Entry(self)
        self.id_proveedor_entry.pack(pady=5)
        tk.Button(self, text="Actualizar", command=self.actualizar_producto_db).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_productos).pack(pady=10)

    def actualizar_producto_db(self):
        id_producto = int(self.id_producto_entry.get())
        nombre = self.nombre_entry.get()
        descripcion = self.descripcion_entry.get()
        precio = float(self.precio_entry.get())
        id_proveedor = int(self.id_proveedor_entry.get())
        producto = Productos(nombre, descripcion, precio, id_proveedor)
        if producto.actualizar(id_producto):
            messagebox.showinfo("Éxito", "Producto actualizado correctamente.")
            self.mostrar_menu_productos()
        else:
            messagebox.showerror("Error", "No se pudo actualizar el producto.")

    def eliminar_proveedor(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Eliminar Proveedor", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="ID Proveedor:").pack()
        self.id_proveedor_entry = tk.Entry(self)
        self.id_proveedor_entry.pack(pady=5)
        tk.Button(self, text="Eliminar", command=self.eliminar_proveedor_db).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_proveedores).pack(pady=10)

    def eliminar_proveedor_db(self):
        id_proveedor = int(self.id_proveedor_entry.get())
        if Proveedores.eliminar(id_proveedor):
            messagebox.showinfo("Éxito", "Proveedor eliminado correctamente.")
            self.mostrar_menu_proveedores()
        else:
            messagebox.showerror("Error", "No se pudo eliminar el proveedor.")

    def eliminar_producto(self):
        self.limpiar_pantalla()
        tk.Label(self, text="Eliminar Producto", font=("Arial", 14)).pack(pady=20)
        tk.Label(self, text="ID Producto:").pack()
        self.id_producto_entry = tk.Entry(self)
        self.id_producto_entry.pack(pady=5)
        tk.Button(self, text="Eliminar", command=self.eliminar_producto_db).pack(pady=10)
        tk.Button(self, text="Regresar", command=self.mostrar_menu_productos).pack(pady=10)

    def eliminar_producto_db(self):
        id_producto = int(self.id_producto_entry.get())
        if Productos.eliminar(id_producto):
            messagebox.showinfo("Éxito", "Producto eliminado correctamente.")
            self.mostrar_menu_productos()
        else:
            messagebox.showerror("Error", "No se pudo eliminar el producto.")

    def limpiar_pantalla(self):
        for widget in self.winfo_children():
            widget.destroy()

# Ejecución de la aplicación
if __name__ == "__main__":
    app = Aplicacion()
    app.mainloop()
