#!/usr/bin/env python3

import csv
import sys


def populate_dictionary(filename):
    """Populate dictionary with Available/Read/Author(book)"""
    books_dict = {}
    with open(filename, encoding='utf-8') as csvfile:
        lines = csv.reader(csvfile, delimiter = ',')
        for row in list(lines)[3:]:
            book = str(row[2])
            available = lambda row: "available" if row[0] == "TRUE" else "not available"
            read = lambda row: "read" if row[1] == "TRUE" else "not read"
            books_dict[book] = [available(row), read(row)]
    return books_dict


def find_book(keyword):
    """Return info about all books containing the given keyword"""
    if keyword is None:
        return None
    if type(keyword) != str:
        raise TypeError("keyword must be a string")
    books_dict = populate_dictionary("../data/Available and desirable_dtsk.csv")
    found_books = []
    for book_name in books_dict.keys():
        if keyword.lower() in book_name.lower():
            if_available = "[" + books_dict[book_name][0] + "]"
            if_read = "[" + books_dict[book_name][1] + "]"
            found_books.append((if_available, if_read, book_name))
    return found_books


def get_keyword(argv):
    keywords = []
    if len(argv) == 1:
        return None
    for i in range(1, len(argv)):
        if str(argv[i].strip()):
                keywords.append(str(argv[i]).strip())
    if len(keywords) == 0:
        return None
    else:
        keyword = " ".join(keywords).strip()
        return keyword


def represent_found(found_books):
    """Print nicely found books"""
    if found_books is None:
        return "missing keyword"
    elif found_books == []:
        return "not found"
    else:
        repr_found = []
        for if_available, if_read, book_name in found_books:
            repr_book = "{:<15} {:<22} {}".format(if_available, if_read, book_name)
            repr_found.append(repr_book)
        return '\n'.join(repr_found)


if __name__ == "__main__":
    keyword = get_keyword(sys.argv)
    found_books = find_book(keyword)
    print(represent_found(found_books))
