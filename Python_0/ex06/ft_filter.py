def ft_filter(function, iterable):
    """
    function: a function to apply to each element of the iterable(or None)
    iterable: a sequence, iterator, or a container to filter
    return: an iterator with elements for which function(element) is True,
            or elements that are evaluated True if finction is None
    """
    if function:
        return (item for item in iterable if function(item))
    return (item for item in iterable if item)
