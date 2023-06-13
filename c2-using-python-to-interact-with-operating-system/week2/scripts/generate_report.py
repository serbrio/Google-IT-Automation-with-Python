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
    result = {}
    for d in employee_list:
      if d['Department'] not in result:
        result[d['Department']] = 1
      else:
        result[d['Department']] += 1
    """Version from Google:
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])
    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data
    """
    return result
    
    
def write_report(dictionary, report_file):
    """Writes a dictionary of department:amount to a file.
    Format:
    department1: amount1
    department2: amount2"""
    with open(report_file, 'w', encoding="utf-8") as file:
        for k in sorted(dictionary):
            formatted_string = "{:*>30}: {}\n".format(k, dictionary[k])
            file.write(formatted_string)
    
    
employee_list = read_employees('../data/employees.csv')
#print(employee_list)
dictionary = process_data(employee_list)
print(dictionary)
write_report(dictionary, '../data/report.txt')