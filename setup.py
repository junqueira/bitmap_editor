setup.py
#!/usr/bin/env python
# coding: utf-8
"""
   File Name: setup.py
      Author: Luiz
      E-mail: lcjneto@gmail.com
  Created on: Thu May  3 09:00:00 2016 CST
"""
DESCRIPTION = """
"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='bitmap',
      version='0.0.1',
      author='Luiz',
      author_email='lcjneto@gmail.com',
      package_dir={'bitmap': 'src'},
      packages=['bitmap'],
      url='https://github.com/junqueira/bitmap',
      # license='LICENSE.txt',
      description='.',
      long_description=open('README.md').read(),
      install_requires=[
      ],
      )
