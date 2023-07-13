#!/usr/bin/env python3

import re
import csv
import sys
import time


def write_to_csv(filename, items):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(items)
  
    
def rank_errors(logs):
    """Take list of logs, 
    return a list of (error, int) tuples, ranked by int, 
    where int is how many times the error appeared in logs."""
    
    d = {}
    for log in logs:
        result = re.search(r"^.+ ERROR: (.+) \(\w+\)$", log)
        if result is None:
            pass
        elif result[1] in d:
            d[result[1]] += 1
        else:
            d[result[1]] = 1
    ranked_errors = sorted(d.items(), key=lambda item: item[1], reverse=True)
    ranked_errors.insert(0, ("Error", "Amount"))
    return ranked_errors
    
    
def sort_users_stat(logs):
    """Take list of logs,
    return a sorted by user name list, which includes
    (username, amount of info messages, amount of errors in logs.
    """
    d = {}
    for log in logs:
        result = re.search(r"^.+ (INFO|ERROR): .+ \((\w+)\)$", log)
        if result is None:
            pass
        elif result[2] in d:
            d[result[2]][result[1]] += 1
        else:
            second_message = "INFO" if result[1] == "ERROR" else "ERROR"
            d[result[2]] = {result[1]: 1, second_message: 0}
    sorted_stat = sorted(d.items())
    #sortd = dict(sorted(d.items()))
    result = []
    for stat in sorted_stat:
        one = [stat[0]]
        for key in sorted(stat[1].keys()):
            info = "{}:{}".format(key, stat[1][key])
            one.append(info)
        result.append(one)
    result.insert(0, ("Username", "Errors", "Infos"))
    return result
    #return sortd
  
  
if __name__ == "__main__":
    #logs_file = sys.argv[1]
    #with open(logs_file) as f:
    #    logs = list(f.readlines())
    logs = sys.stdin.readlines()    
    print(time.ctime())
    print("Logs from python script:")
    for log in logs:
        print(log.strip())
    print("=======================")
    ranked_errors = rank_errors(logs)
    sorted_stat = sort_users_stat(logs)
    #for err in ranked_errors:
    #    print("{}: {}".format(err[1], err[0]))
    #print(ranked_errors)
    #print(sorted_stat)
    write_to_csv("test_ranked_err.csv", ranked_errors)
    write_to_csv("test_sorted_stat.csv", sorted_stat)
