def conserve_links(a, b):
    """Makes Linked List a share as many Link instances as possible with
        Linked List b. a can use b's i-th Link instance as its i-th Link
        instance if a and b have the same element at position i.

    Should mutate a. b is allowed to be destroyed. Returns the new first
        Link instance of a.

    >>> x = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6))))))
    >>> y = Link(1, Link(9, Link(3, Link(4, Link(9, Link(6))))))
    >>> z = conserve_links(x, y)
    >>> curr_x, curr_z = x, z
    >>> while curr_z is not Link.empty:
    >>>     assert curr_z.first == curr_x.first
    >>>     curr_x, curr_z = curr_x.rest, curr_z.rest
    >>> assert z == y
    >>> assert z.rest.rest == y.rest.rest
    >>> assert z.rest.rest.rest.rest.rest == y.rest.rest.rest.rest.rest
    >>> assert z.rest.rest.rest.rest.rest == y.rest.rest.rest.rest.rest
    """

def slice_reverse(s, i, j):
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> slice_reverse(s, 1, 2)
    >>> s
    Link(1, Link(2, Link(3)))
    >>> s = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> slice_reverse(s, 2, 4)
    >>> s
    Link(1, Link(2, Link(4, Link(3, Link(5)))))
    """
    start = s
    for i in range(i) :
        start = start.rest
    reverse = Link.empty
    current = start
    for j in range(j-i) :
        temp = current
        current.rest = reverse
        reverse = current
        current = temp.rest
    start.rest.rest = current
    start.rest = reverse
