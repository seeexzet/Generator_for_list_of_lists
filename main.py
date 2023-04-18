import types


def flat_generator(list_of_lists):
    main_cursor = 0
    cursor = 0

    len_list = len(list_of_lists)

    for main_cursor in range(0, len_list):
        len_len_list = len(list_of_lists[main_cursor])
        for cursor in range(0, len_len_list):
            yield list_of_lists[main_cursor][cursor]


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)

    for item in flat_generator(list_of_lists_1):
        print(item)


if __name__ == '__main__':
    test_2()
