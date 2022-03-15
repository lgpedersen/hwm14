#!/usr/bin/env python
import setuptools  # noqa: F401
from numpy.distutils.core import setup, Extension

ext = Extension(name="hwm14fort", sources=["src/hwm14.f90"], f2py_options=["only:", "hwm14", ":", "--quiet"])

setup(ext_modules=[ext], data_files=[('hwm14/data', ['hwm14/data'])])
