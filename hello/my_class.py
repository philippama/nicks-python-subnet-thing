class MyClass(object):
    """
    >>> mc = MyClass()
    >>> mc.add(2, 3)
    total = 5
    5

    >>> mc.add(6, 8)
    total = 14
    2
    """
    def __init__(self):
        pass

    def add(self, a, b):
        total = a + b
        print("total =", total)
        return total


if __name__ == '__main__':
    import doctest
    doctest.testmod()
