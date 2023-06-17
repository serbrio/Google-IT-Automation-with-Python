#!/usr/bin/env python3
import re
import sys

logfile = sys.argv[1]
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"CMD \((.+)\)$"
        result = re.search(pattern, line)
        print(result[1])
