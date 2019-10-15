# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 14:39:02 2019

@author: aaron.drake
"""

class SelectionPool:
    pass

class Variable:
    subgroups = []
    
    def __init__(self,label):  
        self.label = label;
        
    def __repr__(self):
        return self.label
    
    def __str__(self):
        return self.label
    
    
    # necessary condition indicators words
    def is_necessary(self, var):
        return lambda group: self in group if var in group else True # should return True of False in else condition?
    
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
        return lambda group: var in group if self in group else True
    
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
