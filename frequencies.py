"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for item in items:
        key = str(item)
        if (key in frequencies.keys()):
            frequencies[key] = frequencies[key] + 1
        else:
            frequencies.update({key: 1})
    # Your code goes here
    return frequencies
