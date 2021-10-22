# DESARROLLO
# En equipo construyamos una nueva base de datos. En ella debemos incluir información de diversos
# proveedores de nuestra tienda virtual.
# Cada base de datos, debe tener la información necesaria para crear tres tablas diferentes. La primera
# hace referencia a información de los proveedores como personas jurídicas. La segunda hace referencia
# a los contactos con trabajadores de las empresas proveedoras. Por último, la tercera tabla debe tener
# información relativa a las transacciones que realizamos con cada empresa proveedora (productos
# recibidos y costos asociados).
# Cada integrante debe crear una de las tablas. Si hay más usuarios que tablas, entonces diseñen una
# nueva tabla pertinente.
# Ingresar cada dato por la terminal. Para esto apoyense de la función input.
# Utilizando Git-Hub, indague una forma de guardar toda la información en una sola variable. ¿Cuál
# consideran que es la más eficiente para hacer esto?

proveedores = {}

contactosTrabajadores = {}

transacciones = {}

productos = {}

# proveedores: rut: nombre, telefono, email, dirección
# contactosTrabajadores: rut: nombre, apellido, empresa proveedora, cargo, telefono, email, dirección
# transacciones: idTransacción: fecha, productos, costo total. 
# producto: sku: nombre, costo unitario.

for i in range(5):
    sku = input("Ingrese el SKU del producto: ")
    print("----------------------------")
    nombre = input("Ingrese el nombre del producto: ")
    print("----------------------------")
    costo = int(input("Ingrese el valor del producto: "))
    print("----------------------------")
    productos[sku] = [nombre, costo]

print(productos)

producto = {'0001': ['Naranja', 500], '0002': ['Manzana', 300], '0003': ['Kiwi', 1000], '0004': ['Platano', 250], '0005': ['Sandia', 3000]}




