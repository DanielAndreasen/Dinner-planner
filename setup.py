#!/usr/bin/env python
# -*- coding: utf8 -*-

from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()

setup(name='dinnerPlanner',
      version='0.1',
      description='Plan dinner for several days',
      long_description=readme(),
      url='https://github.com/DanielAndreasen/Dinner-planner',
      author='Daniel T. Andreasen',
      author_email='daniel.andreasen@hotmail.com',
      license='MIT',
      packages=['dinnerPlanner'],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'])
