# -*- coding: utf-8 -*-
"""
Cardiologs Technologies - All rights reserved
Created on Fri Dec  4 16:58:32 2015
"""


class Code(object):
    """4 digits code object
    """
    
    def __init__(self, number):
        # raise an exception if the input is incorrect (make it as explicit as possible)
        if not isinstance(number, int):
            raise TypeError("Expected an int but got an %s instead" % type(number))
        # save the number as a "private" variable (variables starting by "_" are considered private)
        self._number = number
    
    @property  # this makes digits act as an attribute instead of a method
    def digits(self):
        # convert number as a string, iterate on the letters, and reconvert each digit as a integer
        return [int(x) for x in "%s" % self._number]
