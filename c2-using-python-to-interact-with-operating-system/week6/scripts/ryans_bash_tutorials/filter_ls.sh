#!/bin/bash

cat /dev/stdin | awk '{print $9 " - " $5 " - " $3}'
