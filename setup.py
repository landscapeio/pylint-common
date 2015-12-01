# -*- coding: UTF-8 -*-
from distutils.core import setup
from setuptools import find_packages


_version = '0.2.2'
_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

_short_description = "pylint-common is a Pylint plugin to improve Pylint error analysis of the" \
                     "standard Python library"

_classifiers = (
    'Development Status :: 4 - Beta',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Operating System :: Unix',
    'Topic :: Software Development :: Quality Assurance',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
)

setup(
    name='pylint-common',
    url='https://github.com/landscapeio/pylint-common',
    author='landscape.io',
    author_email='code@landscape.io',
    description=_short_description,
    version=_version,
    packages=_packages,
    install_requires=['pylint>=1.0', 'astroid>=1.0', 'pylint-plugin-utils>=0.2.1'],
    license='GPLv2',
    classifiers=_classifiers,
    keywords='pylint stdlib plugin',
    zip_safe=False  # see https://github.com/landscapeio/prospector/issues/18#issuecomment-49857277
)
