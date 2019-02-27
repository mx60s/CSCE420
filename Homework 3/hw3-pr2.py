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
commands = []
for line in file:
    line = line.replace(",", " and ")
    line = line[:2].replace(":-", "not ") + line[2:]   # If this symbol comes first, it's negation.
    line = line.replace(":-", " or not ") # Otherwise, use this equivalence
    line = line.replace("?", "")
    line = line.replace(".", "")    # Assuming that every clause is on its own line
    commands.append(line)
    print(line)

def dpll(clauses):
    alltrue = True
    # stuff needs to be assigned before you can eval though
    for c in clauses:
        if not eval(c):
            alltrue = False
    