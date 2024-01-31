# Definiremos una lista vacía para almacenar los productos
inventario = []

# Creamos una función para agregar un producto al inventario
def agregar_producto(nombre, categoria, cantidad, precio):

  # vamos a verificar si el producto ya existe en el inventario para evitar tener duplicados

  # utilizaremos el ciclo FOR

  for producto in inventario:
    if producto["nombre"] == nombre:
      print("El producto ya existe en el inventario.")
      return

  # Si no existe el producto en el sistema, entonces vamos a crear un diccionario con los datos del producto

  producto = {
    "nombre": nombre,
    "categoria": categoria,
    "cantidad": cantidad,
    "precio": precio
  }

  # Agregaremos el diccionario a la lista del inventario
  inventario.append(producto)
  print("Nuestro producto se ha agregado al inventario exitosamente.")

# Crearemos una función para eliminar un producto del inventario

def eliminar_producto(nombre):

  # para buscar el producto por su nombre en el inventario utilizaremos el ciclo FOR

  for producto in inventario:
    if producto["nombre"] == nombre:

      # Para Eliminar el producto de la lista del inventario usaremos REMOVE

      inventario.remove(producto)

      print("Nuestro producto se ha eliminado del inventario exitosamente.")
      return

  # Si no se encuentra el producto, vamos a mostrar un mensaje

  print("El producto no se encuentra en el inventario.")
  
  # crearemos una función para buscar un producto por nombre o categoría
  
def buscar_producto(criterio):
  
  # vamos a crear una lista vacía para almacenar los resultados
  
  resultados = []
  
  # Recorremos el inventario y compararemos el criterio con el nombre o la categoría de cada producto 
  
  for producto in inventario:
    if criterio == producto["nombre"] or criterio == producto["categoria"]:
      
      # Si hay una coincidencia, agregaremos el producto a la lista de resultados
      
      resultados.append(producto)
      
  # Si la lista de resultados está vacía, arrojaremosr un mensaje
  
  if len(resultados) == 0:
    print("No pudimos encontrar el siguiente producto: ", criterio)
    
  # Si nuestra lista de resultados tiene elementos, los mostraremos
  
  else:
    print(" encontrsnos los siguientes productos: ", criterio)
    for producto in resultados:
      print(producto)

# vamos a crear una función para actualizar la cantidad en stock y el precio de un producto
def actualizar_producto(nombre, cantidad, precio):
  # Buscaremos el producto por su nombre en el inventario
  for producto in inventario:
    if producto["nombre"] == nombre:
      # Modificaremos la cantidad y el precio del producto
      producto["cantidad"] = cantidad
      producto["precio"] = precio
      print("Nuestro producto se ha Actualizado exitosamente.")
      return
  # Si no se encuentra el producto, mostrar un mensaje
  print("El producto no se encuentra en el inventario.")

# crearemos una función para mostrar el inventario actual

def mostrar_inventario():

  # Verificaremos si el inventario está vacío

  if len(inventario) == 0:
    print("El inventario está vacío.")

  # Si el inventario tiene elementos, arrojaremos los resultados

  else:
    print("Nuestro inventario actual es:")
    for producto in inventario:
      print(producto)

# vamos a crear una función para mostrar el menú de opciones
def mostrar_menu():
  print("Bienvenido al sistema de administración de inventario para la ferretería de Karibay.")
  print("Seleccione una opción:")
  print("1. Agregar producto")
  print("2. Eliminar producto")
  print("3. Buscar producto")
  print("4. Actualizar producto")
  print("5. Mostrar inventario")
  print("6. Salir")

# Definiremos una variable para controlar el ciclo principal
continuar = True

# Iniciamos el ciclo principal
while continuar:
  # Mostraremos el menú de opciones
  mostrar_menu()
  # Solicitamos al usuario que ingrese una opción
  opcion = input("Ingrese una opción: ")
  # Verificamos la opción ingresada
  if opcion == "1":
    # Solicitaremos los datos del producto que deseamos agregar
    nombre = input("Ingrese el nombre del producto: ")
    categoria = input("Ingrese la categoría del producto: ")
    # Corregiremos el error de tipo de dato al convertir la entrada a entero
    cantidad = int(input("Ingrese la cantidad en stock del producto: "))
    # Corregiremos el error de tipo de dato al convertir la entrada a flotante
    precio = float(input("Ingrese el precio del producto: "))
    # hacemos un llamado a la función para agregar el producto
    agregar_producto(nombre, categoria, cantidad, precio)
  elif opcion == "2":
    # Solicitaremos el nombre del producto a eliminar
    nombre = input("Ingrese el nombre del producto: ")
    # Llamaremos a la función para eliminar el producto
    eliminar_producto(nombre)
  elif opcion == "3":
    # Solicitaremos el criterio de búsqueda
    criterio = input("Ingrese el nombre o la categoría del producto: ")
    # hacemos un llamado a la función para buscar el producto
    buscar_producto(criterio)
  elif opcion == "4":
    # Solicitar el nombre del producto a actualizar
    nombre = input("Ingrese el nombre del producto: ")
    # Solicitar la nueva cantidad y el nuevo precio
    cantidad = int(input("Ingrese la nueva cantidad en stock del producto: "))
    precio = float(input("Ingrese el nuevo precio del producto: "))
    # hacemos un llamado a la función para actualizar el producto
    actualizar_producto(nombre, cantidad, precio)
  elif opcion == "5":
    # hacemos un llamado a la función para mostrar el inventario
    mostrar_inventario()
  elif opcion == "6":
    # finalizamos el ciclo principal
    continuar = False
    print("Gracias por usar el sistema de Karibay.")
  else:
    # Mostramos un mensaje de error si la opción no es válida
    print("Opción inválida. Intente de nuevo.")