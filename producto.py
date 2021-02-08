from funcionesBD import *
class Producto:
    def __init__(self, n, prec, stock=0, codigo=0):
        self.codigo = codigo
        self.n = n
        self.prec = prec
        self.stock = stock
    def crearProd(self):
        conexion = conectar()
        insProd = "insert into products (nombre, precio, stock) values (%s,%s,%s);"
        data = (self.n, self.prec, self.stock)
        c = ejecutar(insProd, data, conexion)
        cerrar(conexion)
    @staticmethod
    def listarProductos():
        conexion = conectar()
        c = ejecutar("select * from products", 0, conexion)
        lRes = []
        for elem in c:
            result = "Código: " + str(elem[0]) + " | Nombre: " + str(elem[1]) + " | Precio: " + str(elem[2])+ " | Stock: " + str(elem[3])
            lRes.append(result)
        return lRes
    