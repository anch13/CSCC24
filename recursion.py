"""Review: some simple exercises on recursion. Use Python3.11.  Please
implement ALL of the following RECURSIVELY.  Otherwise it defeats the
purpose of this lab --- we need to freshen up on our recursion skills.

You have until Friday 6p.m. to submit your work on MarkUs.

For full marks, this and every other piece of Python code you submit
must pass flake8 and pylint. See course website for required versions
of the software.

"""


def length(lst: list) -> int:
    """Return the number of elements (top level) in lst."""

    pass


def reverse(lst: list) -> list:
    """Return the reverse of lst."""

    pass


def is_pal(lst: list) -> bool:
    """Return whether lst is a palindrome.

    For fun, do not use an if-statement.
    """

    pass


def num_el(lst: list) -> int:
    """Return the number of (non-list) elements of lst, on any nesting
    level.
    """

    pass


def sum_els(lst: list) -> int:
    """Return the sum of all numbers in lst, on any nesting level. Return
    0 on an empty list.

    """

    pass


def repeat_twice(lst: list) -> list:
    """Return a list of elements of lst, each repeated twice, in the same
    order as they appear in lst.

    >>> repeat_twice(['c', '2', '4'])
    ['c', 'c', '2', '2', '4', '4']
    """

    pass


def my_filter(func: callable, lst: list) -> list:
    """Return a list of those elements from lst that pass the function
    func (i.e., func(x) is True for element x in lst), in their
    original order.

    func is a boolean-valued function applicable to every element of
    lst.
    """

    pass


def my_map(func: callable, lst: list) -> list:
    """Return a list of results of applying func to each element of lst.

    func is applicable to every element of lst.
    """

    pass


if __name__ == "__main__":
    import doctest

    doctest.testmod()
