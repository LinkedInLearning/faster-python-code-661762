"""Setup script for csqrt.c"""
from setuptools import setup, Extension

setup(
   name='csqrt',
   version='0.1.0',
   description='Demo C module',
   ext_modules=[Extension('csqrt', sources=['csqrt.c'])],
)
