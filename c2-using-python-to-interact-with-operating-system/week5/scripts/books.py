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
    books_dict = populate_dictionary("../data/Available and desirable_dtsk.csv")
    found_books = []
    for key in books_dict.keys():
        if keyword in key:
            found_books.append((books_dict[key][0], books_dict[key][1], key)) 
    return found_books


def main():
    keyword = str(' '.join(sys.argv[1:]))
    found_books = find_book(keyword)
    if len(found_books) == 0:
        print("not found")
    else:
        for book in found_books:
            print("{:<15} {:<22} {}\n".format("[" + book[0] + "]", "[" +  book[1] + "]", book[2]))


if __name__ == "__main__":
    main()
