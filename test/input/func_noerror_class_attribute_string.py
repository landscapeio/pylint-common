"""
Checks that Pylint does not complain about certain aspects of the Celery library
"""
#  pylint: disable=C0111,R0903

SOME_CONSTANT = 'constant'
""" This is the doc for the constant """


class SomeClass(object):
    an_attribute = ['fish', 'cake']
    """ This is the doc for an_attribute """

    # the following two lines ensure that any pattern of 'assign' followed by
    # something which is not a simple constant do not throw errors
    another_attribute = 1
    an_attribute.sort('something')
