#!/usr/bin/env python
from distutils.core import setup
from distutils.cmd import Command

setup(name='autobib',
      version='0.1',
      description='Automatically creates a bibtex file from pdf's',
      author='Joacim Alvergren',
      author_email='joacim.alvergren@.com',
      url='http://github.com/joacima/autobib',
      scripts=['autobib.py'],
      py_modules=['*'])
