#!/usr/bin/env python3

import re
import csv
import sys
import time


def write_to_csv(filename, d, fieldnames):
    with open(filename, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames)
        writer.writeheader()
        writer.writerows(d.values())
  
    
def rank_errors(logs):
    """Take list of logs, 
    return a dict sorted reversed by int in 'OCCURED', 
    dict items structure:
    error: {"ERROR": error, "OCCURED": n}"""
    d = {}
    for log in logs:
        result = re.search(r"^.+ ERROR: (.+) \(\w+\)$", log)
        if result is None:
            pass
        elif result[1] in d:
            d[result[1]]["OCCURED"] += 1
        else:
            d[result[1]] = {"ERROR": result[1], "OCCURED": 1}
    ranked_errors = sorted(d.items(), key=lambda item: item[1]["OCCURED"], reverse=True)
    return dict(ranked_errors)
    
    
def sort_users_stat(logs):
    """Take list of logs,
    return a dict sorted by user name, which items structure:
    user_name: {"USERNAME": user_name, "ERROR": n, "INFO": n}
    """
    d = {}
    for log in logs:
        result = re.search(r"^.+ (INFO|ERROR): .+ \((\w+)\)$", log)
        try:
            msg, username = result.groups()
        except AttributeError:
            pass   
        if result is None:
            pass
        elif username in d:
            d[username][msg] += 1
        else:
            second_message = "INFO" if msg == "ERROR" else "ERROR"
            d[username] = {"USERNAME": username, msg: 1, second_message: 0}
    sortd = sorted(d.items())
    return dict(sortd)
  
  
if __name__ == "__main__":
    #logs_file = sys.argv[1]
    #with open(logs_file) as f:
    #    logs = list(f.readlines())
    logs = sys.stdin.readlines()
    print("=======================")    
    print(time.ctime())
    print("Logs from python script:")
    for log in logs:
        print(log.strip())
    ranked_errors = rank_errors(logs)
    sorted_stat = sort_users_stat(logs)

    errors_fieldnames = ["ERROR", "OCCURED"]
    stat_fieldnames = ["USERNAME", "ERROR", "INFO"]
    
    write_to_csv("err.csv", ranked_errors, errors_fieldnames)
    write_to_csv("stat.csv", sorted_stat, stat_fieldnames)
