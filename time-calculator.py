""" Time Calculator """
# pyright: reportUnboundVariable=false

def add_time(start, duration, week_day=""):

    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    due_punti = start.find(":")
    due_punti_d = duration.find(":")
    spazio = start.find(" ", due_punti)
    minuto_d = int(duration[due_punti_d+1:])
    minuto = int(start[due_punti+1: spazio])
    ora_d = int(duration[:due_punti_d])
    ora = int(start[:due_punti])
    ampm = start[spazio+1:]
    count_d = 0

    if(int(minuto) >= 60):
        return "Error: Minutes are until 59"

    somma_ora = ora + ora_d
    somma_minuti = minuto + minuto_d
    # aumenta l'ora di 1 se i minuti sono più di 60
    if(somma_minuti >= 60):
        somma_ora += 1
        somma_minuti -= 60    

    # per ogni 24 ore count_d aumenterà il suo valore di 1
    if(ora_d == 24):
        count_d += 1 # giorni passati
        somma_ora -= 24
    elif(ora_d > 24):
        count_d += ora_d/24 # giorni passati
        punto = str(count_d).find(".")
        ore_in_piu = str(count_d)[punto+1] # estraggo la prima cifra dopo la virgola che indica altre ore in più
        somma_ora += int(ore_in_piu) * 24 # moltiplico il valore delle ore in più ottenute in base 24 (tempo di una giornata) e sommarle a somma_ora
        # molitplico 12 (che sono il tempo di durata massima di mattina e pomeriggio) per il numero di giorni che sono passati 
        # poi sottraggo il totale delle ore passate alla somma delle ore ottenute per avere un risultato in formato 12 e non 24
        somma_ora = int((somma_ora - (12 * int(count_d))) / 24)
        somma_ora += int(ore_in_piu)

    # passa da AM a PM a seconda dell'orario
    if(somma_ora >= 12 and somma_ora < 24):
        if(ampm == "AM"):
            ampm = "PM"
        else:
            ampm = "AM"
            count_d += 1 # aumenta di 1 giorno se passa da sera (PM) a mattina (AM)
    
    if(somma_ora > 12):
        somma_ora -= 12
   
    if(count_d == 1):
        giorni = ""
        giorni = " (next day)"
    elif(count_d > 1):
        giorni = ""
        giorni = f" ({int(count_d)} days later)"
    
    if(week_day == ""):
        new_time = f"{somma_ora}:{str(somma_minuti).zfill(2)} {ampm}{giorni}" # zfill riempi con uno 0 i numeri che hanno meno di 2 cifre
        return new_time
    else:
        if(count_d < 7):
            i = 0
            for day in week:
                # per tot giorni contati ripeti il ciclo dei giorni della settimana le tot volte
                if(day.lower() == week_day.lower()): 
                    x = (i - 7) + count_d # sottrae quanti giorni ha fatto scorrere nell'if, li sottrae a 7 (tutta la settimana) e poi gli somma i giorni passati
                    res_day = week[int(x)]
                i += 1
        else:
            y = 0
            # per tot giorni contati ripeti il ciclo dei giorni della settimana le tot volte
            while y <= count_d:
                i = 0
                for day in week:
                    if(day.lower() == week_day.lower()): 
                        x = (count_d % 7) + (i - 7) # trovo il resto dei giorni rimasti che sono minori di 1 settimana e lo sommo al risultato tra: i giorni trascorsi nell'ultimo giro fatto dal for per matchare il giorno di partenza, sottratto a un'intera settimana (che dà un risultato negativo) 
                        res_day = week[int(x)]
                    i += 1
                y += 1

        new_time = f"{int(somma_ora)}:{str(somma_minuti).zfill(2)} {ampm}, {res_day}{giorni}" # zfill riempi con uno 0 i numeri che hanno meno di 2 cifre
        return new_time


print(add_time("8:16 PM", "466:02", "tuesday"))