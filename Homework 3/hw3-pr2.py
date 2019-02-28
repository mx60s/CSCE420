# Maggie von Ebers
# 525001114
# CSCE 420
# Due: February 28, 2019
# hw3pr2.py

# Horn clause is a clause where no more than one proposition is true
# Prolog notation in section 9.4.2
# Function in section 7.17, page 261


print("Please input a filename (including extension) from which commands should be read.")
#filename = input(">")

#file = open(filename, "r")
file = ["B:-A.", "D:-B,C.", "A.", "C.", "?D."]

total_symbols = []


def find_pure_symbol(clauses):
    for s in total_symbols:
        i = 0
        first = False
        for key, value in clauses.items():
            if s not in value:
                continue
            else:
                #ispos = key.find("not") > -1 and 
                pass

    # for each symbol, for each clause, if the symbol appears in the clause, first = if ! comes before the symbol or not

    return 0, 1

def find_unit_cause(clauses, model):
    return 0, 0

# Model is a list of tuples containing a variable and its value
def dpll(clauses: [], symbols: set, model: []) -> bool:
    count = 0
    for key, value in clauses.items():
        for x in value:
            if x not in model:
                continue    # Just ignore a clause if its variables have not all been defined
        if eval(key):
            count += 1
        else:
            return False    # if some clause is false, return false
    if count == len(clauses, symbols, model):
        return True
    
    symbol, value = find_pure_symbol(clauses)
    if symbol != "_":
        return dpll(clauses, symbols.remove(symbol), model.append((symbol, value)))

    symbol, value = find_unit_cause(clauses, model)
    if symbol != "_":
        return dpll(clauses, symbols.remove(symbol), model.append(symbol, value))

    symbol = symbols[0]
    rest = symbols[1:]
    
    final = dpll(clauses, rest, model.append((symbol, True))) or dpll(clauses, rest, model.append((symbol, False)))
    return final


def dpll_sat(filename):
    file = ["B:-A.", "D:-B,C.", "A.", "C.", "?D."]
    commands = []
    for line in file:
        line = line.replace(",", " and ")
        line = line[:2].replace(":-", "not ") + line[2:]   # If this symbol comes first, it's negation.
        line = line.replace(":-", " or not ") # Otherwise, use this equivalence
        line = line.replace("?", "")
        line = line.replace(".", "")    # Assuming that every clause is on its own line
        commands.append(line)
        print(line)

    clauses = dict.fromkeys(commands, [])   # Need a better, more general solution
    symbols = set()
    for c in clauses:
        if c.key.find("A") > -1:
            c.append("A")
            symbols.add("A")
        if c.key.find("B") > -1:
            c.append("B")
            symbols.add("B")
        if c.key.find("C") > -1:
            c.append("C")
            symbols.add("C")
        if c.key.find("D") > -1:
            c.append("D")
            symbols.add("D")
    
    return dpll(clauses, symbols, [])

    