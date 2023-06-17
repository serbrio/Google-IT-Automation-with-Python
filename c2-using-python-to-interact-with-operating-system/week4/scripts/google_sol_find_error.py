#!/usr/bin/env python3
import re
import sys
import os

def error_search(log_file):
    error = input("Enter the type of error to search: ")
    returned_errors = []
    with open(log_file, encoding="UTF-8") as file:
        for log in file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returned_errors.append(log)
        file.close()
    return returned_errors
    
    
def file_output(returned_errors):
    with open(os.path.abspath('..') + '/data/google_errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()
        

if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)