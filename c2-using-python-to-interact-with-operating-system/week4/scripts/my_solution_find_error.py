#!/usr/bin/env python3
import re
import sys
import os


logfile = sys.argv[1]
error_list = []

with open(logfile) as f:
    for line in f:
        if "CRON" not in line or "ERROR" not in line:
            continue
        print(line)
        pattern = r"^[a-zA-Z]+ \d+ [\d:]+ .+ CRON\[\d{5}\]: ERROR.*Failed to start.*$"
        result = re.search(pattern, line)
        if result is None:
            continue
        error_list.append(line)
print(error_list)

new_log = '../data/new_log.log'
with open(new_log, 'w') as f:
    f.writelines(error_list)
