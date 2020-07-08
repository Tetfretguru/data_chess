class Pieza:
    def __init__(self, nombre, equipo):
        """ Constructor de piezas. Superclase """
        self.nombre
        self.equipo

class Rey(Pieza):
    def __init__(self):
        super().__init__(self, 'Rey', color)
    
    def mover(self):
        """ El rey se mueve en todas (8) direcciones de a un paso """
        pass

    def comer(self):
        """ Come en todas las direcciones """
        pass
    
class Reina(Pieza):
    def __init__(self):
        super().__init__(self, 'Reina', color)
    
    def mover(self):
        """ Se mueve en todas las direcciones y a lo largo del tablero"""
        pass
    
    def comer(self):
        """Come en toda direccion y en maximo alcance"""
        pass
    
class Caballo(Pieza):
    def __init__(self):
        super().__init__(self, 'Caballo', color)
        """ Solo 2 caballos por equipo """
    
    def mover(self):
        """ Caballo mueve:
            - 2 adelante, 1 izq
            - 2 adelante, 1 der
            - 1 adelante, 2 izq
            - 1 adelante, 2 der
            - 2 atrás, 1 der
            - 2 atras, 1 izq
            - 1 atras, 2 der
            - 1 atras, 2 izq
            - Salta por encima de aliados y rivales
        """
        pass
    
    def comer(self):
        """ Solo al caer en posicion rival """
        pass

class Alfil(Pieza):
    def __init__(self):
        super().__init__(self, 'Alfil', color)
        """ 2 por equipo"""
    def mover(self):
        """ Solo puede moverse en diagonal y en maximo alcance"""

    def comer(self):
        """ Come en diagonal """
        pass

class Torre(Pieza):
    def __init__(self):
        super().__init__(self, 'Torre', color)
        """ 2 por equipo """
    def mover(self):
        """ Se mueve en |_ o _| avanzando o retrocediendo"""
        pass

class Peon(Pieza):
    def __init__(self):
        super().__init__(self, 'Peon' , color)
        """ 8 peones por equipo """
    
    def mover(self):
        """ Se mueve de a un bloque; unicamente hacia adelante """
        pass
    
    def comer(self):
        """ Come en diagonal y de a un bloque, 2 direcciones. Siempre avanzando"""
        pass

if __name__ == '__main__':

    pieza = Torre('N')

    print(pieza)

    





    
