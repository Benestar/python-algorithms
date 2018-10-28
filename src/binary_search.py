"""
Binary search algorithm
"""

def binary_search_list(lst, val):
    binary_search(lambda i: val - lst[i], 0, len(lst))


def binary_search(fn, begin, end, threshold=0):
    current = (begin + end) / 2

    while end - begin > threshold:
        val = fn(current)

        if val < 0:
            end = current
        elif val > 0:
            begin = current
        else:
            break

        current = (begin + end) / 2

    return current
