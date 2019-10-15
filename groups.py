# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 13:42:43 2019

@author: aaron.drake
"""

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

selection_rules = (rule18, )

group_size_rule1 = lambda possibility: [2,2,2] == sorted([len(p) for p in possibility], reverse = True)
group_size_rule2 = lambda possibility: len(possibility) == 2

group_size_rules = (group_size_rule1, group_size_rule2)

pool = set((A, B, C, D, E, F, G, H, I))

possibilities = []

office1_possibilities = set(it.combinations(pool, 2))
office2_possibilities = None
office3_possibilities = None
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
            possibilities.append(possibility)

print(f"possibility #1: {possibilities[0]}")
solutions = Grouping.is_solution(possibilities[0], group_size_rules, selection_rules)
print(solutions)
