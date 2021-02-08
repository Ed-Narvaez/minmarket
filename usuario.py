from funcionesBD import *
#from administrador import Administrador
#from cajero import Cajero
#from almacen import Almacen
class Usuario:
    def __init__(self, nom, password):
        self.n = nom
        self.p = password
    
    @staticmethod
    def validar(nom, password):
        conexion = conectar()
        data = (nom, password)
        id = 0
        c = ejecutar("select * from usuarios where nombre='"+nom+"' and pass='"+password+"'", data, conexion)
        c=c.fetchone()
        if c == None:
            return 0
        else:
            return c[0]

        cerrar(conexion)
    @staticmethod
    def clasificar(id):
        conexion=conectar()
        
        data=(id,)
        c = ejecutar("select * from administradores where usuarioId='"+str(id)+"'", data, conexion)
        c = c.fetchone()
        if c != None:
            
            return 3
        c = ejecutar("select * from cajeros where usuarioId='"+str(id)+"'", data, conexion)
        c = c.fetchone()
        if c!= None:
            
            return 2
        c = ejecutar("select * from almacenes where usuarioId='"+str(id)+"'", data, conexion)
        c = c.fetchone()
        if c!= None:
            
            return 1
        
        