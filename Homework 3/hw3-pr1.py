# Maggie von Ebers
# 525001114
# CSCE 420
# Due: February 28, 2019
# hw3pr1.py


def revise(relation, domain, var1: str, var2: str) -> bool:
    revised = False
    for x in domain[var1]:
        found = False
        for y in domain[var2]:
            rel = str(x) + "+" + str(y)
            if eval(rel) == eval(relation[rel]):
                found = True
        if not found:
            domain[var1].remove(x)
            revised = True
    return revised

def ac_3(assignment, domain):
    pass


def solve_crypta(letters: set, firstlen: int) -> []:
    assignment = dict.fromkeys(letters, 0)
    domain = dict.fromkeys(letters, list(range(10)))

    for i in range(firstlen):
        name = 'x' + i
        assignment[name] = 0
        domain[name] = [0,1]
    
    
# relations also probably needs to be a dictionary then


# Taking input and setting up our initial problem state
letters = set()
firstlen = 0 # length of the first word
print("Please input your cryptarithmic problem, one line per word: ")

for i in range(3):
    l = input().lower()
    if i == 0:
        firstlen = len(l)
    for c in l:
        letters.add(c)

print(solve_crypta(letters, firstlen))
