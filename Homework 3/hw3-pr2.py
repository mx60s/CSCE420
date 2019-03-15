# Maggie von Ebers
# 525001114
# CSCE 420
# Due: February 28, 2019
# hw3pr2.py


######## Input ########
print("Please input a filename (including extension) from which commands should be read.")
filename = input("> ")

file = open(filename, "r")
given = []

for line in file:
    given.append(line[:len(line)-1])


######## Parsing ########
resolution = given[len(given)-1].replace("?", "").replace(".", "")
given = given[:len(given)-1]
clauses = set()
variables = set()

for clause in given:
    for c in clause:
        if c not in ".?,:-":
            variables.add(c)    # Collect all variables to assign truth values

    clause = clause.replace(".", "")
    if ":-" in clause:
        lhs, rhs = clause.split(":-")
        for term in rhs.split(','):
            clauses.add(f"not {lhs} or {term}")     # Apply equivalence and split terms
    else:
        clause = clause.replace(",", "and")
        clauses.add(clause)


######## Evaluation ########

# Total statement should be a tautology if correct, so set all variables to false.
values = dict.fromkeys(variables, False)

# Creating our statement to evaluate, again using logical equivalence
statement = "not("
for c in clauses:
    statement += "(" + c + ") and "

statement = statement[:len(statement)-5] + ") or " + resolution

print(statement)

print(eval(statement, values))