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

#Creamos 4 diccionarios con los siguientes datos: 

# proveedores: rut: nombre, telefono, email, dirección
# contactosTrabajadores: rut: nombre, apellido, empresa proveedora, cargo, telefono, email, dirección
# transacciones: idTransacción: fecha, productos, costo total. 
# producto: sku: nombre, costo unitario.
from datetime import datetime

proveedores = {}
productos = {}
contactosTrabajadores = {}
transacciones = {}
#input de Proveedores (Constanza Hurtado): 
#Aca edita Emanuel

idTransacción = input('Ingrece el id de transaccion: ')
fecha =  datetime.now()
productos = input('Ingrece producto: ')
costo_total = int(input('Ingre el valor del producto: '))

transacciones[idTransacción] = [fecha, productos, costo_total]

for clave, valor in transacciones.items():
    print(clave, ':',valor)

#Se definen las variables a ingresar en el diccionario Proveedores: 

rutProveedor = input("Ingrese rut proveedor: ")
nombreProveedores = input("Nombre del proveedor: ")
telefonoProveedores = input("Contacto proveedor: ")
emailProveedores = input("Correo proveedor: ")
direccionProveedores = input("Direccion proveedor: ")

#Se genera un diccionario con las variables declaradas anteriormente
proveedores[rutProveedor] = [nombreProveedores, telefonoProveedores, emailProveedores, direccionProveedores]

#Con un ciclo for se imprime los valores ingresados
for clave, valor in proveedores:
    print(clave, ':',valor)


#input de productos (Pablo Morales):

#Se cera un cilo for que permite el ingreso de 5 productos. 

for i in range(5):
    sku = input("Ingrese el SKU del producto: ")
    print("----------------------------")
    nombre = input("Ingrese el nombre del producto: ")
    print("----------------------------")
    costo = int(input("Ingrese el valor del producto: "))
    print("----------------------------")
    productos[sku] = [nombre, costo]

print(productos)

#input de contactosTrabajadores (Alejandro Venegas):

# Se define una variable que indica el número de contactos a ingresar. 

numero_contacto = int(input("cuantos contacto de trabajadores desea ingresar : "))

#Luego, en base al número de contactos, se genera un ciclo for con las variables input y un output con estos datos. 

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









