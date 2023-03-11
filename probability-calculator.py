import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls): # **balls -> significa che la funzione accetta un numero arbitrario di argomenti chiave-valore passati come un dizionario
        if len(balls) < 1:
            raise ValueError("Deve esserci minimo un argomento") 
            # raise -> solleva un'eccezione
            # ValueError -> è un tipo di eccezione che viene sollevata quando si passa un valore non valido a una funzione o metodo
        else: self.contents = balls
    

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


# TEST
hat1 = Hat()
print(hat1) # output = {'yellow': 2, 'red': 5, 'blue': 1}