#!/usr/bin/env python3

import argparse

def linear_search(lst, key):
    """If key is in the list returns its position in the list,
       otherwise returns -1."""
    print("=LINEAR search=")
    for i, item in enumerate(lst):
        if item == key:
            return i
    return -1


def binary_search(lst, key):
    """Returns the position of key in the list if found, -1 otherwise.

    List must be sorted.
    """
    print("=BINARY search=")
    left = 0
    right = len(lst) - 1
    while left <= right:
        middle = (left + right) // 2
        
        if lst[middle] == key:
            return middle
        if lst[middle] > key:
            right = middle - 1
        if lst[middle] < key:
            left = middle + 1
    return -1


def get_list(file):
    """Reads lines from the given file
    and appends them to the list.
    Returns the list.
    """
    lst = []
    with open(file) as f:
        for line in f:
            lst.append(line.strip())
    return lst


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", default="linear", help="select type of search: linear or binary; default: linear")
    parser.add_argument("key", help="search key")
    parser.add_argument("file", help="path to file with the list; if binary search, list must be sorted")
    args = parser.parse_args()
    file = args.file
    key = args.key
    #print("args.key: {}".format(key))
    #print(type(key))
    lst = get_list(file)
    if args.type == "linear":
        print(linear_search(lst, key))
    elif args.type == "binary":
        print(binary_search(lst, key))
    else:
        print("unknown search type")
