from bokeh.plotting import show, output_file, figure
import random

class Pieza:
    def __init__(self, nombre, equipo):
        """ Constructor de piezas. Superclase """
        self.nombre = nombre 
        self.equipo = equipo
    
    def graficar(self, dots):
        output_file('Movimientos de pieza.html')
        fig = figure()
        fig.circle(dots)
        
        show(fig)    
    
    

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
    
    

class Alfil(Pieza):
    def __init__(self, nombre, equipo):
        super().__init__(nombre, equipo)
    
    def __repr__(self):
        return self.nombre + ' ' + self.equipo
    
    def mover():
        # Se mueve en diagonal
        y = list(range(1, 9))
        x = list(range(1, 9))
        
        return  (len(y)**2 + len(x)**2)**0.5

    def comer(self):
        """ Come en todas las direcciones """
        pass


class Caballo(Pieza):
    def __init__(self, nombre, equipo):
        super().__init__(nombre, equipo)
    
    def __repr__(self):
        return self.nombre + ' ' + self.equipo
    
    def mover(self):
        
        pass

    def comer(self):
        """ Come en todas las direcciones """
        pass



if __name__ == '__main__':
    
    reyes = []
    alfiles = []
 

    #Cantidad de reyes posibles 
    r = 0
    while r <= len(reyes):
        nombre = 'King'
        equipo = 'W'
        pieza = Rey(nombre, equipo)
        reyes.append(pieza)
        r += 1
        if r == 1:
            nombre = 'King'
            equipo = 'B'
            pieza = Rey(nombre, equipo)
            reyes.append(pieza)
            break
    
    for rey in reyes:
        print(f'Pieza: {rey}')
    print('---' * 6)

    q = 0
    while q <= len(alfiles):
        nombre = 'Alfie'
        equipo = 'W'
        pieza = Alfil(nombre, equipo)
        alfiles.append(pieza)
        q += 1
        if q == 1:
            nombre = 'Alfie'
            equipo = 'B'
            pieza = Alfil(nombre, equipo)
            alfiles.append(pieza)
            break
    
    for alfil in alfiles:
        print(f'Pieza: {alfil}')
    
    mueve = Alfil.mover()
    print(f'El coeficiente de movimiento maximo de un alfil es {round(mueve, 2)}')
