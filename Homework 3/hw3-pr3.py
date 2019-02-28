# Maggie von Ebers
# 525001114
# CSCE 420
# Due: February 28, 2019
# hw3pr3.py

import re
import sys

print("Please enter the clauses in your CNF formula, one per line:")
clauses = []
variables = set()
for line in sys.stdin:
    line = line.upper()

    for letter in re.sub(r'\W+', '', line):
        variables.add(letter)

    line = line.replace("-", "not ")
    line = line.replace("+", " or ")
    line = line.replace("\n", "")
    clauses.append(line)

print()


# Set up a header in the format   A  B  C    A or B or C
header = ""
for letter in variables:
    header += letter + "  "

header += "   "

formula = ""
for i in range(len(clauses)-1):
    formula += "(" + clauses[i] + ")" + " and "
formula += "(" + clauses[len(clauses)-1] + ")"
header += formula

print(header)
print("-" * len(header))


# Define the assignments for each variable
variables = dict.fromkeys(variables, 0)

for k, v in variables.items():      # this is stupid but it's for the eval function.
    formula = re.sub(k, 'variables[\'' + k + '\']', formula)


for x in range(2**len(variables)):
    # Create a binary string based on the index for assigning values
    values = str(bin(x)[2:]).zfill(len(variables))
    line = ""
    for v in values:
        line += v + "  "

    i = 0
    for k, v in variables.items():
        variables[k] = bool(int(values[i]))
        i += 1

    line += "       " + str(eval(formula))
    print(line)
