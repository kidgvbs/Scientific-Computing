import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls): # **balls -> significa che la funzione accetta un numero arbitrario di argomenti chiave-valore passati come un dizionario
        if len(balls) < 1:
            raise ValueError("Deve esserci minimo un argomento")
            # raise -> solleva un'eccezione
            # ValueError -> è un tipo di eccezione che viene sollevata quando si passa un valore non valido a una funzione o metodo
        else: 
            self.contents = list()
            # inserisci il colore della pallina nella lista tante volte quante è il suo valore
            for color,count in balls.items():
                for i in range(count):
                    self.contents.append(color)
        
    def __repr__(self):
        return str(self.contents)

    def draw(self, n_balls):
        if n_balls > len(self.contents):
            raise ValueError("more balls to draw than balls in the hat")
        else:
            balls_drawn = []
            for i in range(n_balls):
                ball_index = random.randint(0, len(self.contents)-1)
                balls_drawn.append(self.contents.pop(ball_index))
                
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


# TEST
hat1 = Hat()
print(hat1)