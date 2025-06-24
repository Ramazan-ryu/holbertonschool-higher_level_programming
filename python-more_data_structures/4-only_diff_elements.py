#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    result = set()
    for word in set_1:
        if word not in set_2:
            result.add(word)
    for word in set_2:
        if word not in set_1:
            result.add(word)
    return result
