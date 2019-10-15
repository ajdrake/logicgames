# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:42:43 2019

@author: aaron.drake
"""

import itertools as it
from variable import Variable
from variable import *
A = Variable("A")
B = Variable("B")
C = Variable("C")
D = Variable("D")
E = Variable("E")
F = Variable("F")
G = Variable("G")
H = Variable("H")
I = Variable("I")


rule1 = A.is_sufficient(B)
rule2 = A.then(B)
rule3 = A.only(B)
rule4 = A.onlyif(B)
rule5 = A.must(B)
rule6 = A.is_required(B)
rule7 = A.is_precondition(B)
rule8 = A.unless(B)
rule9 = A.xcept(B)
rule10 = A.until(B)
rule11 = A.without(B)

rule12 = when(A).then(B)

rule13 = whenever(A).then(B)

rule14 = B.when(A)
rule15 = B.every(A)
rule16 = B.in_order_to(A)
rule17 = in_order_to(A).must(B)

rules = (rule2, )

# TODO : add to rules.py
def check(rules, possibilities):
    solutions = possibilities.copy()
    for rule in rules:
        for possibility in possibilities:
            if not rule(possibility) and possibility in solutions:
                solutions.remove(possibility)

pool = set((A, B, C, D, E, F, G, H, I))

possibilies = []

office1_possibilities = set(it.combinations(pool, 2))
office2_possibilities = set()
office3_possibilities = set()
#print(f"office #1 pool: {office1_pool}")
for office1_possibility in office1_possibilities:
    office1 = set(office1_possibility)
    office2_pool = pool - office1
    office2_possibilities = set(it.combinations(office2_pool, 2))
    for office2_possibility in office2_possibilities:
        office2 = set(office2_possibility)
        office3_pool = office2_pool - office2
        office3_possibilities = set(it.combinations(office3_pool, 2))
        for office3_possibility in office3_possibilities:
            office3 = set(office3_possibility)
            possibility = (office1,office2,office3) 
            possibilies.append(possibility)

print(f"possibilities: {possibilies}")
solutions = check(rules, possibilies)
print(solutions)


#    print(rule1(possibility))
#    print(rule2(possibility))
#    print(rule3(possibility))
#    print(rule4(possibility))
#    print(rule5(possibility))
#    print(rule6(possibility))
#    print(rule7(possibility))
#    print(rule8(possibility))
#    print(rule9(possibility))
#    print(rule10(possibility))
#    print(rule11(possibility))
#    print(rule12(possibility))
#    print(rule13(possibility))
#    print(rule14(possibility))
#    print(rule15(possibility))
#    print(rule16(possibility))
#    print(rule17(possibility))
#    