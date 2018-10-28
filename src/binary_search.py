"""
Binary search algorithm
"""

def binary_search_list(lst, val):
    binary_search(lambda i: val - lst[i], 0, len(lst))


def binary_search(fn, begin, end):
    current = (begin + end) / 2

    while True:
        val = fn(current)

        if val < 0:
            end = current
        elif val > 0:
            begin = current
        else:
            return current
        
        current = (begin + end) / 2
