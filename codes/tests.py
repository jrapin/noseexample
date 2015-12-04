# -*- coding: utf-8 -*-
"""
Cardiologs Technologies - All rights reserved
Created on Fri Dec  4 17:05:53 2015
"""

import numpy as np
# we will use genty to avoid code duplication
from unittest import TestCase
import genty

# inside a package, use . to import a module in the current folder, ".." for something in the above folder, etc.
from . import _core


def test_code_initialization():
    # you can add a docstring to explain the test, in practice I do not do it anymore,
    # because this is not convenient when using "genty" (package which helps you make plenty of codes)    
    _core.Code(1230)  # this should work


def test_code_initialization_error():
    # test that a TypeError is raised when calling _core.Codes with parameter "whatever"
    np.testing.assert_raises(TypeError, _core.Code, "whatever")


def test_get_figures():
    code = _core.Code(1230)
    # np.testing has plenty of convenient functions for testing results (or errors, as shown above)
    # Writing a small description of your test in err_msg can be convenient to help you debug
    # (though np.testing errors are well detailled)
    np.testing.assert_equal(code.digits, [1, 2, 3, 0], err_msg="Wrong digits")


def test_get_figures_small():
    # one can make several small assertions in one test function. Splitting them can however make bugs appear more clearly
    # In practice, "genty" package will help us deal with this kind of repeated tests.
    code = _core.Code(230)
    expected = [0, 2, 3, 0]
    np.testing.assert_equal(code.digits, expected, err_msg="Wrong digits for 3 digit long number"
                            "expected %s, got %s" % (expected, code.digits))


# the syntax is a bit more complicated, but it is always the same...
# we create a class, and the tests are the methods from this class
@genty.genty
class CodeTests(TestCase):
    
    # here we define several cases in which to run the tests:
    # in the style: name_of_the_test(code_value, error)
    @genty.genty_dataset(
        standard=(1230, None),
        typeerror=("whatever", TypeError),
        moredigits=(51230, ValueError),
        limit_up=(10000, ValueError), # let us test limit cases
        limit_down=(9999, None),
    )
    def test_code_initialization(self, code_value, error):
        if error is None:  # if no error to raise, just try the initialization
            _core.Code(code_value)
        else:  # otherwise check that it raises the error
            np.testing.assert_raises(error, _core.Code, code_value)
    
    
    @genty.genty_dataset(
        standard=(1230, [1, 2, 3, 0]),
        small=(230, [0, 2, 3, 0]),
        null=(0, [0, 0, 0, 0]),  # limit case
    ) 
    def test_get_figures_small(self, code_value, expected):
        code = _core.Code(code_value)
        np.testing.assert_equal(code.digits, expected, err_msg="Wrong digits for 3 digit long number"
                                "expected %s, got %s" % (expected, code.digits))
