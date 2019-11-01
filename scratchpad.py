#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 21:59:12 2019

@author: Aaron
"""

import numpy
import random
import numpy as np
import itertools as it
from AnalyticalReasoning import Variable
import more_itertools as m_it

n = 5
group = numpy.empty(n, dtype=object)
A = Variable("A")
B = Variable("B")
C = Variable("C")
D = Variable("D")
E = Variable("E")
F = Variable("F")
G = Variable("G")
H = Variable("H")
I = Variable("I")
group[0] = I
group[1] = H
group[2] = G
group[3] = F
group[4] = E
print(len(group))

children = m_it.distribute(3, [1, 2, 3, 4, 5, 6, 7])

distinct_lists = []
for perm in it.permutations([1,2,3,4,5,6]):
    lists = [set(s) for s in m_it.split_into(perm, [1,2,3])]
    #print(lists)
    if(lists not in distinct_lists):
        distinct_lists.append(lists)
        print(lists)
#print(distinct_lists)