from funcionesBD import *
from usuario import Usuario
from cajero import Cajero
from administrador import Administrador
from almacen import Almacen
from producto import Producto
from datetime import datetime
from factura import Factura
conexion = conectar()

def menuAdministrador(administrador):
    print("---- MENU ADMINISTRADOR----")
    print("1 ---- Ver lista de productos")
    print("2 ---- Ver facturas por fecha")
    print("3 ---- Ver facturas por día")
    print("4 ---- Salir")
    opc = int(input(""))
    while opc != 4:
        if opc == 1:
            res = Producto.listarProductos()
            for i in range(len(res)):
                print(res[i])
        elif opc == 2:
            print("Ingrese el mes del cual quiere ver las facturas, en formato MM . Por ejemplo, para enero ingrese 01")
            mes = input("")
            lr = Factura.listarPor(mes,0)
            for i in range(len(lr)):
                print(lr[i])
            
        elif opc == 3:
            print("Ingrese el dia del cual quiere ver las facturas, en formato MM . Por ejemplo, para pimer dia ingrese 01")
            dia = input("")
            lr = Factura.listarPor(dia,1)
            for i in range(len(lr)):
                print(lr[i])
        print("---- MENU ADMINISTRADOR ----")
        print("1 ---- Ver lista de productos")
        print("2 ---- Ver facturas por fecha")
        print("3 ---- Ver facturas por día")
        print("4 ---- Salir")
        opc = int(input(""))

def menuAlmacen(almacen):
    print("---- MENU ALMACEN ----")
    print("1 ---- Cargar nuevo producto")
    print("2 ---- Modificar producto existente")
    print("3 ---- Eliminar producto")
    print("4 ---- Salir")
    opc = int(input(""))
    while opc != 4:
        if opc == 1:
            
            nombre = input("Ingrese nombre del producto a crear o 0 para salir...")
            while nombre!="0":
                
                precio = int(input("Ingrese precio del producto a crear..."))
                stock = int(input("Ingrese stock del producto a crear..."))
                almacen.cargarProducto(nombre, precio, stock)
                nombre = input("Ingrese nombre del producto a crear o 0 para salir...")
            print("Carga hecha con éxito")
        elif opc ==2:
            print(Producto.listarProductos())
            print("Elija el código del producto que desea modificar:")
            cod = int(input(""))
            almacen.modificarProducto(cod)
            print("Modificado con éxito")
        elif opc == 3:
            print(Producto.listarProductos())
            print("Elija el código del producto a borrar:")
            cod = int(input(""))
            almacen.borrarProducto(cod)
            print("Borrado con éxito")
        print("---- MENU ALMACEN ----")
        print("1 ---- Cargar nuevo producto")
        print("2 ---- Modificar producto existente")
        print("3 ---- Eliminar producto")
        print("4 ---- Salir")

def menuCajero(cajero):
    print("---- MENU CAJERO----")
    print("1 ---- Cargar nueva factura")
    print("4 ---- Salir")
    opc = int(input(""))
    while opc!=4:
        if opc == 1:
            print("Se cargará con la fecha:")
            now = datetime.now()
            fec = now.strftime("%m/%d/%Y")
            print(fec)
            cajero.agregarFactura(fec)
        print("---- MENU CAJERO----")
        print("1 ---- Cargar nueva factura")
        print("4 ---- Salir")
        opc = int(input(""))    
print("------ MENU SISTEMA:-------\n-------Ingrese sus datos para conectarse ----------")
print("NOTA: el sistema detecta solo si se ha conectado un Administrador, un Cajero o un Almacén.")
print("Para entrar como administrador usar: Nombre de usuario: administrador; Contraseña: pass")
print("Para entrar como cajero usar: Nombre de usuario: cajero; Contraseña: pass")
print("Para entrar como almacen usar: Nombre de usuario: almacen; Contraseña: pass")
nom = input("Ingrese nombre de usuario:")
cont = input("Ingrese contraseña:")
validar = Usuario.validar(nom, cont)

while(nom == "" or cont == "" or validar == 0):
    validar = Usuario.validar(nom, cont)
    print("Datos inválidos")
    nom = input("Ingrese nombre de usuario:")
    cont = input("Ingrese contraseña:")    
res = Usuario.clasificar(validar)
if res ==3:
    print("Bienvenido, nivel administrador")
    admin = Administrador(nom, cont)
    menuAdministrador(admin)
elif res == 2:
    print("Bienvenido, nivel cajero")
    cajero = Cajero(nom, cont)
    menuCajero(cajero)
else:
    print("Bienvenido, nivel almacen")
    almacen = Almacen(nom, cont)
    menuAlmacen(almacen)
cerrar(conexion)