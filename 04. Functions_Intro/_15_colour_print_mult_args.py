"""
    We install this package just to be able to view colours when we
    execute the script from a windows command prompt.
"""
import colorama

# Some ANSI escape sequences for colours and effects
BLACK = '\u001b[30m'
RED = '\u001b[31m'
GREEN = '\u001b[32m'
YELLOW = '\u001b[33m'
BLUE = '\u001b[34m'
MAGENTA = '\u001b[35m'
CYAN = '\u001b[36m'
WHITE = '\u001b[37m'
RESET = '\u001b[0m'

BOLD = '\u001b[1m'
UNDERLINE = '\u001b[4m'
REVERSE = '\u001b[7m'


def colour_print(text: str, *effects: str) -> None:
    """
    Print `text` using the ANSI sequence to chance colour, etc

    :param text: The text to print.
    :param effects: The effects we want. One of the constants defined
        at the start of this module.
    """
    # we add this line to join a variable list of effect arguments
    effect_string = ''.join(effects)
    #
    output_string = '{}{}{}'.format(effect_string, text, RESET)
    print(output_string)


colorama.init()
# test that the colour was reset
print('This should be in a default terminal colour')
colour_print('TEST', BLUE)
colour_print('TEST', RED)
# variable argument testing
colour_print('TEST in Red, and Bold', RED, BOLD)
colour_print('TEST in Blue, and Reversed', BLUE, REVERSE)
colour_print('TEST in Blue, reversed and underlined', BLUE, REVERSE, UNDERLINE)
#
colour_print('TEST', CYAN)
colour_print('TEST', BOLD)
colour_print('TEST', UNDERLINE)
colour_print('TEST', REVERSE)
colorama.deinit()



