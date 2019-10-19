# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:39:02 2019

@author: aaron.drake
"""

import itertools as it
import more_itertools as m_it

def is_necessary(var):
    return var

def when(var):
    return is_necessary(var)

def whenever(var):
    return is_necessary(var)

def every(var):
    return is_necessary(var)

def all_(var):
    return is_necessary(var)

def any_(var):
    return is_necessary(var)

def people_who(var):
    return is_necessary(var)

def in_order_to(var):
    return is_necessary(var)

def select(var):
    return lambda group: is_selected(var, group)

def is_selected(var, group):
    return var in group if var.selected else var not in group

class Grouping:
    def solve(selection_pool, group_size_rules, rules):
        pass
    
    def solve(possibilities, group_size_rules, rules):
        solutions = []
        for possibility in possibilities:
            is_solution, message = Grouping.is_solution(possibility, group_size_rules, rules)
            if is_solution and possibility not in solutions:
                solutions.append(possibility)
        return solutions
    
    def split(iterable, group_sizes, indices):
        pool = tuple(iterable)
        n = len(pool)
        groups = []
        start = 0
        for size in group_sizes:
            groups.append(set([pool[i] for i in indices[start:start + size]]))
            start = start + size
        return groups
    
    def check_sizes(group, sizes):
        if len(group) != len(sizes):
            return False
        for i in range(len(sizes)):
            if len(group[i]) != sizes[i]:
                return False
        return True
              
    def split(selection_pool, group_sizes):
        groups = [item for item in m_it.set_partitions(selection_pool) if Grouping.check_sizes(item, group_sizes)]
        return list(map(tuple, groups))
    
    def generate_possibilities(pool, group_sizes, num_selected):
        # establish the distributions
        dist = group_sizes
        if group_sizes == None:
            dist = [num_selected - len(group_names) + 1]
            dist = np.append(arr=dist, values=np.ones(len(group_names)-1, dtype=int))
        possibilities = Grouping.split(pool, group_sizes)
        return possibilities
    
    def is_solution(possibility, group_size_rules, selection_rules):
        for group_size_rule in group_size_rules:
            if not group_size_rule(possibility):
                return False, f"failed group size rule: {group_size_rule}"
        for group in possibility:
            for rule in selection_rules:
                if not rule(group):
                    return False, f"failed selection size rule: {rule}"
            
        return True, f"{possibility} is a solution"

class Variable:
    selected = True
    subgroups = []
    
    def __init__(self,label):  
        self.label = label;
        
    def __repr__(self):
        return self.label
    
    def __str__(self):
        return self.label
    
    def __eq__(self,obj):
        return self.label == obj.label
    
    def __hash__(self):
        return hash(self.label)
    
    def __neg__(self):
        val = Variable(self.label)
        val.selected = not self.selected
        return val
    
    # necessary condition indicators words
    def is_necessary(self, var):
        return True#lambda group: self in group if var in group else True # should return True of False in else condition?
    
    def when(self, var):
        return self.is_necessary(var)
    
    def whenever(self, var):
        return self.is_necessary(var)
    
    def every(self, var):
        return self.is_necessary(var)
    
    def all_(self, var):
        return self.is_necessary(var)
    
    def any_(self, var):
        return self.is_necessary(var)
    
    def people_who(self, var):
        return self.is_necessary(var)
    
    def in_order_to(self, var):
        return self.is_necessary(var)
    
    # sufficient condition indicator words
    def is_sufficient(self, var):
        return lambda group: is_selected(var, group)  if is_selected(self, group) else True
    
    def then(self, var):
        return self.is_sufficient(var)

    def only(self, var):
        return self.is_sufficient(var)
    
    def onlyif(self, var):
        return self.is_sufficient(var)
    
    def must(self, var):
        return self.is_sufficient(var)
    
    def is_required(self, var):
        return self.is_sufficient(var)

    def is_precondition(self, var):
        return self.is_sufficient(var)
    
    def unless(self, var):
        return self.is_sufficient(var)
    
    def xcept(self, var):
        return self.is_sufficient(var)
    
    def until(self, var):
        return self.is_sufficient(var)
    
    def without(self, var):
        return self.is_sufficient(var)
    
