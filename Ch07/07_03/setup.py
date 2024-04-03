"""Setup for sqrt lib"""

from distutils.core import setup
from Cython.Build import cythonize

setup(
    ext_modules=cythonize('cysqrt.pyx'),
)
