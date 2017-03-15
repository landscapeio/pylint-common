# -*- coding: UTF-8 -*-
import sys
from setuptools import find_packages, setup


_version = '0.2.5'
_packages = find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"])

_short_description = ("pylint-common is a Pylint plugin to improve Pylint "
                      "error analysis of the standard Python library")

_classifiers = (
    'Development Status :: 6 - Mature',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'Operating System :: Unix',
    'Topic :: Software Development :: Quality Assurance',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
)


if sys.version_info < (2, 7):
    # pylint 1.4 dropped support for Python 2.6
    _install_requires = [
        'pylint>=1.0,<1.4',
        'astroid>=1.0,<1.3.0',
        'logilab-common>=0.60.0,<0.63',
        'pylint-plugin-utils>=0.2.6',
    ]
else:
    _install_requires = [
        'pylint>=1.0',
        'pylint-plugin-utils>=0.2.5',
    ]


setup(
    name='pylint-common',
    url='https://github.com/landscapeio/pylint-common',
    author='landscape.io',
    author_email='code@landscape.io',
    description=_short_description,
    version=_version,
    packages=_packages,
    install_requires=_install_requires,
    license='GPLv2',
    classifiers=_classifiers,
    keywords='pylint stdlib plugin',
    zip_safe=False  # see https://github.com/landscapeio/prospector/issues/18#issuecomment-49857277
)
