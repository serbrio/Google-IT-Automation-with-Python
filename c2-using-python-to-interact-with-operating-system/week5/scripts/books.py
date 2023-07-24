#!/usr/bin/env python3

import csv
import sys


def populate_dictionary(csv_file):
    """Function takes csv_file, populates dictionary with 
    Author(book): ["available"|"not available", "read"|"not read"]."""
    books_dict = {}
    with open(csv_file, encoding='utf-8') as csvfile:
        lines = csv.reader(csvfile, delimiter = ',')
        for row in list(lines)[3:]:
            book = str(row[2])
            available = lambda row: "available" if row[0] == "TRUE" else "not available"
            read = lambda row: "read" if row[1] == "TRUE" else "not read"
            books_dict[book] = [available(row), read(row)]
    return books_dict


def find_book(keyword, csv_file):
    """Return info about all books containing the given keyword 
    in the given csv_file."""
    if keyword is None:
        return None
    if type(keyword) != str:
        raise TypeError("keyword must be a string")
    books_dict = populate_dictionary(csv_file)
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
    while True:
        try:
            print("Enter <CTRL C> to quit")
            #csv_file = input('Enter path to csv file: ')
            csv_file = "../data/Avlbl_dsrbl_RU.csv"
            keyword_input = input('Enter key words: ')
            keyword = get_keyword([None, keyword_input])
            found_books = find_book(keyword, csv_file)
            print(represent_found(found_books))
        except KeyboardInterrupt:
            print('Quit: interrupted by user')
            raise
    #keyword = get_keyword(sys.argv)
    #found_books = find_book(keyword)
    #print(represent_found(found_books))
