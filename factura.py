from funcionesBD import *
from producto import Producto
from datetime import datetime
class Factura:
    def __init__(self, fecha, codigo=0, listaP=[], listaC=[], total=0, subtotal=0, ivg=0):
        conexion = conectar()
        self.codigo = 0
        self.fecha = fecha
        self.listaProd = listaP
        self.listaCant = listaC
        self.total = total
        self.ivg = ivg
        self.subtotal = subtotal
        c = ejecutar("select facturaid from facturs order by facturaid desc limit 1", 0, conexion)
        for elem in c:
            self.codigo = elem[0]+1
        if self.codigo == 0:
            self.codigo = 1
        insertFact = "insert into facturs (fecha, total, ivg, subtotal) values (%s, %s,%s,%s);"
        
        datos = (self.fecha, str(self.total), str(self.ivg), str(self.subtotal))
        c = ejecutar(insertFact, datos, conexion)
        cerrar(conexion)
    def agregarProd(self, prod, cant):
        conexion = conectar()
        
        c = ejecutar("select * from products where productoid ='" +str(prod)+"'", 0, conexion)
        prec = 0
        for elem in c:
            #def __init__(self, n, prec, stock=0, codigo=0):
            nuevoProd = Producto(elem[1], elem[2], 0, elem[0])
        hallado = False
        for i in range(len(self.listaProd)):
            if self.listaProd[i].n == nuevoProd.n:
                self.listaCant[i] = self.listaCant[i]+1
                i = len(self.listaProd)
                hallado = True
        if hallado == False:    
            self.listaProd.append(nuevoProd)    
            self.listaCant.append(cant)
        
        self.subtotal = self.subtotal+(nuevoProd.prec*cant)
        self.ivg = self.subtotal*0.18
        self.total = self.subtotal*(1.18)
        print(self.subtotal)
        print(self.ivg)
        print(self.total)
    def grabar(self):
        
        conexion = conectar()
        grabaFact = "update facturs set total = %s, subtotal = %s, ivg = %s where facturaid = %s;"
        datos = (str(self.total), str(self.subtotal), str(self.ivg), str(self.codigo))
        c = ejecutar(grabaFact, datos, conexion)
        for i in range(len(self.listaProd)):
            ingresaRel = "insert into factursproducts (facturaid, productoid, cantidad) values (%s,%s,%s);"
            datos = (str(self.codigo), str(self.listaProd[i].codigo), str(self.listaCant[i]))
            c = ejecutar(ingresaRel, datos, conexion)
            
        cerrar(conexion)
    @staticmethod
    def listarfacturs():
        conexion = conectar()
        c = ejecutar("select * from facturs", 0, conexion)
        lRes = []
        for elem in c:
            result = "Código: " + str(elem[0]) + " | Fecha: " + str(elem[1]) + " | Subtotal: " + str(elem[2]) + " | IVG: " + str(elem[3]) + " | Total: " + str(elem[4])
            lRes.append(result)
        cerrar(conexion)
        return lRes
    @staticmethod
    def listarPor(dato, modo=0):
        conexion = conectar()
        
        c = ejecutar("select * from facturs", 0, conexion)
        lRes = []
        for elem in c:
            fec = elem[1]
            fecs = fec.split('/')
            
            result = "Código: " + str(elem[0]) + " | Fecha: " + str(elem[1]) + " | Subtotal: " + str(elem[2]) + " | IVG: " + str(elem[3]) + " | Total: " + str(elem[4])
            if modo == 0 and dato == fecs[0]  :
                
                lRes.append(result)
            elif modo == 1 and dato == fecs[1]:
                lRes.append(result)

        cerrar(conexion)
        return lRes
        
  

    
        