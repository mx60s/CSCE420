# Maggie von Ebers
# 525001114
# CSCE 420
# Due: February 28, 2019
# hw3pr1.py

from collections import namedtuple
import itertools as it


Var = namedtuple('var', 'letter, assignment, domain, relations')


def parse_results(first, second, result):
    letters = set(first + second + result)
    variables = {}
    for l in letters:
        variables[l] = Var(l, 0, list(range(10)), [])

    aux = [0] * len(first)

    if len(result) > len(first):
        variables[result[0]].relations.append((aux[len(aux) - 1], result[0]))
        j = 1
    else:
        j = 0
    print(aux[len(aux) - 1], '=', result[0])

    for i in range(len(first)):
        side1 = str(aux[i]) + '+' + str(first[i]) + '+' + str(second[i])
        side2 = str(result[j]) + '+' + str(aux[i] + 1) + '*10'
        print(side1, '=', side2)
        variables[first[i]].relations.append((side1, side2))
        if first[i] != second[i]:
            variables[second[i]].relations.append((side1, side2))
        if first[i] != result[i]:
            variables[result[j]].relations.append((side1, side2))
        j += 1

    return variables, aux


def solve_crypta(variables, auxillary):
    domains = []
    for k, v in variables.items():
        domains.append(v.domain)

    for combo in it.product(*domains):
        print(combo)


print("Please input your cryptarithmic problem, one line per word:")
first = input().lower()
second = input().lower()
result = input().lower()
variables, aux = parse_results(first, second, result)
solve_crypta(variables, aux)
