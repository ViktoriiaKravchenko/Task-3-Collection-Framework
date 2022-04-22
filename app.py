from collections import Counter
from functools import lru_cache


@lru_cache
def unique_characters(s):
    if not isinstance(s, str):
        raise TypeError("Text should be str")

    s_counted = Counter(s)
    values = s_counted.values()
    counter = 0

    for i in values:
        if i == 1:
            counter += 1
    return counter
