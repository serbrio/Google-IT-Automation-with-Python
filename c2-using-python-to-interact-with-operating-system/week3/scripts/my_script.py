#!/usr/bin/env python3

#import csv
import re

def process_data(filename):
    pattern = r'^(.*\w+)@(abc)\.edu$'
    replacement = r'\1@xyz.edu'
    newstrings = []
    with open(filename) as f:
        for line in f:
            newstring = re.sub(pattern, replacement, line)
            newstrings.append(newstring)
    #for string in newstrings:
    #    print(string)
    return newstrings

def write_to_file(newstrings, updated_file_name):
    with open(updated_file_name, 'w') as f:
        for string in newstrings:
            f.write(string)
    
newstrings = process_data('../data/user_emails.csv')
write_to_file(newstrings, '../data/updated_user_emails.csv')