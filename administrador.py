from funcionesBD import *
from usuario import Usuario
from producto import Producto
class Administrador(Usuario):
    def __init__(self, nom, password):
        super().__init__(nom, password)
    