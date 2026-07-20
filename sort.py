## Importing libraries
import random

def random_sort(cards):
    result = list(cards)
    random.shuffle(result)

    return result

def DESC_sort(cards):
    result = list(cards)
    result.sort()
    result.reverse()

    return result

def ASC_sort(cards):
    result = list(cards)
    result.sort()

    return result