from bokeh.plotting import show, output_file, figure
import random

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
        return   random.choice([(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)])
       

    def comer(self):
        """ Come en todas las direcciones """
        pass
    
    def graficar(self, x_vals, y_vals):
        output_file('Movimientos de pieza.html')
        fig = figure()




        fig.circle(x_vals, y_vals)
        show(fig)

if __name__ == '__main__':
    nombre = 'King'
    equipo = 'N'
    pieza = Rey(nombre, equipo)

    print(pieza)

    





    
