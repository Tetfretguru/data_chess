#from bokeh.plotting import show, output_file, figure
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
        """ El rey se mueve en todas (8) direcciones de a un paso """
        pass

    def comer(self):
        """ Come en todas las direcciones """
        pass
<<<<<<< HEAD

class Reina(Pieza):
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
    
    reyes = []
    reinas = []
 

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
    while q <= len(reinas):
        nombre = 'Queen'
        equipo = 'W'
        pieza = Reina(nombre, equipo)
        reinas.append(pieza)
        q += 1
        if q == 1:
            nombre = 'Queen'
            equipo = 'B'
            pieza = Reina(nombre, equipo)
            reinas.append(pieza)
            break
    
    for reina in reinas:
        print(f'Pieza: {reina}')
    


    
   
   
  

    
=======
    
    def graficar(self, x_vals, y_vals):
        output_file('Movimientos de pieza.html')
        fig = figure()
        fig.circle(x_vals, y_vals)
        
        show(fig)


>>>>>>> grafico

    





    
