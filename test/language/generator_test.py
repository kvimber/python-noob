def test_generators_for_dict():
    dict1 = {"a": 1, "b": 2, "c": 3}
    dict2 = {"d": 4, "e": 5, "f": 6}

    even_dict = ((key, dict2[key]) for key in dict2 if dict2[key] % 2 == 0)

    assert dict(even_dict) == {"d": 4, "f": 6}


def test_generators_iter():
    dict2 = {"d": 4, "e": 5, "f": 6}

    even_dict = ((key, dict2[key]) for key in dict2 if dict2[key] % 2 == 0)

    for key, value in even_dict:
        print(f"- key: {key}, value: {value}")

    # un-comment the line below to see printing at work
    # assert False


def test_generator_fn_that_returns_dict():
    def create_dict_fn(input_value):
        return {"a": input_value}

    even_dict = (create_dict_fn(x) for x in range(10) if x % 2 == 0)

    answers = [{"a": 0}, {"a": 2}, {"a": 4}, {"a": 6}, {"a": 8}]

    for index, item in enumerate(even_dict):
        assert item == answers[index]
        print(f"- {item}")

    # assert False
