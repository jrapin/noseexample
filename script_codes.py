# -*- coding: utf-8 -*-
"""
Cardiologs Technologies - All rights reserved
Created on Fri Dec  4 16:57:53 2015
"""

# this import is possible because Code is imported in codes/__init__.py
from codes import Code

code = Code(1987)

# returns the code as a sequence of digits
# digits is defined like a function, but it acts as an attribute because it is a property:
# call it as an attribute, i.e not in this way: code.digits()
code.digits
