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
    if lst == []:
        return 0
    lst = lst[1:]
    return 1 + length(lst)


def reverse(lst: list) -> list:
    """Return the reverse of lst."""
    if length(lst) <= 1:
        print(lst)
        return lst
    return lst[-1:] + reverse(lst[1:-1]) + lst[:1]


def is_pal(lst: list) -> bool:
    """Return whether lst is a palindrome.

    For fun, do not use an if-statement.
    """
    return length(lst) <= 1 or (lst[0] == lst[-1] and is_pal(lst[1:-1]))


def num_el(lst: list) -> int:
    """Return the number of (non-list) elements of lst, on any nesting
    level.
    """
    if lst == []:
        return 0
    if isinstance(lst[0], list):
        return num_el(lst[0]) + num_el(lst[1:])
    return 1 + num_el(lst[1:])


def sum_els(lst: list) -> int:
    """Return the sum of all numbers in lst, on any nesting level. Return
    0 on an empty list.

    """
    if lst == []:
        return 0
    if isinstance(lst[0], list):
        return sum_els(lst[0]) + sum_els(lst[1:])
    return lst[0] + sum_els(lst[1:])


def repeat_twice(lst: list) -> list:
    """Return a list of elements of lst, each repeated twice, in the same
    order as they appear in lst.

    >>> repeat_twice(['c', '2', '4'])
    ['c', 'c', '2', '2', '4', '4']
    """
    if lst == []:
        return lst
    double = lst[:1]
    double.append(lst[0])
    return double + repeat_twice(lst[1:])


def my_filter(func: callable, lst: list) -> list:
    """Return a list of those elements from lst that pass the function
    func (i.e., func(x) is True for element x in lst), in their
    original order.

    func is a boolean-valued function applicable to every element of
    lst.
    """
    if lst == []:
        return lst
    if func(lst[0]):
        return lst[:1] + my_filter(func, lst[1:])
    return my_filter(func, lst[1:])


def my_map(func: callable, lst: list) -> list:
    """Return a list of results of applying func to each element of lst.

    func is applicable to every element of lst.
    """
    if lst == []:
        return lst
    mod_list = [func(lst[0])]
    return mod_list + my_map(func, lst[1:])


if __name__ == "__main__":
    import doctest

    doctest.testmod()
