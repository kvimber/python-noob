

def test_dict_merge_operator():
    """
    AskPython says the BEST way to merge dicts is using the merge operator:
      1. https://www.askpython.com/python/dictionary/merge-dictionaries

    Also gives 3 other methods I haven't mentioned here.
    """
    dict1 = { 'a': 1, 'b': 2, 'c': 3 }
    dict2 = { 'd': 4, 'e': 5, 'f': 6 }

    dict1 |= dict2

    assert dict1 == { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6 }


def test_dict_merge_conflicts():
    dict1 = { 'a': 1, 'b': 2, 'c': 3 } # notice that both dicts have a 'c' key
    dict2 = { 'd': 4, 'e': 5, 'c': 6 }

    dict1 |= dict2 # looks like the right-side overrides in a collision
    assert dict1['c'] == 6 # verify this


def test_dict_merge_insanity():
    """
    Same AskPython article[1] has a different way to merge cards: by unpacking
    them using `kwargs`!!!
    """
    dict1 = { 'a': 1, 'b': 2, 'c': 3 }
    dict2 = { 'd': 4, 'e': 5, 'f': 6 }

    dict3 = {**dict1, **dict2}

    assert dict3 == { 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6 }

