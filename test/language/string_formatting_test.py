#####################################################
# string_formatting_test.py                         #
#                                                   #
# by: Kevin Imber <kvimber@gmail.com>               #
# on: Thu, Jun 16th, 2022                           #
#                                                   #
# Testing string formatting, specifically.          #
# Other string manipulation should go into          #
#   other testing files                             #
#                                                   #
# Links & guides on string formatting:              #
# - https://pyformat.info: best examples I've seen  #
#####################################################


def test_named_placeholders_from_dict():
    """
    Good example of Hettinger quote about never be referring to items by their index
    see test/collections/destructuring_test.py#test_destructuring_by_name for the quote

    Actually came from https://pyformat.info/#named_placeholders
    """
    data = {
        'first': 'Morbius',
        'last': 'Morbin',
        'middle': 'Time'
    }
    # NOTE: You have to destructure the dict to pass kwargs for this to work!
    test_str = '{first} {last} {middle}'.format(**data)
    assert test_str == 'Morbius Morbin Time'


def test_named_placeholders_from_kwargs():
    """
    Good example of Hettinger quote about never be referring to items by their index
    see test/collections/destructuring_test.py#test_destructuring_by_name for the quote

    Actually came from https://pyformat.info/#named_placeholders
    """
    capt_jack = "Sparrow"
    jean_luc = "Picard"

    test_str = '{first} {last}'.format(first=capt_jack, last=jean_luc)
    assert test_str == 'Sparrow Picard'