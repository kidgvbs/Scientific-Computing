import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **balls): # **balls -> significa che la funzione accetta un numero arbitrario di argomenti chiave-valore passati come un dizionario 
        self.contents = list()
        # inserisce il colore della pallina nella lista tante volte quante è il suo valore
        for color,count in balls.items():
                for i in range(count):
                    self.contents.append(color)
        
    def draw(self, n_balls):
        if n_balls > len(self.contents):
            return self.contents
        
        balls_drawn = []
        for i in range(n_balls):
            ball_index = random.randint(0, len(self.contents)-1)
            balls_drawn.append(self.contents.pop(ball_index))
        return balls_drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
# hat: Un oggetto cappello contenente palline che dovrebbero essere copiate all'interno della funzione.
# expected_balls: indica il gruppo esatto di palline che tentiamo di attingere dal cappello per l'esperimento. Ad esempio, per determinare la probabilità di pescare 2 palline blu e 1 pallina rossa dal cappello, imposta expected_balls a {"blue":2, "red":1}.
# num_balls_drawn: Il numero di palline da pescare dal cappello in ogni esperimento
# num_experiments: Il numero di esperimenti da eseguire. (Più esperimenti eseguiti, più precisa sarà la probabilità approssimativa.)
    successful_experiments = 0

    expected_balls_list = []
    for ball, count in expected_balls.items():
        expected_balls_list += [ball] * count # trasforma il dizionario in una lista

    for i in range(num_experiments):
        hat_copy = []
        hat_copy = copy.deepcopy(hat) # deepcopy -> crea una nuova instanza dell'oggetto originale
        drawn_balls = hat_copy.draw(num_balls_drawn) # lista delle palline pescate dal cappello
        success = True
        for ball in expected_balls_list:
            if ball not in drawn_balls:
                success = False
                break
            drawn_balls.remove(ball)
        # Il ciclo for itera su expected_balls_list e verifica se ogni elemento di expected_balls_list è presente in drawn_balls tramite un'istruzione condizionale if. Se un elemento non è presente in drawn_balls, significa che l'esperimento non è riuscito e la variabile successful_experiment viene impostata su False e il ciclo viene interrotto con l'istruzione break.
        # In ogni caso, alla fine di ogni iterazione del ciclo viene rimosso l'elemento corrente di expected_balls_list dalla lista drawn_balls, in modo che se un colore è stato pescato più di una volta in questo esperimento, venga considerato solo una volta.
        if success:
            successful_experiments += 1
    return successful_experiments / num_experiments

# TEST
hat1 = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat1, expected_balls={"red":2, "green":1}, num_balls_drawn=5, num_experiments=2000)
print(probability)