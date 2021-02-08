from funcionesBD import *
from usuario import Usuario
from producto import Producto
class Almacen(Usuario):
    def __init__(self, nom, password):
        super().__init__(nom, password)
    def cargarProducto(self, nombre, precio, stock=0):
        prod = Producto(nombre, precio, stock)
        prod.crearProd()
    def modificarProducto(self, codProd):
        conexion = conectar()
        print("Nuevo nombre:")
        nom = input("")
        print("Nuevo precio:")
        prec = int(input(""))
        print("Nuevo stock:")
        stock = int(input(""))
        data = (nom, prec, stock)
        actual = "update products set nombre=%s, precio ='%s', stock='%s' where productoId = '"+str(codProd)+"'"
        c = ejecutar(actual, data, conexion)
        cerrar(conexion)
    def borrarProducto(self, codProd):
        conexion = conectar()
        data = (1,)
        actual = "delete from products where productoId = '"+str(codProd)+"'"
        
        c = ejecutar(actual, data, conexion)
        cerrar(conexion)