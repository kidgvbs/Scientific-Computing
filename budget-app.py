class Category:

    def __init__(self, name_category):
        self.name_category = name_category
        self.ledger = []

    def __repr__(self): # quando vuoi printare un oggetto entra in gioco la funziona __repr__
        title = self.name_category.center(30, "*") + "\n" # centra il nome tra gli asterischi
        elements = ""
        amount = ""
        for i in self.ledger:
            desc = "{:<23}".format(i["description"]) # la stringa verrà allineata a sinistra e avrà una lunghezza massima di 23 caratteri
            amount = "{:>7.2f}".format(i["amount"]) # ">" indica che il numero verrà allineato a destra, "7.2f" indica che il numero verrà arrotondato a due cifre decimali e inserito in una stringa con una lunghezza di sette caratteri
            elements += desc[:23] + amount[:7] + "\n" # contiene i primi 23 caratteri di "desc" e i primi 7 caratteri di "amount"

        balance = "Total: {:.2f}".format(self.get_balance()) # mostra il totale del bilancio, .2f indica che il numero deve essere arrotondato a due cifre decimali
        return title + elements + balance
        
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if(self.check_funds(amount)):
            self.ledger.append({"amount": -1 * amount, "description": description})
            return True
        else:
            return False    

    def get_balance(self):
        balance = 0
        value = 0
        for i in self.ledger:
            value = i["amount"]
            balance += value # sommando un numero pos a uno neg, il ris sarà neg (10 + -15 = -5)
        return balance # arrotonda fino a 2 cifre decimali

    def transfer(self, amount, another_category):
        if(self.check_funds(amount)):
            self.withdraw(amount, "Transfer to " + another_category.name_category)
            another_category.deposit(amount, "Transfer from " + self.name_category)
            return True
        else:
            return False

    def check_funds(self, amount):
        balance = self.get_balance()
        if(balance >= amount):
            return True
        else:
            return False

def create_spend_chart(categories):
    spent_amounts = []
    # Get total spent in each category
    for category in categories:
        spent = 0
        for i in category.ledger:
            if i["amount"] < 0:
                spent += abs(i["amount"]) # totale speso, abs() rimuove il negativo
        spent_amounts.append(round(spent, 2)) # lista dei totali spesi per tutte le categorie

    # Calcola il totale speso sommando tutti gli "ammontare" nella lista e li arrotonda a due cifre decimali
    total = round(sum(spent_amounts), 2)
    # Si divide l'importo per il totale, si moltiplica per 10 e si arrotonda al numero intero più vicino. Il risultato viene quindi moltiplicato per 10 e aggiunto alla lista spent_percentage.
    spent_percentage = []
    for amount in spent_amounts:
        spent_percentage.append(int((((amount / total) * 10) // 1) * 10))

    title = "Percentage spent by category\n"
    grafico = ""
    for i in reversed(range(0, 101, 10)):
        grafico += str(i).rjust(3) + "|"
        for percent in spent_percentage:
            if percent >= i:
                grafico += " o "
            else:
                grafico += "   "
        grafico += " \n"
    
    end = "    " + "-" * ((3 * len(categories)) + 1) + "\n" # len(categories) sono il numero di categorie passate
    # così facendo ci saranno 3 linee per categoria e la categoria sarà sul secondo di 3 linee, +1 alla fine
    
    names = list()
    for category in categories:
        names.append(category.name_category)
    max_len = 0
    for i in names:
        if(len(i) > max_len):
            max_len = len(i)
    
    new_descriptions = list()
    for name in names:
       new_descriptions.append(name.ljust(max_len)) # giustifica il nome a sinistra rispetto alla lunghezza massima di uno dei nomi

    for i in zip(*new_descriptions): # La funzione zip() consente di "zipare" insieme più liste, in modo che ogni elemento della lista risultante sia un tuple contenente un elemento da ogni lista originale
    # es: ["Food  ", "Cinema"] -> [("F", "C"), ("o", "i",) ("o", "n"), ("d", "e"), (" ", "m"), (" ", "a")]
    # Food avrà 2 spazi dopo di sè per l'ljust() utilizzato nel for di prima
        end += "    "
        for s in i:
            end += s.center(3)
        end += " \n"
    # le righe da 102 a 105 permettono la formattazione in colonna di ogni Tuple ottenuto dal for i in zip(*new_descriptions) 
    
    return (title + grafico + end).rstrip("\n")

## TEST ##
budget = Category("Food")
category2 = Category("Entertainment")
category3 = Category("Business")
budget.deposit(1500, "Deposito n.1")
budget.deposit(20.50, "Deposito n.2")
budget.transfer(500, category2)
budget.withdraw(50, "Ziguli")
budget.withdraw(100, "Bose")
category2.withdraw(230, "Zuguluni")
category3.deposit(1500, "Deposito n.1")
category3.transfer(500, budget)
print(create_spend_chart([budget, category2, category3]))

# This Function was stealed from another guy and help me to write my solution without using map() and lambda 
    # spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))
# Explanation of function (in Italy)
    # list() inserisce tutti i risultati in una lista
    # map() consente di applicare una funzione a tutti gli elementi di un iterabile
    # lambda crea funzioni di una sola riga che possono essere passate come argomenti a altre funzioni
    # La sintassi di una funzione lambda è: lambda argomento1, argomento2 : espressione
    # con map -> map(lambda argomento1, argomento2 : espressione, argomento1, argomento2)