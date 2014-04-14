#!/usr/bin/env python

from distutils.core import setup

setup(name='MakeSensePy',
      version='0.1',
      description='MakeSense database API for python',
      author='Oscar Robinson',
      author_email='oscar@make-sense.co.uk',
      url='http://www.make-sense.co.uk',
      py_modules = ['makesensepy'],
      require = ['requests>=2.3']
     )
