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

rutProveedor = input("Ingrese rut proveedor: ")
nombreProveedores = input("Nombre del proveedor: ")
telefonoProveedores = input("Contacto proveedor: ")
emailProveedores = input("Correo proveedor: ")
direccionProveedores = input("Direccion proveedor: ")

proveedores[rutProveedor] = [nombreProveedores, telefonoProveedores, emailProveedores, direccionProveedores]

for clave, valor in proveedores:
    print(clave, ':',valor)

#Aca edita Emanuel
from datetime import datetime

transacciones = {}

idTransacción = input('Ingrece el id de transaccion')
fecha =  datetime.now()
productos = input('Ingrece producto')
costo_total = int(input('Ingre el valor del producto'))

transacciones[idTransacción] = [fecha, productos, costo_total]

for clave, valor in transacciones:
    print(clave, ':',valor)


# proveedores: rut: nombre, telefono, email, dirección
# contactosTrabajadores: rut: nombre, apellido, empresa proveedora, cargo, telefono, email, dirección
# transacciones: idTransacción: fecha, productos, costo total. 
# producto: sku: nombre, costo unitario.





