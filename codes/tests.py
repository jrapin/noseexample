# -*- coding: utf-8 -*-
"""
Cardiologs Technologies - All rights reserved
Created on Fri Dec  4 17:05:53 2015
"""

import numpy as np
# inside a package, use . to import a module in the current folder, ".." for something in the above folder, etc.
from . import _core


def test_code_initialization():
    # you can add a docstring to explain the test, in practice I do not do it anymore,
    # because this is not convenient when using "genty" (package which helps you make plenty of codes)    
    _core.Code(1230)  # this should work


def test_code_initialization_that_fails():
    # Just do not do this. This is only to show what nosetests does when an error is raised
    _core.Code("whatever")


def test_code_initialization_error():
    # test that a TypeError is raised when calling _core.Codes with parameter "whatever"
    np.testing.assert_raises(TypeError, _core.Code, "whatever")
