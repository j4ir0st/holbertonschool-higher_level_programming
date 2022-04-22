#!/usr/bin/python3
""" Test function find_peak """


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    if not list_of_integers:
        return (None)

    size = len(list_of_integers)
    half_size = int(size / 2)

    if (half_size + 1 >= size) and (half_size - 1 < 0):
        return (list_of_integers[half_size])
    elif (half_size - 1 < 0):
        if (list_of_integers[half_size] > list_of_integers[half_size + 1]):
            return (list_of_integers[half_size])
        else:
            return (list_of_integers[half_size + 1])
    elif (half_size + 1 >= size):
        if (list_of_integers[half_size] > list_of_integers[half_size - 1]):
            return (list_of_integers[half_size])
        else:
            return (list_of_integers[half_size - 1])

    if list_of_integers[half_size - 1] < list_of_integers[half_size] \
    > list_of_integers[half_size + 1]:
        return (list_of_integers[half_size])

    if (list_of_integers[half_size + 1] > list_of_integers[half_size - 1]):
        return (find_peak(list_of_integers[half_size:]))

    return (find_peak(list_of_integers[:half_size]))
