class Producto:
    def __init__(self, nroP, nombre, precio, cantidad):
        self.__nroP = nroP  # número de producto
        self.__nombre = nombre
        self.__precio = precio
        self.__cantidad = cantidad

    # Getters
    def get_nroP(self):
        return self.__nroP

    def get_nombre(self):
        return self.__nombre

    def get_precio(self):
        return self.__precio

    def get_cantidad(self):
        return self.__cantidad

    def mostrar_info(self):
        return f"{self.__nroP}) Nombre: {self.__nombre}, Precio: {self.__precio}, Cantidad: {self.__cantidad}"
    
    def obtener_nombre_precio(self):
        return f"Nombre: {self.__nombre}, Precio: {self.__precio}"


class Ropa(Producto):
    def __init__(self, nroP, nombre, precio, cantidad, talla, genero):
        super().__init__(nroP, nombre, precio, cantidad)
        self.__talla = talla
        self.__genero = genero

    def get_talla(self):
        return self.__talla

    def get_genero(self):
        return self.__genero

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Talla: {self.__talla}, Para: {self.__genero}\n"


class Camisa(Ropa):
    def __init__(self, nroP, nombre, precio, cantidad, talla, color, genero):
        super().__init__(nroP, nombre, precio, cantidad, talla, genero)
        self.__color = color

    def mostrar_info(self):
        return f"{super().mostrar_info()}---Color: {self.__color}\n"


class Pantalon(Ropa):
    def __init__(self, nroP, nombre, precio, cantidad, talla, tipo_corte, genero):
        super().__init__(nroP, nombre, precio, cantidad, talla, genero)
        self.__tipo_corte = tipo_corte

    def mostrar_info(self):
        return f"{super().mostrar_info()}---Tipo de corte: {self.__tipo_corte}\n"


class Zapato(Ropa):
    def __init__(self, nroP, nombre, precio, cantidad, talla, tipo, genero):
        super().__init__(nroP, nombre, precio, cantidad, talla, genero)
        self.__tipo = tipo

    def mostrar_info(self):
        return f"{super().mostrar_info()}---Tipo: {self.__tipo}\n"


class Carrito: # Añadir una función para revisar el carrtio
    def __init__(self):
        self.__productos = []

    def agregar_producto(self, producto):
        self.__productos.append(producto)

    def calcular_total(self):
        total = sum(producto.get_precio() for producto in self.__productos)
        return total

    def mostrar_carrito(self):
        for producto in self.__productos:
            print(producto.obtener_nombre_precio())
        print("\nDesea finalizar la compra?")
        opcion = input("1. Si / 2. No:")
        if  opcion == "1":
            print("Compra realizada con exito")
            self.mostrar_resumen()
        else:
            print("Volviendo al menú\n")
            tienda.menu()

    def mostrar_resumen(self):
        print("Resumen de la compra:")
        for producto in self.__productos:
            print(producto.obtener_nombre_precio())
        print(f"Total a pagar: {self.calcular_total()}")
        print("Gracias por su compra\n")



class Tienda:
    def __init__(self):
        self.__inventario = []
        self.__carrito = Carrito()

    def agregar_producto_inventario(self, producto):
        self.__inventario.append(producto)

    def mostrar_inventario(self):
        print("Productos disponibles:")
        for producto in self.__inventario:
            print(producto.mostrar_info())
        nroP = input("\nSeleccione el número de un producto para añadir al carrito (0 para volver al menú)")
        while True:
            if nroP == "0":
                tienda.menu()
                break
            else:
                try:
                    tienda.seleccionar_producto(nroP)
                    break
                except ValueError:
                    print("Número de producto no válido")

    def seleccionar_producto(self, nroP):
        for producto in self.__inventario:
            if producto.get_nroP() == nroP:
                self.__carrito.agregar_producto(producto)
                print(f"Producto '{producto.get_nombre()}' agregado al carrito.\n")
                return
        print("Producto no encontrado. O sin existencias")
    
    def menu(self):
        while True:
            print("Bienvenido a la tienda!")
            print("1. Ver inventario")
            print("2. Ver Carrtio")
            print("3. Salir de la tienda")
            opcion = input("Seleccione una opción:")
            if opcion == "1":
                self.mostrar_inventario()

            elif opcion == "2":
                self.__carrito.mostrar_carrito()
            elif opcion == "3":
                print("Saliendo de la tienda...")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida. (Número del 1 al 3)")


tienda = Tienda()

# Agregar productos al inventario, esta lógica fue cambiada, no es igual al ejemplo utilizado en la tarea
tienda.agregar_producto_inventario(Camisa("1", "Camisa Azul", 25.00, 10, "M", "Azul", "Hombre"))
tienda.agregar_producto_inventario(Camisa("2", "Camisa Roja", 28.00, 5, "L", "Rojo", "Hombre"))
tienda.agregar_producto_inventario(Pantalon("3", "Vaquero Gris", 40.00, 20, "M", "Skinny", "Hombre"))
tienda.agregar_producto_inventario(Zapato("4", "Zapato Deportivo", 60.00, 15, "42", "Deportivo", "Hombre"))
tienda.agregar_producto_inventario(Zapato("5", "Zapato Formal", 75.00, 10, "37", "Formal", "Mujer"))

tienda.menu()


    
