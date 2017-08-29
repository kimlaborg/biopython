# Copyright 2000 by Jeffrey Chang.  All rights reserved.
# This code is part of the Biopython distribution and governed by its
# license.  Please see the LICENSE file that should have been included
# as part of this package.
# flake8: noqa
"""Collection of modules for dealing with biological data in Python.

The Biopython Project is an international association of developers
of freely available Python tools for computational molecular biology.

http://biopython.org
"""
__version__ = "2.0.2.dev0"

__all__ = [
    'KDTree',
    'PDB',
    'SVDSuperimposer',
]
from . import *
