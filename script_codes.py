# -*- coding: utf-8 -*-
"""
Cardiologs Technologies - All rights reserved
Created on Fri Dec  4 16:57:53 2015
"""

# this import is possible because Code is imported in codes/__init__.py
from codes import Code

code = Code(123)
# we have just tested if the initialization worked

# test that it fails
code = Code("whatever")

# we can "catch" the exception so that it is not raised anymore
try:
    code = Code("whatever")
except TypeError as e:
    print("You did something wrong, we just caught this error: %s" % e)


# tests have been added!
# from noseexample folder, call "nosetests codes" to test the codes package
# this will look for functions with "test" in their name, in modules with "test" in their name
# one of them will fail, to show what a failing test does. This will test be removed afterwards
#
# if nosetests is not defined: "pip install nose"