"""
Checks that Pylint does not complain about certain aspects of the Celery library
"""
#  pylint: disable=C0111,R0903


class SomeClass(object):
    an_attribute = 1
    """ This is the doc for an_attribute """
