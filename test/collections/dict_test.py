
def test_dict_merge_operator():
    """
    AskPython says the BEST way to merge dicts is using the merge operator:
      https://www.askpython.com/python/dictionary/merge-dictionaries

    Also gives 3 other methods I haven't mentioned here.
    """
    dict1 = { 'a': 1, 'b': 2, 'c': 3 }
    dict2 = { 'd': 4, 'e': 5, 'f': 6 }

    dict1 |= dict2

    assert dict1 == { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6 }

# TODO what about merge conflicts?

