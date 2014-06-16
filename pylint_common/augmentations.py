from pylint.checkers.base import BasicChecker, astroid
from pylint_plugin_utils import augment_visit


# grumble grumble python3 grumble
try:
    BASESTRING = basestring
except NameError:
    BASESTRING = str


def allow_attribute_comments(chain, node):
    """
    This augmentation is to allow comments on class attributes, for example:

    class SomeClass(object):
        some_attribute = 5
        ''' This is a docstring for the above attribute '''
    """

    # TODO: find the relevant citation for why this is the correct way to comment attributes
    if isinstance(node.previous_sibling(), astroid.Assign) and \
            isinstance(node.parent, (astroid.Class, astroid.Module)) and \
            isinstance(node.value, astroid.Const) and \
            isinstance(node.value.value, BASESTRING):
        return

    chain()


def apply_augmentations(linter):
    augment_visit(linter, BasicChecker.visit_discard, allow_attribute_comments)
