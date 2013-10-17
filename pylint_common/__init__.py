from pylint.checkers.format import FormatChecker
from pylint_common.augmentations import apply_augmentations
from pylint_plugin_utils import get_checker


def register(linter):
    apply_augmentations(linter)

    format_checker = get_checker(linter, FormatChecker)
    format_checker.set_option('max-line-length', 160)