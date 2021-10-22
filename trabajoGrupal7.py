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
numero_contacto = int(input("cuantos contacto de trabajadores desea ingresar : "))


contactosTrabajadores = {}

for ingreso in range(0, numero_contacto):
    rut= int(input("ingrese rut del contacto trabajador: "))
    nombre= input("ingrese nombre del contacto trabajador: ")
    apellido= input("ingrese apellido del contacto trabajador: ")
    empresa= input("ingrese empresa que pertenece contacto trabajador: ")
    cargo= input("ingrese cargo del contacto trabajador: ")
    telefono= int(input("ingrese telefono del contacto trabajador: "))
    email= input("ingrese email del contacto trabajador: ")
    direccion= input("ingrese direccion del contacto trabajador: ")
    contactosTrabajadores[rut]= [nombre,apellido,empresa,cargo,telefono,email,direccion]
print(contactosTrabajadores)


# proveedores: rut: nombre, telefono, email, dirección
# contactosTrabajadores: rut: nombre, apellido, empresa proveedora, cargo, telefono, email, dirección
# transacciones: idTransacción: fecha, productos, costo total.
# producto: sku: nombre, costo unitario.





