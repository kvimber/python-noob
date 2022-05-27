########
# destructuring_test.py
#
#
# Refs:
# 1. https://blog.teclado.com/destructuring-in-python/


def test_splat_first():
    """Splat operator grabs all not-first values (from 1)"""
    head, *tail = [1, 2, 3, 4]
    assert head == 1
    assert tail == [2, 3, 4]


def test_splat_last():
    """Splat operator grabs all not-last values (from 1)"""
    *head, tail = [5, 6, 7, 8]
    assert head == [5, 6, 7]
    assert tail == 8


def test_splat_middle():
    """Splat operator grabs all middle values (from 1)"""
    head, *middle, tail = [9, 10, 11, 12, 13]
    assert head == 9
    assert middle == [10, 11, 12]
    assert tail == 13


def test_destructure_by_name():
    """
    Raymond Hettinger (a core Python dev) said

      In Python, you should basically never be referring to items by their index.
      There's nearly always a better way

    from 1
    """
    people = [
        ("Bob", 42, "Mechanic"),
        ("James", 24, "Artist"),
        ("Harry", 32, "Lecturer"),
    ]

    for name, age, profession in people:
        print(f"Name: {name}, Age: {age}, Profession: {profession}")
