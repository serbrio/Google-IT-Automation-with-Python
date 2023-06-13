#!/usr/bin/env python3

import csv


def read_employees(csv_file_location):
    """Receives the CSV file and returns 
    a list of dictionaries from that file."""
    employee_list = []
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    with open (csv_file_location, newline='') as csvfile:
      reader = csv.DictReader(csvfile, dialect='empDialect')    
      for row in reader:
        employee_list.append(row)
    return employee_list
    

def process_data(employee_list):
    """Receives the list of dictionaries, 
    i.e. employee_list as a parameter and return 
    a dictionary of department:amount."""
    pass
    
    
def write_report(dictionary, report_file):
    """Writes a dictionary of department:amount to a file.
    Format:
    <department1>: <amount1>
    <department2>: <amount2>"""
    pass
    
    
employee_list = read_employees('../data/employees.csv')
print(employee_list)
#dictionary = process_data(employee_list)
#print(dictionary)
#write_report(dictionary, '../data/report.txt')