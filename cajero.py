from funcionesBD import *
from usuario import Usuario
from factura import Factura
from producto import Producto
class Cajero(Usuario):
    def __init__(self, nom, password):
        super().__init__(nom, password)
    
    def agregarFactura(self, fec):
        miFac = Factura(fec)
        print(Producto.listarProductos())
        print("Ingrese código del producto que desea agregar o -1 para salir...")
        miCod = int(input(""))
        while miCod != -1:
            miFac.agregarProd(miCod, 1)
            print("Ingrese código del producto que desea agregar o -1 para salir...")
            miCod = int(input(""))
        miFac.grabar()
        print("Factura cerrada con éxito")
        
        