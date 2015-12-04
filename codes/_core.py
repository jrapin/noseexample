# -*- coding: utf-8 -*-
"""
Cardiologs Technologies - All rights reserved
Created on Fri Dec  4 16:58:32 2015
"""
import numpy as np


def _digits_to_number(digits):
    """Returns a number from a sequence of digits
    
    Example
    -------
    _digits_to_number([4, 3, 6])
    >>>> 436
    """
    return sum(val * 10**k for k, val in enumerate(digits[::-1]))


class Code(object):
    """4 digits code object
    """
    
    def __init__(self, number):
        # raise an exception if the input is incorrect (make it as explicit as possible)
        if not isinstance(number, int):
            raise TypeError("Expected an int but got an %s instead" % type(number))
        # check that it has 4 digits
        if number > 9999:
            raise ValueError("Number %s has more than 4 digits" % number)
        # save the number as a "private" variable (variables starting by "_" are considered private)
        self._number = number
    
    @property  # this makes digits act as an attribute instead of a method
    def digits(self):
        # convert number as a string, iterate on the letters, and reconvert each digit as a integer
        last_digits = [int(x) for x in "%s" % self._number]
        # pad with 0 for the remaining digits
        return np.array([0] * (4 - len(last_digits)) + last_digits)  # np.array allows for easy math operation

    
    # overload the + operator. Same thing would be done with * using __mult__, etc...
    def __add__(self, other):
        if not isinstance(other, Code):
            other = Code(other)
        digits = (self.digits + other.digits) % 10
        return Code(self._number + other._number)
