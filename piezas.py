class Pieza:
    def __init__(self, nombre, equipo):
        """ Constructor de piezas. Superclase """
        self.nombre = nombre 
        self.equipo = equipo
    
    

class Rey(Pieza):
    def __init__(self, nombre, equipo):
        super().__init__(nombre, equipo)
    
    def __repr__(self):
        return self.nombre + ' ' + self.equipo
    
    def mover(self):
        """ El rey se mueve en todas (8) direcciones de a un paso """
        pass

    def comer(self):
        """ Come en todas las direcciones """
        pass

if __name__ == '__main__':
    nombre = 'King'
    equipo = 'N'
    pieza = Rey(nombre, equipo)

    print(pieza)

    





    
