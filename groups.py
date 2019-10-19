# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:42:43 2019

@author: aaron.drake
"""
import random
import numpy as np
import itertools as it
from AnalyticalReasoning import Variable
from AnalyticalReasoning import Grouping
from AnalyticalReasoning import *
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
rule18 = when(A).then(-B)


rule19 = D.then(-E)
rule20 = D.then(-I)
rule21 = D.then(-C)
rule22 = D.then(-F)
rule23 = D.then(-B)
rule24 = D.then(-H)
rule25 = D.then(-G)
rule26 = D.then(-A)
rule27 = select(-A)

selection_rules = (rule26,rule25,rule24,rule23, rule20, rule21)

def group_size_rule3(possibility):
    return len(possibility) == 2

group_size_rule1 = lambda possibility: [3,3,3] == sorted([len(p) for p in possibility], reverse = True)
group_size_rule2 = lambda possibility: len(possibility) == 3

group_size_rules = (group_size_rule1, group_size_rule2, )

pool = (A, B, C, D, E, F, G, H, I)

#possibilities = []
#
#office1_possibilities = set(it.combinations(pool, 3))
#office2_possibilities = None
#office3_possibilities = None
#
#
#for office1_possibility in office1_possibilities:
#    office1 = set(office1_possibility)
#    office2_pool = pool - office1
#    office2_possibilities = set(it.combinations(office2_pool, 3))
#    for office2_possibility in office2_possibilities:
#        office2 = set(office2_possibility)
#        office3_pool = office2_pool - office2
#        office3_possibilities = set(it.combinations(office3_pool, 3))
#        for office3_possibility in office3_possibilities:
#            office3 = set(office3_possibility)
#            possibility = (office1,office2,office3) 
#            possibilities.append(possibility)


gen_poss = Grouping.generate_possibilities(pool, group_sizes=(3,3,3), num_selected=9)
possiblity1_is_solution, message = Grouping.is_solution(gen_poss[0], group_size_rules, selection_rules)
solutions = Grouping.solve(gen_poss, group_size_rules, selection_rules)
print("solutions found")
for solution in solutions:
    print(solution)

print(f"possibility #1: {gen_poss[0]}")
print(possiblity1_is_solution)
print(message)

