En este bloc de nota, se explicarará el funcionamiento de distintas funciones, así cómo el de las clases.

Explicación de Clases:

- clase Producto():
Esta es la clase padre, dentro de ella se inicializa los atributos nroP (número del producto), nombre, precio y cantidad.

* Metodos de la Clase Producto
Primero podrá apreciar metodos get_atributo x para devolver el valor de algún atributo, debido a que los atributos son privados y no se pueden modificar, para obtenerlos se debe de llamar a estos metodos get

metodo mostrar_info()
Este metodo como su nombre lo dice, muestra la información de los productos, principalmente el número de producto, el nombre, el precio y la cantidad que son los atributos de la cLase Producto.

metodo obtener_nombre_precio():
Este metodo devuelve solamente el nombre y el precio de un producto, esto se utilizara más tarde para el metodo mostrar_resumen de la clase Carrito.

- clase Ropa(Producto):
Esta clase hija inicializa con los atributos de la clase padre, sin embargo añade dos atributos nuevos, la talla y el genero de la ropa.

* Metodos de la Clase Ropa
No hay mucho por agregar debido a que la lógica es casi la misma que la de la clase padre Producto, lo que si es que se añade a mostrar_info los atributos nuevos de la clase hija para que se impriman con el mensaje de información

- clases Camisa(Ropa), Pantalon(Ropa), Zapato(Ropa)
Todas estas clases hijas de la clase Ropa, no cambian mucho en cuanto a metodos, y cada una tiene un atributo especifico; color para la clase Camisa, tipo de corte para la clase Pantalon y tipo para la clase Zapato.

- clase Carrito()
La clase Carrito es la encargada de manejar los productos que se le añadan para mostrarlos en una lista de un carrito, así como de calcular el total a pagar y el resumen de la compra.
Primero se inicializa la clase con el atributo "productos" que es una lista vacia donde se guardaran los productos que se vayan guardando.

* Metodos de la Clase Carrito
metodo agregar_producto()
Recibe el argumento de prodcuto cuando se le llamda, este metodo se encarga de añadir el argumento recibido a la lista de productos.

metodo calcular_total()
Guarda en una variable llamada "total" la suma realizada.
Se utiliza la funcion sum(), para luego iterar sobre "Productos", que se asume es una lista (Que como bien sabemos es, si revisamos el atributo en el constructor), por cada producto que se itera se imprime el precio del producto y con la funcion sum(), se suma todos los valores que se imprimieron.
Al final se devuelve la suma total

metodo mostrar_carrito()
Cuando es llamado este metodo, primero se itera sobre la lista de productos, imprimiendo el nombre y el precio de los productos que estan en el carrito.
Después se le pregunta al usuario si desea finalizar la comprar, si introduce 1, se finaliza y se muestra el resumen de la compra, si introduce 2, le muestra nuevamente el menu inicial.

metodo mostrar_resumen()
Similar al metodo mostrar_carrito, pero en este despues de iterar sobre la lista de productos, se imprime el total a pagar (llamando a la funcion calcular_total()) y se devuelve al menu princiapl.

- clase Tienda()
En esta clase, se inicializa con los atributos inventario (que es una lista vacia) y un atributo carrito (que pertenece a la clase Carrito()).

* Metodos de la Clase Tienda
agregar_producto_inventario()
Recibe el argumento producto, y lo añade a la lista de inventario

mostrar_inventario()
Itera sobre la lista de inventario, imprimiendo la información de cada producto dentro de la lista de inventario.
nroP es la variable que guardara el número del producto que el usuario ponga, si pone 0, se le devolvera al menú inicial, si pone otro número, se llamara al metodo seleccionar_producto()

seleccionar_producto()
Recibe el argumento nroP.
Itera sobre la lista de inventario, si el número de producto de la lista de productos del inventario, coicide con el número de producto ingresado por usuario, se llamara al metodo agregar_producto() del objeto carrito y se imprime el mensaje indicando el producto que fue añadido al carrito. Si no hay coincidencias, se imprime un mensaje indicando que no se encontro el producto.

menu():
este metodo es para mostrar el menu de la tienda, con las distinas opciones disponibles para el usuario.
