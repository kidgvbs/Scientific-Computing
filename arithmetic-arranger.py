# pyright: reportUnboundVariable=false
# pyright: reportGeneralTypeIssues=false

def arithmetic_arranger(problems, visual_results = False):

    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ''
    num1 = []
    num2 = []
    lines = []
    results = []

    for elements in problems:
        splitted = elements.split()
        max_len = len(max(splitted, key=len)) # ritorna la lunghezza dell'elemento più lungo
        if (len(splitted[0]) > 4 or len(splitted[2]) > 4):
            return "Error: Numbers cannot be more than four digits."
        elif (splitted[1] == '*' or splitted[1] == '/'):
            return "Error: Operator must be '+' or '-'."
        elif (splitted[0].isdecimal() == False or  splitted[2].isdecimal() == False):
            return "Error: Numbers must only contain digits."
        
        len_line = max_len + 2  # 2 è uguale all'operatore + spazio vuoto
        line = '-' * len_line
        
        firstnum = splitted[0].rjust(len_line,' ') # right justify with white space for len_line value
        secnum = splitted[1] + splitted[2].rjust(len_line - 1, ' ')

        num1.append(firstnum)
        num2.append(secnum)
        lines.append(line)
        arranged_problems = '    '.join(num1) + '\n' + '    '.join(num2) + '\n' + '    '.join(lines)

        if visual_results:
            if(splitted[1] == '+'):
                result = int(splitted[0]) + int(splitted[2])
            else:
                result = int(splitted[0]) - int(splitted[2])
            res = str(result).rjust(len_line, ' ')
            results.append(res)
            arranged_problems += '\n' + '    '.join(results) # va a capo e joina la lista dei risultati a quella di prima

    return arranged_problems

print(arithmetic_arranger(["32 - 8222", "10 + 10", "978 - 431"], True))