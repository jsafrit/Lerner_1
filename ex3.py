import types


def my_range(first, second=None, step=1):
    if second is not None:
        start = first
        stop = second
    else:
        start = 0
        stop = first

    result = []

    x = start
    while x < stop:
        result.append(x)
        x += step

    return result


def my_range_gen(first, second=None, step=1):
    if second is not None:
        start = first
        stop = second
    else:
        start = 0
        stop = first

    x = start
    while x < stop:
        yield x
        x += step


if __name__ == '__main__':
    assert my_range(4) == [0, 1, 2, 3]
    assert my_range(1, 6) == [1, 2, 3, 4, 5]
    assert my_range(1, 10, 2) == [1, 3, 5, 7, 9]
    assert isinstance(my_range(3), list)

    assert list(my_range_gen(4)) == [0, 1, 2, 3]
    assert list(my_range_gen(1, 6)) == [1, 2, 3, 4, 5]
    assert list(my_range_gen(1, 10, 2)) == [1, 3, 5, 7, 9]
    assert list(my_range_gen(3, 25, 4)) == [3, 7, 11, 15, 19, 23]
    my_gen = my_range_gen(3, 25, 4)
    for i in range(6):
        print('{}  {}'.format(i, next(my_gen)))
    assert isinstance(my_range_gen(3), types.GeneratorType)
