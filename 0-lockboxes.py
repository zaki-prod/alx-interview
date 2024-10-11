#!/usr/bin/python3
"""Determines if all boxes can be unlocked using keys found in other boxes via DFS."""


def canUnlockAll(boxes):
    """This function will take a list of lists and the content
       of a list will unlock other lists
    """

    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < len(boxes):
                keys.append(boxKey)
    if len(keys) == len(boxes):
        return True
    return False
